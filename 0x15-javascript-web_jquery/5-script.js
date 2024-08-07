// adds a <li> element to a list when the user clicks on the tag DIV#add_item
// using the JQuery API

$('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
});