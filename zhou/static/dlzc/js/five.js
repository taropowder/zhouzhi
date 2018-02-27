function check1() {
    var oInp=document.getElementById("one");
    var oSpan=document.getElementById("span1");
    if (oInp.value=="")
    {
        oSpan.style.display="inline-block";
        return false;
    }
    else
        return true;
}
function check2() {
    var oInp=document.getElementById("three");
    var  oIn=document.getElementById("two");
    var oSpan=document.getElementById("span2");
    if(oInp.value!=oIn.value)
    {
        oSpan.style.display="inline-block";
        return false;
    }
    else
        return true;
}
function focus1() {
    var oSpan=document.getElementById("span1");
    oSpan.style.display="none";
}
function  focus2() {
    var oSpan=document.getElementById("span2");
    oSpan.style.display=="none";
}

function check() {
    if (check1()==false||check2()==false)
    {
        return false;
    }
    else
        return true;
}