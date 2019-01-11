window.onload = function divmodify() {
    var box_itemCon = document.getElementsByClassName("box_itemCon");
    var edit = document.getElementsByClassName("edit");
    var uidedit = document.getElementById("uidedit");
    if (uidedit.innerText == "null") {
        for (var i = 0; i < box_itemCon.length; i++) {
            box_itemCon[i].style.display = "block"
        }
    } else {
        for (var j = 0; j < edit.length; j++) {
            edit[j].style.display = "block"
        }
    }
}