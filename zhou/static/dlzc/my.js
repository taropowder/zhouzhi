/*  邮箱验证*/
function focusEmail()
{
    var oEmail=document.getElementById("email");
    var oSpan=document.getElementById("span1");
    oSpan.innerHTML="";
}
function checkEmail ()
{
    var oEmail=document.getElementById("email");
    var oSpan=document.getElementById("span1");
    var oBd=document.getElementById("bd");
    if(oEmail.value=="")
    {
        oSpan.innerHTML="邮箱可用来找回密码请输入";
        return false;
    }
    else if(oEmail.value.indexOf("@")==-1)
    {
        oSpan.innerHTML="请输入正确的邮箱";
        return false;
    }
    else
    {
        oSpan.innerHTML="";
        return true;
    }
};
/*验证用户名*/
function checkName()
{
    var oSan2=document.getElementById("span2");
    var oName=document.getElementById("name");
    if (oName.value=="")
    {
        oSan2.innerHTML="请输入用户名";
        return false;
    }
    else if (oName.value.length>"20")
    {
        oSan2.innerHTML="请输入小于20个字的用户名";
        return false;
    }
    else
    {
        oSan2.innerHTML="";
        return true;
    }
}
function  focusName()
{
    var oSan2=document.getElementById("span2");
    var oName=document.getElementById("name");
    oName.innerHTML="";
}
/*密码验证*/
function checkPass()
{
    var oSan3=document.getElementById("span3");
    var oPass=document.getElementById("pass");
    if(oPass.value=="")
    {
        oSan3.innerHTML="请输入密码";
        return false;
    }
    else
    {
        oSan3.innerHTML="";
        return true;
    }
}
function focusPass()
{
    var oSan3=document.getElementById("span3");
    oSan3.innerHTML="";
}
/*提交验证*/
function check() {
    if(checkEmail()==false||checkName()==false||checkPass==false)
        return false;
    else
        return true;
}

