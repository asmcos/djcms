// JavaScript Document

$(document).ready(function(){
// Home page Slider 1	
$('.home1').revolution(
	{
		delay:9000,
		startheight:550,
		startwidth:1200,
		hideThumbs:200,
		thumbWidth:100,							// Thumb With and Height and Amount (only if navigation Tyope set to thumb !)
		thumbHeight:50,
		thumbAmount:5,
		navigationType:"bullet",				// bullet, tmyTabclasshumb, none
		navigationArrows:"solo",				// nexttobullets, solo (old name verticalcentered), none

		navigationStyle:"square",				// round,square,navbar,round-old,square-old,navbar-old, or any from the list in the docu (choose between 50+ different item), custom


		navigationHAlign:"center",				// Vertical Align top,center,bottom
		navigationVAlign:"bottom",					// Horizontal Align left,center,right
		navigationHOffset:0,
		navigationVOffset:20,

		soloArrowLeftHalign:"left",
		soloArrowLeftValign:"center",
		soloArrowLeftHOffset:20,
		soloArrowLeftVOffset:20,

		soloArrowRightHalign:"right",
		soloArrowRightValign:"center",
		soloArrowRightHOffset:20,
		soloArrowRightVOffset:20,

		touchenabled:"on",						// Enable Swipe Function : on/off
		onHoverStop:"on",						// Stop Banner Timet at Hover on Slide on/off

		stopAtSlide:-1,							// Stop Timer if Slide "x" has been Reached. If stopAfterLoops set to 0, then it stops already in the first Loop at slide X which defined. -1 means do not stop at any slide. stopAfterLoops has no sinn in this case.
		stopAfterLoops:-1,						// Stop Timer if All slides has been played "x" times. IT will stop at THe slide which is defined via stopAtSlide:x, if set to -1 slide never stop automatic

		hideCaptionAtLimit:0,					// It Defines if a caption should be shown under a Screen Resolution ( Basod on The Width of Browser)
		hideAllCaptionAtLilmit:0,				// Hide all The Captions if Width of Browser is less then this value
		hideSliderAtLimit:0,					// Hide the whole slider, and stop also functions if Width of Browser is less than this value

		shadow:1,								//0 = no Shadow, 1,2,3 = 3 Different Art of Shadows  (No Shadow in Fullwidth Version !)
		fullWidth:"off"							// Turns On or Off the Fullwidth Image Centering in FullWidth Modus


	}); 

 // Home page Slider 5
 
$('.fullscreenbanner').revolution(
	{
		delay:9000,
		startheight:550,
		startwidth:1200,

		hideThumbs:200,

		thumbWidth:100,							// Thumb With and Height and Amount (only if navigation Tyope set to thumb !)
		thumbHeight:50,
		thumbAmount:5,

		navigationType:"both",					//bullet, thumb, none, both		(No Thumbs In FullWidth Version !)
		navigationArrows:"verticalcentered",		//nexttobullets, verticalcentered, none
		navigationStyle:"square",				//round,square,navbar

		touchenabled:"on",						// Enable Swipe Function : on/off
		onHoverStop:"on",						// Stop Banner Timet at Hover on Slide on/off

		navOffsetHorizontal:0,
		navOffsetVertical:20,

		stopAtSlide:-1,
		stopAfterLoops:-1,

		shadow:0,								//0 = no Shadow, 1,2,3 = 3 Different Art of Shadows  (No Shadow in Fullwidth Version !)
		fullWidth:"on",							// Turns On or Off the Fullwidth Image Centering in FullWidth Modus
		fullScreen:"on",
		fullScreenOffsetContainer:".header"
	});	  
	
// Home page Slider 7	
$('.home7').revolution(
	{
		delay:9000,
		startheight:550,
		startwidth:1200,


		hideThumbs:200,

		thumbWidth:100,							// Thumb With and Height and Amount (only if navigation Tyope set to thumb !)
		thumbHeight:50,
		thumbAmount:3,

		navigationType:"thumb",				// bullet, thumb, none
		navigationArrows:"nexttobullets",				// nexttobullets, solo (old name verticalcentered), none

		navigationStyle:"round",				// round,square,navbar,round-old,square-old,navbar-old, or any from the list in the docu (choose between 50+ different item), custom


		navigationHAlign:"right",				// Vertical Align top,center,bottom
		navigationVAlign:"bottom",					// Horizontal Align left,center,right
		navigationHOffset:20,
		navigationVOffset:20,

		soloArrowLeftHalign:"left",
		soloArrowLeftValign:"center",
		soloArrowLeftHOffset:20,
		soloArrowLeftVOffset:0,

		soloArrowRightHalign:"right",
		soloArrowRightValign:"center",
		soloArrowRightHOffset:20,
		soloArrowRightVOffset:0,

		touchenabled:"on",						// Enable Swipe Function : on/off
		onHoverStop:"on",						// Stop Banner Timet at Hover on Slide on/off

		stopAtSlide:-1,							// Stop Timer if Slide "x" has been Reached. If stopAfterLoops set to 0, then it stops already in the first Loop at slide X which defined. -1 means do not stop at any slide. stopAfterLoops has no sinn in this case.
		stopAfterLoops:-1,						// Stop Timer if All slides has been played "x" times. IT will stop at THe slide which is defined via stopAtSlide:x, if set to -1 slide never stop automatic

		hideCaptionAtLimit:0,					// It Defines if a caption should be shown under a Screen Resolution ( Basod on The Width of Browser)
		hideAllCaptionAtLilmit:0,				// Hide all The Captions if Width of Browser is less then this value
		hideSliderAtLimit:0,					// Hide the whole slider, and stop also functions if Width of Browser is less than this value

		shadow:1,								//0 = no Shadow, 1,2,3 = 3 Different Art of Shadows  (No Shadow in Fullwidth Version !)
		fullWidth:"off"							// Turns On or Off the Fullwidth Image Centering in FullWidth Modus


	}); 
	
	
// Home page Slider 7	
$('.home8').revolution(
	{
		delay:9000,
		startheight:550,
		startwidth:1200,


		onHoverStop:"on",						// Stop Banner Timet at Hover on Slide on/off

		thumbWidth:100,							// Thumb With and Height and Amount (only if navigation Tyope set to thumb !)
		thumbHeight:50,
		thumbAmount:3,

		hideThumbs:0,
		navigationType:"thumb",				// bullet, thumb, none
		navigationArrows:"nexttobullets",				// nexttobullets, solo (old name verticalcentered), none

		navigationStyle:"square",				// round,square,navbar,round-old,square-old,navbar-old, or any from the list in the docu (choose between 50+ different item), custom


		navigationHAlign:"center",				// Vertical Align top,center,bottom
		navigationVAlign:"bottom",					// Horizontal Align left,center,right
		navigationHOffset:0,
		navigationVOffset:20,

		soloArrowLeftHalign:"left",
		soloArrowLeftValign:"center",
		soloArrowLeftHOffset:20,
		soloArrowLeftVOffset:0,

		soloArrowRightHalign:"right",
		soloArrowRightValign:"center",
		soloArrowRightHOffset:20,
		soloArrowRightVOffset:0,

		touchenabled:"on",						// Enable Swipe Function : on/off



		stopAtSlide:-1,							// Stop Timer if Slide "x" has been Reached. If stopAfterLoops set to 0, then it stops already in the first Loop at slide X which defined. -1 means do not stop at any slide. stopAfterLoops has no sinn in this case.
		stopAfterLoops:-1,						// Stop Timer if All slides has been played "x" times. IT will stop at THe slide which is defined via stopAtSlide:x, if set to -1 slide never stop automatic

		hideCaptionAtLimit:0,					// It Defines if a caption should be shown under a Screen Resolution ( Basod on The Width of Browser)
		hideAllCaptionAtLilmit:0,				// Hide all The Captions if Width of Browser is less then this value
		hideSliderAtLimit:0,					// Hide the whole slider, and stop also functions if Width of Browser is less than this value


		fullWidth:"on",

		shadow:0								//0 = no Shadow, 1,2,3 = 3 Different Art of Shadows -  (No Shadow in Fullwidth Version !)


	}); 
	
	
	
// Navigation Menu
	$('ul.mainmenucontain li').hover(
		function(){
			$(this).children('div').css('display','table')
		},
		function(){	
			$(this).children('div').css('display','none')
		}
	);
		  
// Main Menu mobile
	 $("<select />").appendTo(".menurelative");
	  
	 // Create default option "Go to..."
	  $("<option />", {
		 "selected": "selected",
		 "value"   : "",
		 "text"    : "Go to..."
	  }).appendTo("nav.subnav select");
      
	// Populate dropdown with menu items
      $("nav.subnav a[href]").each(function() {
       var el = $(this);
       $("<option />", {
           "value"   : el.attr("href"),
           "text"    : el.text()
       }).appendTo("nav.subnav select");
      });
      
	 // To make dropdown actually work
      $("nav.subnav select").change(function() {
        window.location = $(this).find("option:selected").val();
      });
	  
	  
// Fancybox 
	$('a.prettyphotpopup').prettyPhoto({animation_speed:'normal',theme:'light_square',slideshow:3000, autoplay_slideshow: false, allow_expand: false});	


//  Accrodian	
	$("#accrodian").collapse({toggle: false})

//  Accrodian	
	var $acdata = $('.accrodian-data'),
		$acclick = $('.accrodian-trigger');

	$acdata.hide();
	$acclick.first().addClass('active').next().show();	
	
	$acclick.on('click', function(e) {
		if( $(this).next().is(':hidden') ) {
			$acclick.removeClass('active').next().slideUp(300);
			$(this).toggleClass('active').next().slideDown(300);
		}
		e.preventDefault();
	});
	
//  Accrodian	
	var $acdata1 = $('.accrodian-data-faq'),
		$acclick1 = $('.accrodian-trigger-faq');

	$acdata1.hide();
	$acclick1.first().addClass('active').next().show();	
	
	$acclick1.on('click', function(e) {
		if( $(this).next().is(':hidden') ) {
			$acclick1.removeClass('active').next().slideUp(300);
			$(this).toggleClass('active').next().slideDown(300);
		}
		e.preventDefault();
	});

// Toggle			
	$('.togglehandle').click(function()
	{
		$(this).toggleClass('active')
		$(this).next('.toggledata').slideToggle()
	});
	
// Dropdowns
	$('.dropdown').hover(
		function(){$(this).addClass('open')			
		},
		function(){			
			$(this).removeClass('open')
		}
		);

//Tab Why Us
	$('#myTab a').click(function (e) {
		e.preventDefault()
  		$(this).tab('show');
	})
	$('#myTab a:first').tab('show') // Select first tab
	//Tab Why Us
	$('.myTabclass a').click(function (e) {
		e.preventDefault()
  		$(this).tab('show');
	})
	$('.myTabclass a:first').tab('show') // Select first tab

//Messages
	$('.alert .icon-remove').click(function (e) {
		$(this).parent('.alert').fadeOut();
	})
			
// Product thumbnails
	$('.thumbnail').each(function(){		
		$(this).hover(
		function(){
			$(this).children('.shortlinks').fadeIn()
		},
		function(){	
			$(this).children('.shortlinks').fadeOut()
		});		
	});
	$('.thumbnail').each(function()
	{
		$(this).hover(
		function(){
			$(this).children('.shortlinksourteam').fadeIn()
		},
		function(){	
			$(this).children('.shortlinksourteam').fadeOut()
		}
		);
	});

// Product Thumb Zoom
	$('.my-foto-container').imagezoomsl({ 
	 zoomrange: [1, 12],
         zoomstart: 4,
         innerzoom: true,
         magnifierborder: "none",	    
          magnifiersize: [500, 300],
          scrollspeedanimate: 10,
          loopspeedanimate: 5,          
         // magnifiereffectanimate: "slideIn"	
	}); 
	$ (".zoom" ).click( function () {
    var That =  this ;
    $( ".my-foto-container" ).fadeOut ( 100 , function (){
	 $(this).attr( "src" ,$ ( That).attr ( "src" ))            
     . attr ("data-large", $ (That).attr ("data-large")).fadeIn (200 )
	 . attr ("data-title", $ (That).attr ("data-title"))
	 . attr ("data-help", $ (That).attr ("data-help"))
				
           }); 
       }); 
	
	
// List & Grid View
	$('#productlist .featureprojectwrap:first').show()
	$('#list').click(function()
	{	$(this).addClass ('btn-orange').children('i').addClass('icon-white')
		$('.grid').fadeOut()
		$('.list').fadeIn()
		$('#grid').removeClass ('btn-orange').children('i').removeClass('icon-white')
	});
	$('#grid').click(function()
	{	$(this).addClass ('btn-orange').children('i').addClass('icon-white')
		$('.list').fadeOut()
		$('.grid').fadeIn()
		$('#list').removeClass ('btn-orange').children('i').removeClass('icon-white')
	});
	
// Tooltip	
	$('.tooltip-test').tooltip();

// Scroll top
	$(window).scroll(function () {
			if ($(this).scrollTop() > 50) {
				$('#gotop').fadeIn(500);
							
			} else {
				$('#gotop').fadeOut(500);
			}
		});	
	$('#gotop').click(function()
			{
				
				$("html, body").animate({ scrollTop: 0 }, 600);
			})
			
// Checkout steps
	$('.checkoutsteptitle').addClass('down').next('.checkoutstep').fadeIn()
	$('.checkoutsteptitle').on('click', function()
	{		
	
	$("select, input:checkbox, input:radio, input:file").css('display', 'blcok');	
		$(this).toggleClass('down').next('.checkoutstep').slideToggle()
	});	
	
// Coming Soon
	//cowntdown function. Set the date by modifying the date in next line (January 01, 2013 00:00:00):
		var austDay = new Date("December 31, 2013 00:00:00");
		
			$('#comingsoon').countdown({until: austDay, layout: '<div class="box"><div>{dn}</div> <span> {dl} </span></div> <div class="box"><div>{hn}</div> <span> {hl} </span></div> <div class="box"><div>{mn}</div> <span> {ml} </span></div> <div class="box"><div>{sn}</div> <span> {sl} </span></div>'});
			$('#year').text(austDay.getFullYear());

// google map	
$("#contactmap").gMap({
	address: "pxcreate, Elizabeth Street, Melbourne, Victoria, Australia",//replace this with your address
	zoom: 10,
	markers:[
		{
			latitude: -37.817361, //replace this with your latitude
			longitude: 144.965047,//replace this with your longitude
			html: "pxcreate Pty Ltd" //replace this with your text
		}		
	]
});
	
// Social Steams 
   $('.flickr-feed').socialstream({
			socialnetwork: 'flickr',
			limit: 12,
			username: 'flickr',        })
	$('.pinterest-feed').socialstream({
			socialnetwork: 'pinterest',
			limit: 12,
			username: 'pinterest'
	})
	$('.dribbble-feed').socialstream({
			socialnetwork: 'dribbble',
			limit: 12,
			username: 'dribbble'
	})
	$('.youtube-feed').socialstream({
			socialnetwork: 'youtube',
			limit: 12,
			username: 'youtube'
	})
	$('.instagram-feed').socialstream({
			socialnetwork: 'instagram',
			limit: 12,
			username: 'instagram',
			overlay: true
	})
	
 
// Twitter
		$("#twitter").tweet({
     	join_text: "auto",
      	username: "pxcreate", //replace this with your username
		modpath: './twitter/',
     	avatar_size: 32,
      	count: 3,
      	auto_join_text_default: "we said,",
      	auto_join_text_ed: "we",
      	auto_join_text_ing: "we were",
     	auto_join_text_reply: "we replied",
     	auto_join_text_url: "we were checking out",
      	loading_text: "loading tweets..."
 	    });
	
// Contact Form 
		$(".contactform").validate({
	   submitHandler: function(form) {
		   var name = $("input#name").val();
		   var email = $("input#email").val();
		   var url = $("input#url").val();
		   var message = $("textarea#message").val();
		   
		   var dataString = 'name='+ name + '&email=' + email + '&url=' + url+'&message='+message;
		  $.ajax({
		  type: "POST",
		  url: "email.php",
		  data: dataString,
		  success: function() {
			  $('#contactmsg').remove();
			  $('.contactform').prepend("<div id='contactmsg' class='successmsg'>Form submitted successfully!</div>");
			   $('#contactmsg').delay(1500).fadeOut(500);
			  $('#submit_id').attr('disabled','disabled');
			  }
		 	});   
	   return false;
	  	}
		});
	});


