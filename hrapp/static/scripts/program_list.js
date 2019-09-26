function showPastPrograms() {
    let element = document.getElementById("hidden");
    let button = document.getElementById("reveal_past")
    // element.classList.toggle]("visible");
    element.setAttribute("class", "visible")
    element.removeAttribute("id")
    button.setAttribute("disabled", null)

  }