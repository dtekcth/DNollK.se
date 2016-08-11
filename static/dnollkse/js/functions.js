function toggleSidebar() {
  if ($('#content').is('.pushed')) {
    $('#content').show();
  } else {
    setTimeout(function() {
      $('#content').hide();
    }, 700);
  }
  $('#sidebar').toggleClass("visible");
  // This is needed since otherwise we will miss out on the transition because we just showed the element.
  setTimeout(function() {
    $('#content').toggleClass("pushed");
  }, 0);
}

$( document ).ready(function() {

  // Calculate the height of the mobile navigation menu.
  var h = $('.primary > ul').height();

  /*
   * If viewport width is less than 550 pixels,
   * we are in mobile view and we would like to hide
   * the navbar.
   */
  if (document.documentElement.clientWidth < 550) {
    $('.primary > ul').get(0).style.height = "0rem"
  };

  /*
   * Click handler for #nav-btn.
   * Toggles the mobile navigation menu by changing the height.
   * Thanks to changing from and to a fixed value we can use CSS
   * transitions.
   */
  $('#nav-btn').click(function() {
    if ($('.primary > ul').get(0).style.height == "0rem") {
      setTimeout(function() {
        $('.primary > ul').get(0).style.height = h + "px";
      }, 0);
    } else {
      setTimeout(function() {
        $('.primary > ul').get(0).style.height = "0rem";
      }, 0);
    }
  });
});
