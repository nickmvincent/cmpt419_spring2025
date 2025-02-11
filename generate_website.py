import os
import shutil
import markdown
import yaml
from pathlib import Path
from bs4 import BeautifulSoup
import pypdf
import re

class CourseWebsiteGenerator:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.docs_dir = self.root_dir / 'docs'
        self.template_dir = self.root_dir / '_templates'
        
        # Directory order as specified
        self.content_dirs = [
            'readings',
            'assignments',
            'slides',
            'misc_materials',
            'slides_pdfs'
        ]
        
        # Create required directories
        self.docs_dir.mkdir(exist_ok=True)
        
    def generate_navigation(self):
        """Generate the collapsible navigation structure."""
        nav = []
        
        for dir_name in self.content_dirs:
            dir_path = self.root_dir / dir_name if dir_name else self.root_dir
            if not dir_path.exists():
                continue
                
            section = {
                'name': dir_name if dir_name else 'Home',
                'items': []
            }
            
            for file_path in sorted(dir_path.glob('**/*')):
                if file_path.suffix.lower() in ['.md', '.pdf']:
                    relative_path = file_path.relative_to(self.root_dir)
                    # Convert .md paths to .html for links
                    if relative_path.suffix.lower() == '.md':
                        relative_path = relative_path.with_suffix('.html')
                    section['items'].append({
                        'title': self._get_title(file_path),
                        'path': str(relative_path)
                    })
            
            if section['items']:
                nav.append(section)
                
        return nav
    
    def _get_title(self, file_path):
        """Extract title from markdown front matter or filename."""
        if file_path.suffix.lower() == '.md':
            content = file_path.read_text(encoding='utf-8')
            if content.startswith('---'):
                try:
                    front_matter = content.split('---')[1]
                    metadata = yaml.safe_load(front_matter)
                    if 'title' in metadata:
                        return metadata['title']
                except:
                    pass
        
        # Fallback to filename
        return file_path.stem.replace('_', ' ').title()
    
    def _process_markdown(self, content):
        """Convert markdown to HTML with extensions."""
        extensions = [
            'meta',
            'fenced_code',
            'tables',
            'toc',
            'markdown.extensions.def_list',
            'markdown.extensions.attr_list',
            'markdown.extensions.nl2br',
            'markdown.extensions.smarty',
            'markdown.extensions.sane_lists'
        ]
        
        # Normalize list indentation in the content
        lines = content.split('\n')
        normalized_lines = []
        in_list = False
        for line in lines:
            stripped = line.lstrip()
            if stripped.startswith(('- ', '* ', '+ ')):
                # Count leading spaces
                indent = len(line) - len(stripped)
                # Normalize to 4 spaces per level (standard markdown indent)
                level = indent // 2  # Assuming input uses 2 spaces
                normalized_line = ('    ' * level) + stripped
                normalized_lines.append(normalized_line)
                in_list = True
            else:
                if in_list and not stripped:
                    # Preserve empty lines in lists
                    normalized_lines.append('')
                else:
                    normalized_lines.append(line)
                    in_list = False
        
        normalized_content = '\n'.join(normalized_lines)
        md = markdown.Markdown(extensions=extensions)
        return md.convert(normalized_content)
    
    def _process_pdf(self, pdf_path):
        """Extract PDF info and create a viewer page."""
        reader = pypdf.PdfReader(pdf_path)
        info = reader.metadata
        
        return f"""
        <div class="pdf-container">
            <h1>{pdf_path.stem}</h1>
            <embed src="{pdf_path.name}" type="application/pdf" width="100%" height="800px">
        </div>
        """
    
    def _create_page(self, content, title, nav):
        """Create a full HTML page with navigation."""
        template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
            <link rel="stylesheet" href="assets/style.css">
        </head>
        <body>
            <div class="sidebar">
                <nav>{nav_html}</nav>
            </div>
            <div class="content">
                {content}
            </div>
            <script src="assets/script.js"></script>
        </body>
        </html>
        """
        
        nav_html = self._generate_nav_html(nav)
        return template.format(
            title=title,
            content=content,
            nav_html=nav_html
        )
    
    def _generate_nav_html(self, nav):
        """Generate HTML for collapsible navigation."""
        html = ['<ul class="nav-list">']
        
        for section in nav:
            html.append(f'<li class="nav-section">')
            html.append(f'<div class="nav-section-header">{section["name"]}</div>')
            html.append('<ul class="nav-items">')
            
            for item in section['items']:
                html.append(
                    f'<li><a href="/{item["path"]}">{item["title"]}</a></li>'
                )
            
            html.append('</ul></li>')
        
        html.append('</ul>')
        return '\n'.join(html)
    
    def _copy_assets(self):
        """Copy CSS and JS assets to the docs directory."""
        assets_dir = self.docs_dir / 'assets'
        assets_dir.mkdir(exist_ok=True)
        
        # Create CSS
        css = """
        body {
            display: flex;
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }
        
        .sidebar {
            width: 250px;
            height: 100vh;
            background: #f5f5f5;
            padding: 20px;
            overflow-y: auto;
            position: fixed;
        }
        
        .content {
            margin-left: 290px;
            padding: 20px;
            max-width: 800px;
        }
        
        .nav-list {
            list-style: none;
            padding: 0;
        }
        
        .nav-section {
            margin-bottom: 15px;
        }
        
        .nav-section-header {
            font-weight: bold;
            cursor: pointer;
            padding: 5px;
            background: #e0e0e0;
            border-radius: 4px;
        }
        
        .nav-items {
            list-style: none;
            padding-left: 15px;
            display: none;
        }
        
        .nav-items.active {
            display: block;
        }
        
        .nav-items a {
            color: #333;
            text-decoration: none;
            display: block;
            padding: 5px;
        }
        
        .nav-items a:hover {
            background: #e0e0e0;
            border-radius: 4px;
        }
        
        /* Enhanced nested list styling */
        .content ul,
        .content ol {
            padding-left: 2em;
            margin-bottom: 1em;
        }
        
        .content ul ul,
        .content ol ol,
        .content ul ol,
        .content ol ul {
            margin-top: 0.5em;
            margin-bottom: 0.5em;
        }
        
        .content li {
            margin-bottom: 0.5em;
        }
        
        .content ul > li {
            list-style-type: disc;
        }
        
        .content ul > li > ul > li {
            list-style-type: circle;
        }
        
        .content ul > li > ul > li > ul > li {
            list-style-type: square;
        }
        
        .pdf-container {
            width: 100%;
            height: 100%;
        }
        """
        
        (assets_dir / 'style.css').write_text(css)
        
        # Create JavaScript
        js = """
        document.addEventListener('DOMContentLoaded', function() {
            const headers = document.querySelectorAll('.nav-section-header');
            
            headers.forEach(header => {
                header.addEventListener('click', () => {
                    const items = header.nextElementSibling;
                    items.classList.toggle('active');
                });
            });
        });
        """
        
        (assets_dir / 'script.js').write_text(js)
    
    def build(self):
        """Build the complete website."""
        # Generate navigation structure
        nav = self.generate_navigation()
        
        # Create assets
        self._copy_assets()
        
        # Process syllabus.md from root directory
        syllabus_path = self.root_dir / 'syllabus.md'
        if syllabus_path.exists():
            content = syllabus_path.read_text(encoding='utf-8')
            html_content = self._process_markdown(content)
            index_path = self.docs_dir / 'index.html'
            page_html = self._create_page(
                html_content,
                'Home',
                nav
            )
            index_path.write_text(page_html)
        else:
            print("Warning: syllabus.md not found in root directory")
        
        # Process all content from other directories
        for dir_name in self.content_dirs:
            dir_path = self.root_dir / dir_name if dir_name else self.root_dir
            if not dir_path.exists():
                continue
            
            for file_path in dir_path.glob('**/*'):
                if file_path.suffix.lower() not in ['.md', '.pdf']:
                    continue
                    
                # Create relative output path
                rel_path = file_path.relative_to(self.root_dir)
                out_path = self.docs_dir / rel_path
                out_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Process content based on type
                if file_path.suffix.lower() == '.md':
                    content = file_path.read_text(encoding='utf-8')
                    html_content = self._process_markdown(content)
                    page_html = self._create_page(
                        html_content,
                        self._get_title(file_path),
                        nav
                    )
                    out_path = out_path.with_suffix('.html')
                    out_path.write_text(page_html)
                else:  # PDF
                    # Copy PDF file
                    shutil.copy2(file_path, out_path)
                    # Create viewer page
                    viewer_content = self._process_pdf(rel_path)
                    page_html = self._create_page(
                        viewer_content,
                        self._get_title(file_path),
                        nav
                    )
                    viewer_path = out_path.with_suffix('.html')
                    viewer_path.write_text(page_html)

if __name__ == '__main__':
    generator = CourseWebsiteGenerator('.')
    generator.build()