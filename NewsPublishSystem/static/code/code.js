var nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
];

var str="";
var verVal=drawCode(); //
function drawCode(str){
    var canvas=document.getElementById("verifyCanvas");
    
    var context=canvas.getContext("2d"); //获取画布上下文2d
    context.fillStyle="cornflowerblue"; //填充颜色
    context.fillRect(0,0,canvas.clientWidth,canvas.height);//清空画布
    context.fillStyle="white";//字体颜色
    context.font="25px Arial";//字体
    var rand =new Array();
    var x=new Array();
    var y=new Array();
    for (var i=0;i<4;i++){
        rand.push(rand[i]);
        rand[i]=nums[Math.floor(Math.random()*nums.length)];
        x[i]=i*20+10;
        y[i]=Math.random()*20+20;
        context.fillText(rand[i],x[i],y[i]);
    }
    str=rand.join('').toUpperCase();

    //3条随机线
    for (var i=0;i<3;i++){
        drawline(canvas,context);
    }

    //画30个随机点
    for (var i=0;i<30;i++){
        drawDot(canvas,context);

    }
    convertCanvasToImage(canvas);
    return str;
}

function drawline(canvas,context){
    context.moveTo(Math.floor(Math.random()*canvas.width),Math.floor(Math.random()*canvas.height));
    context.lineTo(Math.floor(Math.random()*canvas.width),Math.floor(Math.random()*canvas.height));
    context.lineWidth=0.5;
    context.strokeStyle='rgba(50,50,50,0.3)';
    context.stroke();
}
function drawDot(canvas,context){
    var px=Math.floor(Math.random()*canvas.width);
    var py=Math.floor(Math.random()*canvas.height);
    context.moveTo(px,py);
    context.lineTo(px+1,py+1);
    context.lineWidth=0.2;
    context.stroke();
}

function convertCanvasToImage(canvas){
    document.getElementById("verifyCanvas").style.display="none";
    var image=document.getElementById("code_img");
    image.src=canvas.toDataURL("image/png"); //png格式
    return image;
}
document.getElementById("code_img").onclick=function(){
    resetCode();
}
function resetCode(){
    $('#verifyCanvas').remove();
    $('#code_img').before('<canvas width="100px" height="100px" id="verifyCanvas"></canvas>');
    verVal=drawCode();
}

