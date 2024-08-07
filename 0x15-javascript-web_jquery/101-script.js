$(document).ready(function() {
  // Add a new list item
  $('#add_item').click(function() {
    $('.my_list').append('<li>Item</li>');
  });

  // Remove the last list item
  $('#remove_item').click(function() {
    $('.my_list li:last').remove();
  });

  // Clear all list items
  $('#clear_list').click(function() {
    $('.my_list').empty();
  });
});
