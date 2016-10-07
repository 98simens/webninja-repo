/* - Header Parallax - */
$(document).on("scroll", function() {
    $("header").css("background-position-y", $(document).scrollTop()/2 + "px");
});


/* - Fixed Navbar jQuery - */
$(document).on("scroll", function() {
    if ($(window).scrollTop() > 512) {
        $(".main-nav").addClass("fixed-nav");
        $("article").css("margin-top", "160px");
    } else {
        $(".main-nav").removeClass("fixed-nav");
        $("article").css("margin-top", "100px");
    }
});

/* - copyright button (BETA) - */
$(document).click(function() {
    $("#info-div").slideToggle();
    $(document).scrollTop($(document).height());
});