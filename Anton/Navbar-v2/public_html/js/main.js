$(document).ready(function() {
    $("#offers-link, #intro-link, #contact-link").click(function(element) {
        var attribute = this.getAttribute("dest");
        scrollTo(attribute);
    });
    
    $("#backToTop").click(function() {
        backToTop();
    });
});

$(document).on("scroll", function() {
    var width = $("body").width();
    if(width >= 767) {
        if($(window).scrollTop() >= 188) {
            $("nav.main-nav").addClass("fixed");
            $("#intro").css("margin-top", "70px");
            $("#backToTop").fadeIn();
        } else {
            $("nav.main-nav").removeClass("fixed");
            $("#intro").css("margin-top", "0");
            $("#backToTop").fadeOut();
        }
    } else {
    }
});

function scrollTo(attribute) {
    var destination = $("#"+attribute).offset().top;
    $("body, html").animate({scrollTop: destination - 50}, 1000);
}

function backToTop() {
    $("body, html").animate({scrollTop: 0}, 1000);
}