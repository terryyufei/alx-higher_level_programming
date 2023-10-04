$(document).ready(function () {
    // add a click event to the translate button
    $('#btn_translate').click(function () {

        //get language code entered by the user
        const languageCode = $('#language_code').val();

        // use AJAX to fetch data
        $.ajax({
            url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
            method: 'GET',
            dataType: 'json',
            success: function (data) {
                // extract translaton of hello from fetched data
                $('#hello').text(translation);
            },
            error: function () {
            // Handle any errors here
            $('#hello').text('Translation not found.');
            }
        });
    });
});
