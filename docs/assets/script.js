
        document.addEventListener('DOMContentLoaded', function() {
            const headers = document.querySelectorAll('.nav-section-header');
            
            headers.forEach(header => {
                header.addEventListener('click', () => {
                    const items = header.nextElementSibling;
                    items.classList.toggle('active');
                });
            });
        });
        