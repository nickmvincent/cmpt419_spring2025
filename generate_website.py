import os
import shutil
import markdown
import yaml
from pathlib import Path

class CourseWebsiteGenerator:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        # All output will be in docs/
        self.docs_dir = self.root_dir / 'docs'
        self.docs_dir.mkdir(exist_ok=True)
        
        # Content directories in the order you want them to appear
        self.content_dirs = [
            'readings',
            'assignments',
            'slides',
            'misc',
            'slides_pdfs'
        ]
    
    def generate_navigation(self, nav):
        """
        Build HTML for the sidebar navigation.
        Each navigation item is a hash link (e.g. href="#readings-lecture1")
        that points to a section in the single-page app.
        """
        html = ['<ul class="nav-list">']
        for section in nav:
            html.append(f'<li class="nav-section">')
            html.append(f'<div class="nav-section-header">{section["name"]}</div>')
            html.append('<ul class="nav-items">')
            for item in section['items']:
                html.append(f'<li><a href="#{item["id"]}">{item["title"]}</a></li>')
            html.append('</ul></li>')
        html.append('</ul>')
        return '\n'.join(html)
    
    def _get_title(self, file_path):
        """Extract title from Markdown YAML front matter (if present) or use a prettified filename."""
        if file_path.suffix.lower() == '.md':
            content = file_path.read_text(encoding='utf-8')
            if content.startswith('---'):
                try:
                    front_matter = content.split('---')[1]
                    metadata = yaml.safe_load(front_matter)
                    if metadata and 'title' in metadata:
                        return metadata['title']
                except Exception as e:
                    print(f"Error parsing YAML in {file_path}: {e}")
        # Fallback: prettify the file stem.
        return file_path.stem.replace('_', ' ').title()
    
    def _process_markdown(self, content):
        """Convert Markdown text to HTML using several useful extensions."""
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
        # (Optional) Normalize list indentation.
        lines = content.split('\n')
        normalized_lines = []
        in_list = False
        for line in lines:
            stripped = line.lstrip()
            if stripped.startswith(('- ', '* ', '+ ')):
                indent = len(line) - len(stripped)
                level = indent // 2  # assuming 2 spaces per level
                normalized_lines.append(('    ' * level) + stripped)
                in_list = True
            else:
                if in_list and not stripped:
                    normalized_lines.append('')
                else:
                    normalized_lines.append(line)
                    in_list = False
        normalized_content = '\n'.join(normalized_lines)
        md = markdown.Markdown(extensions=extensions)
        return md.convert(normalized_content)
    
    def _process_pdf(self, pdf_rel_path):
        """
        Instead of embedding the PDF, generate an external link that opens the PDF in a new tab.
        pdf_rel_path is the path of the PDF relative to the site root.
        """
        pdf_url = str(pdf_rel_path).replace(os.sep, '/')
        # Use the file's stem as a label.
        label = pdf_rel_path.stem.replace('_', ' ').title()
        return f'<p><a href="{pdf_url}" target="_blank">View PDF: {label}</a></p>'
    
    def _create_single_page(self, sections, nav):
        """
        Assemble the final single-page HTML.
        Each section is wrapped in a <section> tag with a unique id.
        The sidebar uses hash links to jump to the corresponding section.
        """
        nav_html = self.generate_navigation(nav)
        sections_html = []
        for section in sections:
            # Show the home section by default; other sections are hidden until activated.
            active_class = 'active' if section['id'] == 'home' else ''
            sections_html.append(f'<section id="{section["id"]}" class="page-section {active_class}">')
            sections_html.append(f'<h1>{section["title"]}</h1>')
            sections_html.append(section["content"])
            sections_html.append('</section>')
        sections_html = '\n'.join(sections_html)
        
        template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Course Website</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <div class="sidebar">
    <nav>{nav_html}</nav>
  </div>
  <div class="content">
    {sections_html}
  </div>
  <script src="assets/script.js"></script>
