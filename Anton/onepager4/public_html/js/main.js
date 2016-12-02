$(document).ready(function() {
    $(".imageSlider").unslider({
        autoplay: true,
        nav: false,
        arrows: false,
        dots: false,
        delay: 5000,
        speed: 500,
        infinite: true
    });
});

function navExpand() {
    $(".navboxhidden").slideToggle();
}

function tabChange(elem) {
    var tab = elem.getAttribute("tab");
    if(tab === "1") {
        $(".tabContentOne").hide();
        $(".tabContentTwo").show();
        $(".tabButton[tab='1']").addClass("active");
        $(".tabButton[tab='2']").removeClass("active");
    } else if(tab === "2") {
        $(".tabContentTwo").hide();
        $(".tabContentOne").show();
        $(".tabButton[tab='2']").addClass("active");
        $(".tabButton[tab='1']").removeClass("active");
    }
}

function initMap() {
    var uluru = {lat: 65.783028, lng: 21.729181};
    var map = new google.maps.Map(document.getElementById("map"), {
        scrollwheel: false,
        zoom: 14,
        center: uluru,
        mapTypeId: "hybrid",
        disableDefaultUI: true
    });
    var market = new google.maps.Marker({
        position: uluru,
        map: map
    });
}

function scrollDestination(dest) {
    $("html, body").animate({
        scrollTop: $("#" + dest).offset().top - 30
    }, 1000);
}