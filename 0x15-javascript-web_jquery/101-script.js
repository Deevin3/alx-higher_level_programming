$('document').ready(function () {
    $('DIV#add_item').click(function () {
        $('UL.my_list').append('<li>Item</li>');
    })
    $('DIV#add_item').click(function () {
        $('UL.my_list').remove('<li>Item</li>');
    })
    $('DIV#add_item').click(function (){
        $('UL.my_list').empty('<li>Item</li>');
    });
});