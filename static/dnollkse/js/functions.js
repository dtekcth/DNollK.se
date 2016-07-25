function navbarClick() {
  $('.primary ul').slideToggle("slow");
}

function toggleSidebar() {
  if($('#content').is('.pushed')) {
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
