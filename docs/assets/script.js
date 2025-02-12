
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
