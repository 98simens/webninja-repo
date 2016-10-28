function tabClick(elem){
    var elements = document.getElementById("tab_content").getElementsByTagName("li");
    var tabs = document.getElementById("tabs").getElementsByTagName("li");
    for(var index = 0; index < tabs.length; index++){
        tabs[index].className = "";
    }
    elem.parentElement.className = "active";
    for(var i = 0; i < elements.length; i++){
        if(elem.getAttribute("data-target") === elements[i].id){
            elements[i].className = "active";
        }
        else{
            elements[i].className = "";
        }
    }
}

/* - Header Parallax - */
$(document).on("scroll", function() {
    $("header").css("background-position-y", $(document).scrollTop()/2 + "px");
});
$(document).on("scroll", function() {
    $("#Header").css("background-position-y", (document.getElementById("intro").offsetTop - $(document).scrollTop())/4 + "px");
});

$(document).on("scroll", function() {
    $("#spacing").css("background-position-y", (document.getElementById("spacing").offsetTop - $(document).scrollTop() - 1200)/4 + "px");
});

/* - Fixed Navbar jQuery - */
$(document).on("scroll", function() {
	if ($(window).scrollTop() > 512) {
		if($(".main-nav").className !== "main-nav fixed-nav") {
        $(".main-nav").addClass("fixed-nav");
        $("#offers").css("margin-top", "59px");
    }
	}
	else{
        $(".main-nav").removeClass("fixed-nav");
        $("#offers").css("margin-top", "0px");
    }
});

/* - copyright button (BETA) - */
$("footer").click(function() {
    $("#info-div").slideToggle();
    $(document).scrollTop($(document).height());
});

function scrollToDest(elem) {
	/*var destination = $("#" + elem).offset().top;
	$("body, html").animate("scrollTop: destination");*/
}