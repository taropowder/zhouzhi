/*用户名验证*/
function checkName()
{
    var oName=document.getElementById("name");
    var oSpan1=document.getElementById("span1");
    if (oName.value=="")
    {
        oSpan1.innerHTML="请输入用户名";
        return false;
    }
    else
    {
        oSpan1.innerHTML="";
        return true;
    }
}
function focusName() {
    var oSpan1=document.getElementById("span1");
    oSpan1.innerHTML="";
}
/*密码验证*/
function checkPass()
{
    var oPass=document.getElementById("pass");
    var oSpan2=document.getElementById("span2");
    if (oPass.value=="")
    {
        oSpan2.innerHTML="请输入密码";
        return false;
    }
    else
    {
        oSpan2.innerHTML="";
        return true;
    }
}
function focusPass() {
    var oSpan2=document.getElementById("span2");
    oSpan2.innerHTML="";
}
/*提交验证*/
function check() {
    if (checkName()==false||checkPass()==false)
        return false;
}

