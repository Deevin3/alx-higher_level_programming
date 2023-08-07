$('document').ready(function () {
$.fetch("https://fourtonfish.com/hellosalut/?lang=fr", function (data){
    $('DIV#hello').text(data.hello);
 });
})