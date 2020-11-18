$(function() {
// csrf_tokenの取得に使う
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

for(let number =1;number<=1000;number ++){

    $('.news_'+number).click(function() {
        var csrf_token = getCookie("csrftoken");

    //$(document).on("click", "'.news_'+number", function() {
        $.ajax({
            type: 'POST',
            url: './news',
            data: {
                view_number: 1,
                news_number: number,  
            },
            contentType: "application/json",
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
            },

            });
            
            
    });

};
});