// Window load Funcitons 

$(window).load(function() {
// Home page Slider 2
	$("#mainslider2").carouFredSel({
		responsive: true,
	items		: 1,
	scroll		: {
		fx			: "crossfade"
	},
	auto: false,
	//mousewheel: true,	
	swipe: {
		onMouse: true,
		onTouch: true
	},
	
	pagination	: {
		container		: "#mainslider2_pag",
		anchorBuilder	: function( nr ) {
			var src = $("img", this).attr( "src" );
				//src = src.replace( "/large/", "/small/");
			return '<img src="' + src + '" style="width:100px" />';
			}
		}
	});
	
// Home page Slider 3	
  // The slider being synced must be initialized first
  $('#carouseindex3').flexslider({
	animation: "slide",
	controlNav: false,
	animationLoop: false,
	slideshow: false,
	itemWidth: 230,
	//itemMargin: 15,
	asNavFor: '#sliderindex3'
  });
  
  $('#sliderindex3').flexslider({
	animation: "slide",
	controlNav: false,
	animationLoop: false,
	slideshow: false,
	sync: "#carouseindex3"
  });
  
// Home page Slider 4 
	$('#mainslider4').flexslider({
        animation: "slide",		
        start: function(slider){
          $('body').removeClass('loading');
        }
   });	

// Home page Slider 6				
	$('#mainslider6').carouFredSel({
		//width: 900,
		//height: '100%',
		direction: 'up',
		auto : false,
		items: 1,
		prev: '#prevmainslider6',
		next: '#nextmainslider6',
		pagination: "#pagermainslider6",
		//mousewheel: true,
		swipe: {
			onMouse: true,
			onTouch: true
		}
	});

// Home page Slider 10	
			function prevTimers() {
				return allTimers().slice( 0, $('.sliderindex10pager a.selected').index() );
			}
			function allTimers() {
				return $('.sliderindex10pager a span');
			}

			$(function() {
				$('#sliderindex10').carouFredSel({
					items: 1,
					responsive : true,
					auto: {
						pauseOnHover: 'resume',
						progress: {
							bar: '.sliderindex10pager a:first span'
						}
					},
					scroll: {
						fx: 'crossfade',
						duration: 300,
						timeoutDuration: 2000,
						onAfter: function() {
							allTimers().stop().width( 0 );
						//	prevTimers().width(  );
							$(this).trigger('configuration', [ 'auto.progress.bar', '.sliderindex10pager a.selected span' ]);
						}
					},
					pagination: {
						container: '.sliderindex10pager',
						anchorBuilder: false
					}
				});
			});			

//OurClient Carousal
	$('#ourclientcarousal').carouFredSel({
		width: '100%',
		scroll: 1,
		auto: false,
		prev: '#prevclient',
		next: '#nextclient',
	   // mousewheel: true,
		
		swipe: {
			onMouse: true,
			onTouch: true
		}
	});			
	
// Flexslider  Musthave    
	$('#bannerslider').flexslider({
        animation: "fade",		
        start: function(slider){
          $('body').removeClass('loading');
    }
      });
	  
// Flexslider  Testimonial   	  
	  $('#testimonialsidebar').flexslider({
        animation: "slide",	
		auto: false,	
        start: function(slider){
          $('body').removeClass('loading');
    }
	  });
	  
// Flexslider  Portfolio   	  
	  $('#portfolioslider').flexslider({
        animation: "slide",		
        start: function(slider){
          $('body').removeClass('loading');
    }
	  });	  
	  
// Flexslider  Latest Blog	  
	   $('#latesetblogsidebar').flexslider({
        animation: "fade",		
        start: function(slider){
          $('body').removeClass('loading');
    }
      });  
	  
	  
//OurClient Carousal
	$('#ourclientcarousal').carouFredSel({
		width: '100%',
		scroll: 1,
		auto: false,
		prev: '#prevclient',
		next: '#nextclient',
	   // mousewheel: true,
		
		swipe: {
			onMouse: true,
			onTouch: true
		}
	});
	}); 
	

