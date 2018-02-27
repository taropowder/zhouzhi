window.onload=function ()
{

    var oInput=document.getElementById("jiu");
    var oImg=document.getElementById("img1");
    var oKaiguan=document.getElementById("guan");
    var oTan=document.getElementById("dlt");
    var oA1=document.getElementById("oA1");
    var oHui=document.getElementById("hui");
    var oDlyhm=document.getElementById("yhm");
    var oDlymm=document.getElementById("mm");
    oInput.onfocus=function ()
    {
        if(oInput.value=="啾一下就知道")
        {
            oInput.value='';
         }
    }
    oInput.onblur=function ()
    {
        if(oInput.value=="")
        {
            oInput.value="啾一下就知道";
        }
    }


    /*弹出登陆框*/
    oA1.onclick=function ()
    {
        oHui.style.display="block";
        oTan.style.display="block";
    }
    oKaiguan.onclick=function () {
        oHui.style.display="none";
        oTan.style.display="none";
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


}
