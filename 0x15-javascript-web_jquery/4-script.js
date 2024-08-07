// toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
// using the JQuery API

$('div#toggle_header').click(function () {
    $('header').ToggleClass('red');
});