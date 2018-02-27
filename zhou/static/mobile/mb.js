window.onload=function () {
    var oSearch=document.getElementById("search");
    var oRc=document.getElementById("reci");
    var oWd=document.getElementById("wode");
    var oBut=oSearch.getElementsByTagName("button");
    var oBut1=oRc.getElementsByTagName("button");
    var oBut2=oWd.getElementsByTagName("button");
    var oDiv=oSearch.getElementsByTagName("div");
    var oDiv1=oRc.getElementsByTagName("div");
    var oDiv2=oWd.getElementsByTagName("div");
    var oSpan=oSearch.getElementsByTagName("span");
    var oSpan1=oRc.getElementsByTagName("span");
    var oSpan2=oWd.getElementsByTagName("span");
    var oGai=document.getElementById("two");
    var oD=oGai.getElementsByTagName("div");
    var oAg=document.getElementById("ta");
    var oAa=document.getElementById("te");
    var oYhm=document.getElementById("yhm");
    var oMm=document.getElementById("mm");
    var oJIu=document.getElementById("jiu");
        oDiv[1].setAttribute("class","");
         oDiv1[0].setAttribute("class","");
    oDiv2[0].setAttribute("class","");
        for(var i=0;i<oSpan.length;i++)
        {oSpan[i].setAttribute("class","");
            oSpan1[i].setAttribute("class","");
            oSpan2[i].setAttribute("class","");}
        oBut[0].setAttribute("class","");
    oBut1[0].setAttribute("class","");
    oBut2[0].setAttribute("class","");
        oBut[0].setAttribute("id","butjiu");
        oD[0].setAttribute("class","");
         oAg.setAttribute("class","");
          oAa.setAttribute("class","");

    oYhm.onfocus=function ()
    {
        if(this.placeholder=="请输入用户名或邮箱")
        {
            this.placeholder='';
        }
    }
    oYhm.onblur=function ()
    {
        if(this.placeholder=="")
        {
            this.placeholder="请输入用户名或邮箱";
        }
    }
    oMm.onfocus=function ()
    {
        if(this.placeholder=="请输入密码")
        {
            this.placeholder='';
        }
    }
    oMm.onblur=function ()
    {
        if(this.placeholder=="")
        {
            this.placeholder="请输入密码";
        }
    }
    oJIu.onfocus=function () {
        if(this.value=="啾一下就知道")
        {
            this.value="";
        }
    }
    oJIu.onblur=function ()
    {
        if(this.value=="")
        {
            this.value="啾一下就知道";
        }
    }



}