</body>
</html>"""
        return template
    
    def _copy_assets(self):
        """Create the assets folder and write CSS/JS files."""
        assets_dir = self.docs_dir / 'assets'
        assets_dir.mkdir(exist_ok=True)
        
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
/* Nested list styling */
.content ul,
.content ol {
    padding-left: 2em;
    margin-bottom: 1em;
}
.content li {
    margin-bottom: 0.5em;
}
/* Single-page sections */
.page-section {
    display: none;
}
.page-section.active {
    display: block;
}
"""
        (assets_dir / 'style.css').write_text(css)
        
        js = """
document.addEventListener('DOMContentLoaded', function() {
    // Show the section based on the URL hash.
    function showSection(id) {
        document.querySelectorAll('.page-section').forEach(function(section) {
            section.classList.remove('active');
        });
        var target = document.getElementById(id);
        if (target) {
            target.classList.add('active');
        }
    }
    
    window.addEventListener('hashchange', function() {
        var id = window.location.hash.substring(1);
        showSection(id);
    });
    
    // On initial load, check hash (default to 'home')
    var initial = window.location.hash ? window.location.hash.substring(1) : 'home';
    showSection(initial);
    
    // Toggle navigation sections.
    document.querySelectorAll('.nav-section-header').forEach(function(header) {
        header.addEventListener('click', function() {
            var items = header.nextElementSibling;
            items.classList.toggle('active');
        });
    });
});
"""
        (assets_dir / 'script.js').write_text(js)
    
    def build(self):
        """
        Build the single-page website:
         - Process the syllabus (home page).
         - Process content from the specified directories.
         - For Markdown files, convert to HTML.
         - For PDF files, copy them (if needed) and create an external link.
         - Assemble a single index.html with a sidebar navigation.
        """
        sections = []
        nav = []
        
        # Process the syllabus as the home section.
        syllabus_path = self.root_dir / 'syllabus.md'
        if syllabus_path.exists():
            content = self._process_markdown(syllabus_path.read_text(encoding='utf-8'))
            sections.append({
                'id': 'home',
                'title': 'Home',
                'content': content
            })
        else:
            print("Warning: syllabus.md not found in root directory")
        
        # Add Home to the navigation.
        nav.append({
            'name': 'Home',
            'items': [{'title': 'Home', 'id': 'home'}]
        })
        
        # Process each content directory.
        for dir_name in self.content_dirs:
            dir_path = self.root_dir / dir_name
            if not dir_path.exists():
                continue
            nav_section = {'name': dir_name, 'items': []}
            for file_path in sorted(dir_path.glob('**/*')):
                if file_path.suffix.lower() not in ['.md', '.pdf']:
                    continue
                rel_path = file_path.relative_to(self.root_dir)
                
                # For PDF files, copy them (creating parent folders on demand)
                if file_path.suffix.lower() == '.pdf':
                    out_path = self.docs_dir / rel_path
                    out_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file_path, out_path)
                    content = self._process_pdf(rel_path)
                else:
                    content = self._process_markdown(file_path.read_text(encoding='utf-8'))
                
                # Create a unique section id by replacing slashes with dashes.
                section_id = rel_path.with_suffix('').as_posix().replace('/', '-')
                title = self._get_title(file_path)
                sections.append({
                    'id': section_id,
                    'title': title,
                    'content': content
                })
                nav_section['items'].append({
                    'title': title,
                    'id': section_id
                })
            if nav_section['items']:
                nav.append(nav_section)
        
        # Create assets and the single index.html page.
        self._copy_assets()
        page_html = self._create_single_page(sections, nav)
        (self.docs_dir / 'index.html').write_text(page_html)
        print(f"Built single-page site at: {self.docs_dir / 'index.html'}")

if __name__ == '__main__':
    generator = CourseWebsiteGenerator('.')
    generator.build()
