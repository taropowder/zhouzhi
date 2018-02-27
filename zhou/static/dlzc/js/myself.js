jQuery(window).load(function () {
	// Fade out the Loading animation
	 $('.loadingBg').fadeOut(1500);
	 $("#QuotePagetitleBreadcrumbsWrapper").delay(1000).addClass('animated bounceInDown');
	 $(".image404").delay(1400).addClass('animated flip');
});

$(document).ready(function() {

		$(function () {    
		  $('.dropdown li').hover(function () {
			$('ul', this).stop(true, true).delay(100).slideDown(200);
		  }, function () {
			$('ul', this).stop(true, true).delay(50).slideUp(200);
		  });
		});
		var bcWidth = ($('#breadcrumbsWrapper span.left').outerWidth(true)) + ($('#breadcrumbsWrapper div.breadcrumbsContainer').outerWidth(true)) + ($('#breadcrumbsWrapper span.right').outerWidth(true) + 10);
		$('#breadcrumbsWrapper').css("width",bcWidth);	
		
		/* Adds nice animation to the services|menu widget & related posts menu */
		$("#servicesWidget li p, .RPMItems li p").hover(function () {
			  $(this).stop().animate({'text-indent': '10px'}, 150);
			  }, 
			  function () {
			  $(this).stop().animate({'text-indent': '0'}, 150);
		});
		
		/* remove margin on the last gallery items */
		$(".galleryItemsList3Col li:nth-child(3n + 3)").css("margin-right", "0px");
		$(".galleryItemsList li:nth-child(2n+2)").css("margin-right", "0px");

		$(document).ready(function(){
			$("a[rel^='prettyPhoto']").prettyPhoto({
				animationSpeed: 'normal', /* fast/slow/normal */
				opacity: 0.80, /* Value between 0 and 1 */
				showTitle: true, /* true/false */
				deeplinking: true, /* Allow prettyPhoto to update the url to enable deeplinking. */
				social_tools: false /* delete this line to enable social network sharing */
			});
		});
		
		/* Rollover effect on Featured image carousel | Services thumbnails | Blog Post Thumbnails | Blog Images | Gallery Images */
		$('.featuredImageContainer a, .servicesThumbImageContainer a, .postThumbAndMeta a, .postImageContainer a, .galleryImageContainer a, .galleryImageContainer3col a').hover(function(){
			$(this).children('.featuredImageContainer a span, .servicesThumbImageContainer a span, .postThumbAndMeta a span, .postImageContainer a span, .galleryImageContainer a span, .galleryImageContainer3col a span').stop().fadeTo(350, 0.8);
			},function(){
			  $(this).children('.featuredImageContainer a span, .servicesThumbImageContainer a span, .postThumbAndMeta a span, .postImageContainer a span, .galleryImageContainer a span, .galleryImageContainer3col a span').stop().fadeTo(350, 0);
			  }
		);
			    	
	    /* -- Page Curl Animation -- */
		$(".imageFlip").hover(function() {
			$(this).children(".postImageContainerCorner, .galleryImageContainerCorner").stop().animate({width: '73px', height: '74px'}, 500);
			/* animates the page peel */
			$(this).children(".imageFlip a").stop().animate({width: '78px',height: '87px'}, 500);} , function() {
				/* when done, sets everythig back to original */
				$(this).children(".imageFlip a").stop().animate({width: '54px',height: '56px'}, 220);
				$(this).children(".postImageContainerCorner, .galleryImageContainerCorner").stop().animate({width: '52px', height: '51px'}, 220);
		});
		
		// jQuery Quicksand project categories filtering (Portfolio Filtering)
		// Thanks to Sacha Greif - http://www.sachagreif.com/
		
		jQuery(document).ready(function($){
			// Clone applications to get a second collection
			var $data = $(".galleryItemsList, .galleryItemsList3Col").clone();
			
			//NOTE: Only filter on the main portfolio page, not on the subcategory pages
			$('.sortNav li').click(function(e) {
				$(".sortNav li").removeClass("active");	
				// Use the last category class as the category to filter by. This means that multiple categories are not supported (yet)
				var filterClass=$(this).attr('class').split(' ').slice(-1)[0];
				
				if (filterClass == 'all-projects') {
					var $filteredData = $data.find('.project');
				} else {
					var $filteredData = $data.find('.project[data-type=' + filterClass + ']');
				}
				$(".galleryItemsList, .galleryItemsList3Col").quicksand($filteredData, {
					duration: 800,
					easing: 'easeInOutQuad'
			
				},	function(){
						//callback function to re-apply hover effects on cloned elements
						/* Rollover effect on Featured image carousel | Services thumbnails | Blog Post Thumbnails | Blog Images | Gallery Images */
						$('.featuredImageContainer a, .servicesThumbImageContainer a, .postThumbAndMeta a, .postImageContainer a, .galleryImageContainer a, .galleryImageContainer3col a').hover(function(){
							$(this).children('.featuredImageContainer a span, .servicesThumbImageContainer a span, .postThumbAndMeta a span, .postImageContainer a span, .galleryImageContainer a span, .galleryImageContainer3col a span').stop().fadeTo(350, 0.8);
							},function(){
							  $(this).children('.featuredImageContainer a span, .servicesThumbImageContainer a span, .postThumbAndMeta a span, .postImageContainer a span, .galleryImageContainer a span, .galleryImageContainer3col a span').stop().fadeTo(350, 0);
							  }
						);
						/* -- Page Curl Animation -- */
						$(".imageFlip").hover(function() {
							$(this).children(".postImageContainerCorner, .galleryImageContainerCorner").stop().animate({width: '73px', height: '74px'}, 500);
							/* animates the page peel */
							$(this).children(".imageFlip a").stop().animate({width: '78px',height: '87px'}, 500);} , function() {
								/* when done, sets everythig back to original */
								$(this).children(".imageFlip a").stop().animate({width: '54px',height: '56px'}, 220);
								$(this).children(".postImageContainerCorner, .galleryImageContainerCorner").stop().animate({width: '52px', height: '51px'}, 220);
						});	
						
						/* prettyPhoto re-Initialize */
						$(document).ready(function(){
							$("a[rel^='prettyPhoto']").prettyPhoto({
								animationSpeed: 'normal', /* fast/slow/normal */
								opacity: 0.80, /* Value between 0 and 1 */
								showTitle: true, /* true/false */
								deeplinking: true, /* Allow prettyPhoto to update the url to enable deeplinking. */
								social_tools: false /* delete this line to enable social network sharing */
							});
						});
				});		
				$(this).addClass("active"); 			
				return false;
			});
		});

})