/**
 * Created by carej on 10/12/2017.
 */

function updateMemberInfo() {
    $.ajaxSetup({
        headers : {
            'Authorization' : 'Token ' + getCookie('token'),
        }
    });
    $.getJSON('http://localhost:8000/current-user/', function(data) {
        console.log();
        $('#member-id').text("Id: " + data.id);
        $('#member-lastname').text(data.last_name);
        $('#member-firstname').text(data.first_name);
        $('#member-surname').html(data.username);
        console.log(data, "success");
    })
    .fail(function( data, status )  {
        window.location.replace("http://localhost:63342/EUPeopleProject/client/html/login.html");
        console.log(status);
    });
}
