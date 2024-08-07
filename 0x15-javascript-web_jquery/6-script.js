// updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header
// using the JQuery API

$('div#update_header').click(function () {
    $('header').text('New Header!!!');
});