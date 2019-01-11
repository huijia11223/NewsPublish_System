window.onload = function () {
    var container = document.getElementById("container");
    var list = document.getElementById("list");
    var buttons = document.getElementById("buttons").getElementsByTagName('span');
    var prev = document.getElementById("prev");
    var next = document.getElementById("next");
    var index = 1;
    var timer;

    function changeDiv() {
        var username = document.getElementById("username");
        var login = document.getElementsByClassName("login");
        var userOnline = document.getElementsByClassName("userOnline");
        if (username.innerText == "null") {
            for (var i = 0; i < login.length; i++) {
                login[i].style.display = "block"
            }
        } else {
            for (var j = 0; j < userOnline.length; j++) {
                userOnline[j].style.display = "block"
            }
        }
    }

    function animate(offset) {
        var newLeft = parseInt(list.style.left) + offset;
        list.style.left = newLeft + "px";

        if (newLeft < -3840) {
            list.style.left = 0 + 'px';
        } else if (newLeft > 0) {
            list.style.left = -3840 + 'px';
        }
    }

    function play() {
        timer = setInterval(function () {
            next.onclick();
        }, 2000)
    }

    function stop() {
        clearInterval(timer);
    }

    function buttonsShow() {
        for (var i = 0; i < buttons.length; i++) {
            if (buttons[i].className == 'on') {
                buttons[i].className = '';
            }
        }

        buttons[index - 1].className = 'on';

    }

    prev.onclick = function () {
        index -= 1;
        if (index < 1) {
            index = 5
        }
        buttonsShow();
        animate(960);
    };

    next.onclick = function () {
        index += 1;
        if (index > 5) {
            index = 1 
        }
        animate(-960);
        buttonsShow();
    };

    for (var i = 0; i < buttons.length; i++) {
        (function (i) {
            buttons[i].onclick = function () {
                var clickIndex = parseInt(this.getAttribute('index'));
                var offset = 960 * (index - clickIndex);
                animate(offset);
                index = clickIndex;
                buttonsShow()
            }
        })(i)
    }
    container.onmouseover = stop;
    container.onmouseout = play;
    changeDiv();    
    play();
}