function navbarClick() {
  $('.primary ul').slideToggle("slow");
}

function toggleSidebar() {
  $('#sidebar').toggleClass("visible");
  $('#content').toggleClass("pushed");
}