function tabClick(elem){
    var elements = document.getElementById("tab_content").getElementsByTagName("li");
    var tabs = document.getElementById("tabs").getElementsByTagName("li");
    for(var index = 0; index < tabs.length; index++){
        tabs[index].className = "";
    }
    elem.parentElement.className = "active";
    for(var i = 0; i < elements.length; i++){
        console.log(elements[i].id);
        if(elem.getAttribute("data-target") === elements[i].id){
            elements[i].className = "active";
        }
        else{
            elements[i].className = "";
        }
    }
}

