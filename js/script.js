function toggle(button) {
    var parent_container = button.parentElement;
    var iframe = parent_container.getElementsByTagName("iframe")[0]
    var img = parent_container.getElementsByTagName("img")[0]
    var p = parent_container.getElementsByTagName("p")[0]
    
    img.style.display = "none";
    p.style.display = "none";
    iframe.style.display = "block";
}
