
window.addEventListener("resize", function () {
    if (window.matchMedia("(max-width: 800px)").matches) {
        $(".navbar").addClass("navbar-light bg-light")
    } else {
        $(".navbar").removeClass("navbar-dark bg-light")
    }
});
