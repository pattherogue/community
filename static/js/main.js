document.addEventListener('DOMContentLoaded', function () {
    // Function to toggle navigation menu
    function toggleNav() {
        var nav = document.querySelector('nav');
        nav.classList.toggle('active');
    }

    // Event listener for hamburger menu icon click
    var menuIcon = document.getElementById('menu-icon');
    if (menuIcon) {
        menuIcon.addEventListener('click', function () {
            toggleNav();
        });
    }
});
