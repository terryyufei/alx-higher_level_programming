// jquery script
$(document).ready(function () {
  // use jquery selector
  const element = $('header');

  // check if header was found
  if (element) {
    // use css to set color
    element.css('color', '#FF0000');
  } else {
    console.error('Header element not found');
  }
});