//All Carousals	 - Flex plugin
(function() {  
// store the slider in a local variable
	var $window = $(window),
		flexslider;
		
// 5 COLUMN carousal
function getGridSizecolumn5() {
		return  (window.innerWidth < 480) ? 1 :
				(window.innerWidth < 600) ? 2 :
				(window.innerWidth < 900) ? 3 : 5;
  	} 
$window.load(function() {
	$('.column5').flexslider({
		animation: "slide",
		animationSpeed: 400,
		animationLoop: false,
		slideshow : false,
		itemWidth: 210,	
		itemMargin: 30,	
		minItems: getGridSizecolumn5(), // use function to pull in initial value
		maxItems: getGridSizecolumn5(), // use function to pull in initial value
		start: function(slider){
		$('body').removeClass('loading');
 		flexslider = slider;
      	}
	});
})


// 4 COLOUMN carosal
 
// tiny helper function to add breakpoints
	function getGridSizecolumn4() {
		return  (window.innerWidth < 480) ? 1 :
				(window.innerWidth < 600) ? 2 :
				(window.innerWidth < 900) ? 3 : 4;
  	} 
	$window.load(function() {
	$('.column4').flexslider({
		animation: "slide",
		animationSpeed: 400,
		animationLoop: false,
		slideshow : false,
		itemWidth: 270,
		itemMargin: 33,
		minItems: getGridSizecolumn4(), // use function to pull in initial value
		maxItems: getGridSizecolumn4(), // use function to pull in initial value
		start: function(slider){
		$('body').removeClass('loading');
 		flexslider = slider;
      	}
	});
	})
	


// 3 COLOUMN carosal
	// tiny helper function to add breakpoints
	function getGridSizecolumn3() {
		return  (window.innerWidth < 480) ? 1 :
				(window.innerWidth < 600) ? 2 :
				(window.innerWidth < 900) ? 3 : 3;
  	} 
	$window.load(function() {
	$('.column3').flexslider({
		animation: "slide",
		animationSpeed: 400,
		animationLoop: false,
		slideshow : false,
		itemWidth: 270,
		itemMargin: 34,
		minItems: getGridSizecolumn3(), // use function to pull in initial value
		maxItems: getGridSizecolumn3(), // use function to pull in initial value
		start: function(slider){
		$('body').removeClass('loading');
 		flexslider = slider;
      	}
	});
	})


// 2 COLOUMN carosal
	function getGridSizecolumn2() {
	   return   (window.innerWidth < 480) ? 1 :
				(window.innerWidth < 600) ? 2 :
        		(window.innerWidth < 900) ? 2 : 2;
 	}	
	
	$window.load(function() {
	$('.column2').flexslider({
		animation: "slide",
		animationSpeed: 400,
		animationLoop: false,
		slideshow : false,
		itemWidth: 260,
		itemMargin: 30,
		minItems: getGridSizecolumn2(), // use function to pull in initial value
		maxItems: getGridSizecolumn2(), // use function to pull in initial value
		start: function(slider){
			$('body').removeClass('loading');
            flexslider = slider;
          }
        });		
	});
	
  }());
