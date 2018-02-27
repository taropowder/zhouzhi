window.onload=function () {
    /*啾一下*/
    var oInput=document.getElementById("jiu");
    var oMy=document.getElementById("myself");

   /* var oImg=document.getElementById("img1");
    var oKaiguan=document.getElementById("guan");
    var oKaiguan1=document.getElementById("guan1");
    var oTan=document.getElementById("dlt");
    oKuang=document.getElementById("kuang");

    var oA1=document.getElementById("oA1");
    var oA2=document.getElementById("oA2");
    var oHui=document.getElementById("hui");
    var oDlyhm=document.getElementById("yhm");
    var oDlymm=document.getElementById("mm");
    var oDl=document.getElementById("dl");
    var oZc=document.getElementById("zc");*/
    var oWd=document.getElementById("san");
/*
/!*弹出登陆框*!/
    oA1.onclick=function ()
    {
        oHui.style.display="block";
        oTan.style.display="block";
    }
    oKaiguan.onclick=function () {
        oHui.style.display="none";
        oTan.style.display="none";
    }
/!*注册弹出*!/
    oA2.onclick=function ()
    {
        oHui.style.display="block";
        oKuang.style.display="block";
    }
    oKaiguan1.onclick=function () {
        oHui.style.display="none";
        oKuang.style.display="none";
    }
    oDlyhm.onfocus=function ()
    {
        this.setAttribute("class","dlb1");
        if(this.value=="请输入用户名或邮箱")
        {
            this.value='';
        }
    }
    oDlyhm.onblur=function ()
    {
        this.setAttribute("class","dlb0");
        if(this.value=="")
        {
            this.value="请输入用户名或邮箱";
        }
    }

    oDlymm.onfocus=function ()
    {
        this.setAttribute("class","dlb1");
        if(this.placeholder=="请输入密码")
        {
            this.placeholder='';
        }
    }
    oDlymm.onblur=function ()
    {
        this.setAttribute("class","dlb0");
        if(this.placeholder=="")
        {
            this.placeholder="请输入密码";
        }
    }
*/

/*动态value*/
    $("#jiu").focus(function () {
        if(this.value=="啾一下就知道")
        {
           this.value='';
        }
    });
    oInput.onblur=function ()
    {
        if(this.value=="")
        {
            this.value="啾一下就知道";
        }
    }
    $("#bjiu").click(function () {
        if(oInput.value==""||oInput.value=="啾一下就知道")
        {
            return false;
        }
    })
}