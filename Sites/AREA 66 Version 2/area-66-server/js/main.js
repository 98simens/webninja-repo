var slider;
$(document).ready(function() {
    slider = $(".wn-imgslider div").unslider({
        infinite: true,
        arrows: false,
        nav: false
    });
})

function imgslider(val) {
    var val = val;
    if(val === "next") {
        slider.unslider("next");
    } else if(val === "prev") {
        slider.unslider("prev");
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
	
	market.addListener("click",function(){
		window.location = "https://www.google.se/maps/place/Area+66+Lasergame/@65.791844,21.7444968,14z/";
	});
}

function aboutmore(val) {
    var val = val;
    if(val === "show") {
        $("a#showmore").hide();
        $("span.wn-about-more").slideDown();
    } else if(val === "hide") {
        $("span.wn-about-more").slideUp();
        $("a#showmore").show();
    }
}

function scrollTo(dest) {
    var dest = dest;
    $("html, body").animate({
        scrollTop: $("#" + dest).offset().top - 50
    }, 1000);
}
