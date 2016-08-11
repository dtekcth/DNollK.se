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

  // We like haskell! :D
  var h = $('.primary > ul').height();

  $('.primary > ul').get(0).style.height = "0rem";

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
