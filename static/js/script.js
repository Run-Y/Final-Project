function showSeaLevelPage() {
    // Hide the welcome text
    document.getElementById('welcome-text').style.display = 'none';
    document.getElementById('welcome-description').style.display = 'none';

    var mainContainer = document.querySelector('main');
    // Clear previous content
    mainContainer.innerHTML = '';

    // Create iframe and set the source to load the Flask route for sea_level
    var iframe = document.createElement('iframe');
    iframe.src = '/sea_level?' + new Date().getTime();  // Avoid caching
    mainContainer.appendChild(iframe);  // Add iframe to the main container
}

function showIceMassPage() {
    // Hide the welcome text
    document.getElementById('welcome-text').style.display = 'none';
    document.getElementById('welcome-description').style.display = 'none';

    var mainContainer = document.querySelector('main');
    // Clear previous content
    mainContainer.innerHTML = '';

    // Create iframe and set the source to load the Flask route for ice_mass
    var iframe = document.createElement('iframe');
    iframe.src = '/ice_mass?' + new Date().getTime();  // Avoid caching
    mainContainer.appendChild(iframe);  // Add iframe to the main container
}
