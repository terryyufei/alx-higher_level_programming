//document.addEventListener('DOMContentLoaded', ()=>{
    //document.querySelector('header').style.color = '#FF0000';
//});


// Ensure the DOM is ready
document.addEventListener('DOMContentLoaded', function () {
    // Select the <header> element
    const headerElement = document.querySelector('header');

    // Check if the element was found
    if (headerElement) {
        // Set the text color to red
        headerElement.style.color = '#FF0000';
    } else {
        console.error('Header element not found.');
    }
});
