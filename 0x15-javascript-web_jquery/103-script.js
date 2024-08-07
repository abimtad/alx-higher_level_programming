$(document).ready(function() {
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    });
  }

  // Event listener for button click
  $('#btn_translate').click(fetchTranslation);

  // Event listener for Enter key press on the input field
  $('#language_code').keypress(function(event) {
    if (event.which == 13) { // 13 is the keycode for Enter key
      fetchTranslation();
    }
  });
});
