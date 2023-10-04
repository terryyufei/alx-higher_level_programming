// GET request
//$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data)=>{
//$('DIV#character').text(data.name);
//});

$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    datatype: 'json',
    success: function (data) {
        // extract character from the fetched data
        const characterName = data.name;

        //display the xcter name in the div
        $('DIV#character').text(characterName);
    }
});
