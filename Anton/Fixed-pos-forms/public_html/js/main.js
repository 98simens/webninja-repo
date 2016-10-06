$(document).ready(function() {
    $("#forms-button").click(function() {
        showForm();
    });
    $("#forms-quit").click(function() {
        hideForm();
    });
});

function showForm() {
    $("#forms-button").css("height", "100%").css("bottom", "0").css("right", "0").css("width", "350px").css("border-radius", "0px");
    $("#forms-button form").show();
    $("#forms-quit").fadeIn();
}

function hideForm() {
    $("#forms-button").css("height", "50px").css("bottom", "10px").css("right", "10px").css("width", "50px");
    $("#forms-button form").hide();
    $("#forms-quit").fadeOut();
}