// Animation


$(document).ready(function() {	
  	$('.seodetails').bind('inview', function (event, visible) {
        if (visible == true) {
            $('.headingcenter, .metadetails').addClass("animated pulse time3");        
        }else{
            $('.headingcenter, .metadetails').removeClass("animated pulse time3");
        }
    });
	$('.ourprocess').bind('inview', function (event, visible) {
        if (visible == true) {
            $('.ourprocess').addClass("animated pulse time3");        
        }else{
            $('.ourprocess').removeClass("animated pulse time3");
        }
    });	
	$('.features, .features-home2, .features-home4, .features-home5').bind('inview', function (event, visible) {
        if (visible == true) {
            $('.features, .features-home2, .features-home4, .features-home5').addClass("animated fadeInUp time3");        
        }else{
            $('.features, .features-home2, .features-home4, .features-home5').removeClass("animated fadeInUp time3");
        }
    });		
	
	$('#footer').bind('inview', function (event, visible) {
        if (visible == true) {
            $('#footer .footersocial .container').addClass("animated fadeInUp time3");        
        }else{
            $('#footer .footersocial .container').removeClass("animated fadeInUp time3");
        }	
    });	
	$('.heading1').bind('inview', function (event, visible) {
        if (visible == true) {
            $(this).addClass("animated fadeInUp time3");        
        }else{
            $(this).removeClass("animated fadeInUp time3");
        }	
    });
	$('.heading2').bind('inview', function (event, visible) {
        if (visible == true) {
            $(this).addClass("animated fadeInUp time3");        
        }else{
            $(this).removeClass("animated fadeInUp time3");
        }	
    });	
	$('.titles').bind('inview', function (event, visible) {
        if (visible == true) {
            $(this).addClass("animated fadeInUp time3"); 
			$('.titles i').addClass("animated flip time3");          
        }else{
            $(this).removeClass("animated fadeInUp time3");
			$('.titles i').removeClass("animated flip time3"); 
        }	
    });

});
	 
	 
	 
	

	