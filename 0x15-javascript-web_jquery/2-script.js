//$('DIV#red_header').click(function () {
   // $('header').css('color', '#FF0000');
//});

// jQuery script
$(document).ready(function() {

    // select the div by ID
    const redHeaderDiv = $('DIV#red_header');

    // add an event handler
    redHeaderDiv.click(function() {
        // find the header
        const headerElement = $('header');

        // check if header was found
        if (headerElement) {
            // use css to set color
            headerElement.css('color', '#FF0000');
        } else {
            console.error('Header elemnet not found');
        }
    });
});
