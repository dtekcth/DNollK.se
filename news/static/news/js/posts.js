function toggleExpanded(element) {
  /*var post = document.getElementById(id);*/
  var post = element.parentNode.parentNode;

  if ( !post.classList.contains("post")) {
    /* toggleExpanded is not called from a second level grandchild of a post */
    return false;
  }

  $('#' + post.id + ' .post-content').slideToggle("slow");
  $('#' + post.id).toggleClass("expanded");
}


window.onload = function() {
  /**
   * Adds class "expanded" to first post and hides all other posts' content.
   */
  (function () {
    var posts = document.getElementsByClassName("post");
    
    var length = posts.length;
    
    /* Return if no posts */
    if (length == 0) { return; }
    
    /* Make first post expanded. */
    posts.item(0).classList.add("expanded");
    
    /* Hide post-content on rest of posts. */
    if (length > 1) {
      for (var i = 1; i < length; i++) {
        posts.item(i).children.item(2).style.display = "none";
      }
    }
  })();
  
  /**
   * Removes class "hidden" from every .expandBtn element to reveal them when
   * JavaScript is enabled.
   */
  (function() {
    var expandBtns = document.getElementsByClassName("expandBtn");
    var length = expandBtns.length;
    for (var i = 0; i < length; i++) {
      expandBtns.item(i).classList.remove("hidden");
    }
  })();
};
