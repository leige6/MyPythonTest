$(function(){function n(n){$(".js-bookimg").children("a").eq(n).fadeIn().siblings().fadeOut(),$(".js-listcont").children("dl").eq(n).addClass("on").siblings().removeClass("on");var s=138*n+90;$(".js-rline").stop(!0,!0).animate({top:s+"px"},100)}function s(){l++;var s=$(".js-bookimg").find("a").length;l>=s&&(l=0),n(l)}function i(n){$(".js-listnav li").eq(n).addClass("on").siblings().removeClass("on"),$(".js-listcont ul").hide(),$(".js-listcont ul").eq(n).fadeIn(500)}$(".js-hotgame li").hover(function(){$(this).children(".fldiv").stop(!0,!0).fadeIn(100),$(this).children(".fdiv").stop(!0,!0).fadeOut(300)},function(){$(this).children(".fldiv").stop(!0,!0).fadeOut(100),$(this).children(".fdiv").stop(!0,!0).fadeIn(300)});scroll.scroll($(".js-hotgame"),4,1,$(".js-prev"),$(".js-next")),scroll.moviescroll($(".js-scrollmovie"),1,1,$(".js-mleft"),$(".js-mright"));scroll.newshow(),scroll.flashbox(),scroll.video(),$(".js-navbar li,.company").hover(function(){$(this).children(".child-nav").length>0&&$(this).children(".child-nav").toggle()});var l=0;$(".js-booklist").click(function(){clearInterval(t),s(),t=setInterval(s,5e3)}),$(".js-listcont dl").click(function(){clearInterval(t),n(l=$(this).index()),t=setInterval(s,5e3)});var t=setInterval(s,5e3);!function(){var n=document.location.href.split("/")[3].split(".")[0],s=0;if(100==(s="game"==n?2:"news"==n?1:"movie"==n?3:""==n?0:"mobile"==n?6:"product"==n?4:100)){var i;"about"==n?i=0:"annals"==n?i=1:"contact"==n&&(i=3),1==s&&(i=2),$(".cMenu li").eq(i).children("a").addClass("cOn")}else $(".js-navbar li").eq(s).children("a").addClass("on")}(),$(window).scroll(function(){$(window).width()>1e3&&($(".js-rightnav").css({top:$(window).scrollTop()+$(window).height()-400}),$(window).scrollTop()>300?$(".js-rightnav").fadeIn(500):$(".js-rightnav").fadeOut(500))}),$(".js-listnav li").click(function(){var n=$(this).index();$(".js-listnav li").eq(n).addClass("on").siblings().removeClass("on"),$(".js-listcont ul").hide(),$(".js-listcont ul").eq(n).fadeIn(500)}),$(".js-gotop").click(function(){return $("body,html").animate({scrollTop:0},0),!1});var e=function(n){var s=new RegExp("(^|&)"+n+"=([^&]*)(&|$)"),i=window.location.search.substr(1).match(s);return null!=i?unescape(i[2]):null}("type");if(null!=e&&e.toString().length>0)switch(e){case"0":case"1":case"2":case"3":i(e)}else i(0);$(".js-listcont li").hover(function(){$(this).find(".productmore").stop(!0,!0).fadeIn(100)},function(){$(this).find(".productmore").stop(!0,!0).fadeOut(0)}),$(".js-rclose").click(function(){$(".right-nav").fadeOut()})});