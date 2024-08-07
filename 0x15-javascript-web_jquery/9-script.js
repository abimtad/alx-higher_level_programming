// fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello
// Using the JQuery API

let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.get(url, function (data) {
    $('div#hello').text(data.hello);
});