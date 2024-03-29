$(document).ready(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    
    $('#email_register').change(function () {
        console.log("validate triggered");
        form_email = this.value;
        $.ajax({
            type: 'POST',
            url: 'validate_email',
            data: {
                email: form_email,
                
            },
            headers: {
                "X-CSRFToken" : csrftoken
            },
            success: function (json){
                console.log(json)
                $("#emailWarning").html(json.result)
            }
        })
    })
})