$(document).ready(function(){
    $("tr td img").mouseover(function(){
        $(this).css("opacity","1");
    }).mouseout(function(){
        $(this).css("opacity","0.6");
    })
    $("#daohang ul li a").mouseenter(function(){
        var $parent=$(this).parent();
        var left=$parent.position().left+470;
        $(".dhua").stop(true,true).animate({left:left,width:"82px"},"fast");
    })
    $("#wenben table:eq(1) tr td ").hover(function(){
        $(this ).css("color","#fe9900");
    },function(){
        $(this).css("color","white");
    })

    $("#adress1").focus(function(){
        var $s1=$(this).val();//val()函数还有一个作用就是用于下拉列表，单选框，多选框的默认选项：$("#id").val(["option.value","option.value"])
        if($s1=="请输入手机号"){
            $(this).val("");
        }
    })
    $("#adress1").blur(function(){
        var $s1=$(this).val();
        if($s1==""){
            $(this).val("请输入手机号");
        }
    })
    $("#adress2").focus(function(){
        var $s1=$(this).val();
        if($s1=="请输入密码"){
            $(this).val("");
        }
    })
    $("#adress2").blur(function(){
        var $s1=$(this).val();
        if($s1==""){
            $(this).val("请输入密码");
        }
    })
    $("#dldaoh ul li:eq(1) a").click(function(){
        $(this).css("backgroundColor","white");
    })

})