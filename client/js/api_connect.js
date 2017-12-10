/**
 * Created by carej on 17/11/2017.
 */

function loginAPI() {
    $.post('http://localhost:8000/api-token-auth/', {
        username: $( "#username" ).val(),
        password : $( "#password" ).val()}
        )
        .success(function(data) {
            console.log("success");
            setCookie('token', data.token, 365);
            setCookie('user-id', data.id, 365);
            console.log(data.token);
            $.ajaxSetup({
              headers : {
                'Authorization' : 'Token ' + data.token,
              }
            });
            $.getJSON('http://localhost:8000/current-user/', function(data) {
                console.log(data);
                data.is_staff = false;
                console.log(data.is_staff);
                if (data.is_staff === false) {
                    console.log("is not staff");
                    $( "#login-form" ).attr('action', 'Member_home.html');

                } else {
                    console.log("is_staff");
                    $( "#login-form" ).attr('action', 'Staff_home.html');
                }
            });
            $( "#login-form" ).submit();
            return true;
        })
        .fail(function( data, status )  {
            $( "#password" ).css({'border' : 'solid #f77979 1px'}).val('');
            return false;
        });
    return false;
}