/**
 * Created by carej on 22/11/2017.
 */

function myGet() {

    $.getJSON('http://localhost:8000/api-token-auth/', function(data) {
        console.log(data);
        $.each(data, function (index, element) {
            $('body').append($('<div>', {
                text: element.first_name
            }));
        });
    }
}