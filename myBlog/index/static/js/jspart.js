// JavaScript Document

//initiating jQuery
jQuery(function($) {
	$(document).ready( function() {
		//enabling stickUp on the '.navbar-wrapper' class
		$('#navbar1').stickUp({
			marginTop:'auto'
		});
	});
});

//导航条点击
$("#mytab2 a").click(function(e){
    e.preventDefault();
    $(this).tab("show");
});

//返回顶部按钮
$(function(){
    $(".js-affixed-element-bottom").affix({
        offset:{
        }
    })
});