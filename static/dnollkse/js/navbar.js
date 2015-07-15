function navbarClick() {
  var navUl = document.getElementsByClassName("primary").item(0).children[1]

  if (navUl.classList.contains("expanded")) {
    navUl.classList.remove("expanded");
  } else {
    navUl.classList.add("expanded");
  }
}