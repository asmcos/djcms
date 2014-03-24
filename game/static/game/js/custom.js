$('.my-tooltip').tooltip();

/* *************************************** */ 
/* Scroll to Top */
/* *************************************** */  
		
$(document).ready(function() {
	$(".totop").hide();
	
	$(window).scroll(function(){
	if ($(this).scrollTop() > 300) {
		$('.totop').fadeIn();
	} else {
		$('.totop').fadeOut();
	}
	});
	$(".totop a").click(function(e) {
		e.preventDefault();
		$("html, body").animate({ scrollTop: 0 }, "slow");
		return false;
	});
		
});
/* *************************************** */