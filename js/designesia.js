(function($){ "use strict";	

	var v_count = '0';

	/* Page scroll to id */
	if ($('body').hasClass("de-navbar-left")) {
       	$(".mainmenu li a, a.scroll-to").mPageScroll2id({
	        highlightSelector: ".mainmenu li a",
	        offset: 0,
	        scrollSpeed:750,
	        scrollEasing: "easeInOutCubic"
	    });	
    } else {
       	$("#mainmenu li a, a.scroll-to").mPageScroll2id({
	        highlightSelector: "#mainmenu li a",
	        offset: 70,
	        scrollSpeed:750,
	        scrollEasing: "easeInOutCubic"
	    }); 
    }

	/* ========================================== 
    Header Mobile
    ========================================== */
    $( "#menu-btn" ).on('click', function() {
        $(this).toggleClass( "active" );
        if ($(this).hasClass( "active" )) {
            $('#mainmenu, .mainmenu').stop(true, true).slideDown();
        }else{
            $('#mainmenu, .mainmenu').stop(true, true).slideUp();
        }       
    });

	/*mobile_mainmenu create span*/
    $('#mainmenu li:has(ul)').prepend('<span class="arrow"></span>');
    $("#mainmenu > li span.arrow").click(function() {
        $(this).parent().find("> ul").stop(true, true).slideToggle();
        $(this).toggleClass( "active" ); 
    });


    /* --------------------------------------------------
    * function
    * --------------------------------------------------*/
    function video_autosize(){
        $('.de-video-container').each(function() {
            var height_1 = $(this).css("height");
            var height_2 = $(this).find(".de-video-content").css("height");
            var newheight = (height_1.substring(0, height_1.length - 2)-height_2.substring(0, height_2.length - 2))/2;
            $(this).find('.de-video-overlay').css("height", height_1);
            $(this).find(".de-video-content").animate({'margin-top': newheight},'fast');
        });
    }

    function init() {        
        var sh = $('#de-sidebar').css("height");
        var dh = $(window).innerHeight();
        var h  = parseInt(sh) - parseInt(dh);
        var header_height = parseInt($('.site-header').height(), 10);
        var screen_height = parseInt($(window).height(), 10);
        var header_mt = screen_height - header_height;
        var mq = window.matchMedia("(min-width: 993px)");
        var ms = window.matchMedia("(min-width: 768px)");

        window.addEventListener('scroll', function (e) {

        	/* header shrink class */
            if (mq.matches) {
                var distanceY = window.pageYOffset || document.documentElement.scrollTop,
                    shrinkOn = 100,
                    header = document.querySelector(".site-header");

                if (distanceY > shrinkOn) {
                    $(".site-header").addClass("smaller", 1000, "easeOutBounce");
                } else {
                    if ( $(".site-header").hasClass("smaller") ) {
                        $(".site-header").removeClass("smaller");
                    }
                }
            }    

            if (mq.matches) {
                /* header autoshow on scroll begin */
                var scrollTop = $(window).scrollTop();
                var vscroll = 0;

                if (scrollTop >= 50 && vscroll == 0) {
                    $("header.autoshow").removeClass("scrollOff");
                    $("header.autoshow").addClass("scrollOn");
                    vscroll = 1;
                } else {
                    $("header.autoshow").removeClass("scrollOn");
                    $("header.autoshow").addClass("scrollOff");
                    vscroll = 0;
                }
                /* header autoshow on scroll close */

                /* header bottom on scroll begin */
                var header_height = parseInt($('.site-header').height(), 10);
                var screen_height = parseInt($(window).height(), 10);
                var header_mt = screen_height - header_height;

                if (scrollTop >= header_mt) {
                    $('.header-bottom').css("position", "fixed");
                    $('.header-bottom').css("top", "0");
                } else if (scrollTop <= header_mt) {
                    $('.header-bottom').css("position", "absolute");
                    $('.header-bottom').css("top", header_mt);
                }
                /* header bottom on scroll close */

                /*side header on scroll begin*/
                if ($("header").hasClass("side-header")) {
                    if ($(window).scrollTop() >= h) {
                        $('#de-sidebar').css("position", "fixed");
                        if (parseInt(sh) > parseInt(dh)) {
                            $('#de-sidebar').css("top", -h);
                        }
                    } else {
                        $('#de-sidebar').css("position", "absolute");
                        if (parseInt(sh) > parseInt(dh)) {
                            $('#de-sidebar').css("top", 0);
                        }
                    }
                }
                /*side header on scroll close*/
            }
        });

        if (mq.matches) {
            $('.header-bottom').css('position', 'absolute');
            $('.header-bottom').css('top', header_mt);
        }        

        /* Paralax Background */	
		var $window = $(window);
        $('section[data-type="background"]').each(function () {
            var $bgobj = $(this);
            $(window).scroll(function () {
            	var mq = window.matchMedia("screen and (min-width: 993px)");
		        if ( mq.matches ) {
		            var yPos = -($window.scrollTop() / $bgobj.data('speed'));
                    var coords = '50% ' + yPos + 'px';
                    $bgobj.css({ backgroundPosition: coords });
		        }
            });
            document.createElement("article");
            document.createElement("section");
        });

    }
    window.onload = init();

    $(window).on('resize', function() {
        video_autosize();
        init();

        $( ".site-header" ).removeClass( "smaller" );

        /*header bottom setting begin*/
        var mq = window.matchMedia("(max-width: 993px)");
        if (mq.matches) {
            $('.header-bottom').css("display", "block");
            $('.header-bottom').css("top", "0");
        }
        /*header bottom setting close*/

        /* --------------------------------------------------
        * custom page with background on side
        * --------------------------------------------------*/
        $('.side-bg').each(function(){ 
            $(this).find(".image-container").css("height",$(this).find(".image-container").parent().css("height"));
        });         
    });    

    $(window).on('load', function() {
        video_autosize();
        /* --------------------------------------------------
        * custom page with background on side
        * --------------------------------------------------*/
        $('.side-bg').each(function(){ 
            $(this).find(".image-container").css("height",$(this).find(".image-container").parent().css("height"));
        });

        /* --------------------------------------------------
        * tabs
        * --------------------------------------------------*/
        $('.de_tab').not('.de_tab_links').find('.de_tab_content div.de_tab_content_inner').hide();
        $('.de_tab').not('.de_tab_links').find('.de_tab_content div.de_tab_content_inner:first').show();
        $('li').find('.v-border').fadeTo(150,0);
        $('li.active').find('.v-border').fadeTo(150,1);
        $('.de_nav li').not('.de_nav_links li').click(function() {
            $(this).parent().find('li').removeClass("active");
            $(this).addClass("active");
            $(this).parent().parent().find('.v-border').fadeTo(150,0);
            $(this).parent().parent().find('.de_tab_content div.de_tab_content_inner').hide();
        
            var indexer = $(this).index(); 
            $(this).parent().parent().find('.de_tab_content div.de_tab_content_inner:eq(' + indexer + ')').fadeIn(); 
            $(this).find('.v-border').fadeTo(150,1);
        });

        /* Scroll Percent Opacity */
        var target = $('.center-y, .vertical-align');
        var targetHeight = target.outerHeight();      
        $(document).scroll(function(e){
            var scrollPercent = ( targetHeight - window.scrollY ) / targetHeight;
            if( scrollPercent >= 0 ){
                target.css('opacity', scrollPercent);
            }
        });

        /* btn arrow up */
        $(".arrow-up").on("click", function() {
            $(".coming-soon .coming-soon-content").fadeOut("medium",function(){
                $("#hide-content").fadeIn(600,function(){
                    $('.arrow-up').animate({'bottom': '-40px' },"slow");
                    $('.arrow-down').animate({'top': '0' },"slow");
                });
            });
        });
        
        /* btn arrow down */
        $(".arrow-down").on("click", function() {
            $("#hide-content").fadeOut("slow",function(){
                $(".coming-soon .coming-soon-content").fadeIn(800,function(){
                    $('.arrow-up').animate({'bottom': '0px' },"slow");
                    $('.arrow-down').animate({'top': '-40' },"slow");
                });
            });
        });
    });

    $(window).on('scroll', function() {
        
        /* counter */     
        $('.timer').each(function(){
            var imagePos = $(this).offset().top;           
            var topOfWindow = $(window).scrollTop();
            if (imagePos < topOfWindow+500 && v_count=='0') {       
                $(function ($) {
                    /*start all the timers*/
                    $('.timer').each(count);                                         
                    function count(options) {
                        v_count = '1';
                        var $this = $(this);
                        options = $.extend({}, options || {}, $this.data('countToOptions') || {});
                        $this.countTo(options);
                    }
                });             
            }
        });

        /* progress bar */
        $('.de-progress').each(function() {
            var pos_y = $(this).offset().top;
            var value = $(this).find(".progress-bar").attr('data-value');      
            var topOfWindow = $(window).scrollTop();
            if (pos_y < topOfWindow+500) {      
                $(this).find(".progress-bar").animate({'width': value },"slow");
            }
        });        
    });

    /* --------------------------------------------------
    * custom positiion
    * --------------------------------------------------*/
    var $doc_height = $(window).innerHeight(); 

    /* Custom .center-y */
    var picheight = $('.center-y').css("height");
    picheight = parseInt(picheight, 10);
    $('.center-y').css('margin-top', ( ( $doc_height - picheight ) / 2 ) - 90 );
    
    /* Custom .vertical-align */
    var vertical_height = $('.vertical-align').css("height");
    vertical_height = parseInt(vertical_height, 10);
    var bannerlogo_height = $('.banner-logo').css("height");
    bannerlogo_height = parseInt(bannerlogo_height, 10);
    $('.vertical-align').css('margin-top', (($doc_height - vertical_height)/2) - (70 + (bannerlogo_height/2)));
    
    $('#home-sec').css("height",$doc_height);
    $('.full-height').css("height", $doc_height);
    $('.full-height .de-video-container').css("height",$doc_height);
    $(window).on('resize', function(){
        $('#home-sec').css("height",$doc_height);
        $('.full-height').css("height", $doc_height);
        $('.full-height .de-video-container').css("height",$doc_height);
    });

    /* Filter Sub Categories */
    $('ul.listed_taxonomy_filters > li > a').on('click', function(e){
        $('ul.listed_taxonomy_filters > li > a').parent().removeClass("showchild");
        $(this).parent().addClass("showchild");
    });

    /* new added */
	$('.expand').each(function () {
		$(this).find('h4').on("click", function () {
			var iteration=$(this).data('iteration')||1
			switch ( iteration) {
				case 1:
					$(this).next('.hidden-content').slideDown(300);
					$(this).addClass('active');
					break;
				
				case 2:
					$(this).next('.hidden-content').slideUp(300);
					$(this).removeClass('active');
					break;
			}
			iteration++;
			if (iteration>2) iteration=1
			$(this).data('iteration',iteration);
		});
	});

	$("section,div").css('background-color', function () {
		return $(this).data('bgcolor');
	});
	
	$("div").css('background-image', function () {
		return $(this).data('bgimage');
	});	

	/* stellar */
	$(window).stellar({
        horizontalScrolling: false,
        verticalOffset: 0,
    });

    /* Typing Text */
    $('.typing-wrap').each( function(){
        var $selector = $(this),
            $id       = $selector.data('id'),
            $cursor   = $selector.data('cursorchar'),
            $speed    = $selector.data('speed'),
            $delay    = $selector.data('delay');

        $('.typed-'+$id).typed({
            stringsElement: $('.typed-strings'),
            typeSpeed: $speed,
            backDelay: $delay,
            loop: true,
            cursorChar: $cursor,            
            contentType: 'html', 
            loopCount: false,
            callback: function () { null; },
            resetCallback: function () { newTyped(); }
        });    
    }); 

	/* Let It Snow */
    $('.let-it-snow').each( function() {
        $(this).letItSnow({
            stickyFlakes: 'lis-flake--js',
            makeFlakes: true,
            sticky: true
        });
    });    

    /* Home YouTube Video */
	$(".player").YTPlayer();

	/* FitVids */
	$(".container").fitVids();

	$(window).load(function() {
		/* --------------------------------------------------
	    * Image Before After
	    * --------------------------------------------------*/
	    $('.twentytwenty-container').each( function(){
	        var $selector       = $(this),
	            before          = $selector.data('before'),
	            after           = $selector.data('after'),
	            before_size     = $selector.data('bsize');          
	        $selector.twentytwenty({                
	            default_offset_pct: before_size, 
	            orientation: 'horizontal', 
	            before_label: before, 
	            after_label: after, 
	            no_overlay: false, 
	            move_slider_on_hover: false, 
	            move_with_handle_only: true, 
	            click_to_move: false,
	        });     
	    }); 
    });

    /*Moving Background Image*/
    $('.moving-home').each( function() {
        var selector = $(this),
            time     = selector.data('time'),
            x        = 0;
        setInterval( function() {
            x -= 1;
            selector.css('background-position', x + 'px 0');
        }, time);
    }); 

    /* --------------------------------------------------
     * magnificPopup
     * --------------------------------------------------*/
    /* OT Image Gallery 1, OT Image Gallery 2 */
    $('.archi-image-gallery').each( function(){
        var $selector = $(this);
        $selector.magnificPopup({
            delegate: '.image-popup',
            type: 'image',
            closeOnContentClick: true,
            closeBtnInside: false,
            fixedContentPos: true,
            mainClass: 'mfp-no-margins mfp-with-zoom mfp-img-mobile',
            image: {
                verticalFit: true,
                titleSrc: function(item) {
                    return item.el.attr('title');
                }
            },
            gallery: {
                enabled: true
            }
        });    
    });

    /* OT Portfolio Gallery, OT Portfolio Gallery 2 */
    $('.gallery-popup-link').magnificPopup({
        delegate: 'a',
        type: 'image',
        closeOnContentClick: true,
        closeBtnInside: false,
        fixedContentPos: true,
        mainClass: 'mfp-no-margins mfp-with-zoom mfp-img-mobile',
        image: {
            verticalFit: true,
            titleSrc: function(item) {
                return item.el.attr('title');
            }
        },
        gallery: {
            enabled: true
        }
    });

    /* OT Masonry Image Gallery */
    $('.masonry-gallery-images-popup').each( function(){
        var $selector = $(this);
        $selector.magnificPopup({
            delegate: '.masonry-image-popup',
            type: 'image',
            closeOnContentClick: true,
            closeBtnInside: false,
            fixedContentPos: true,
            mainClass: 'mfp-no-margins mfp-with-zoom mfp-img-mobile',
            image: {
                verticalFit: true,
                titleSrc: function(item) {
                    return item.el.attr('title');
                }
            },
            gallery: {
                enabled: true
            }
        });    
    });

    /* OT Album Gallery 1, OT Album Gallery 2 */
    $('.album-gallery-popup').each( function(){
        var $selector = $(this);
        $selector.magnificPopup({
            delegate: '.item-popup',
            type: 'image',
            closeOnContentClick: true,
            closeBtnInside: false,
            fixedContentPos: true,
            mainClass: 'mfp-no-margins mfp-with-zoom mfp-img-mobile',
            image: {
                verticalFit: true,
                titleSrc: function(item) {
                    return item.el.attr('title');
                }
            },
            gallery: {
                enabled: true
            }
        });    
    });

    /* Project popup content with next/previous button */
    $('.projects-load-ajax').each( function(){
        var $selector = $(this);
        $selector.magnificPopup({
            delegate: '.simple-ajax-popup-align-top',
            type: 'ajax',
            alignTop: true,
            overflowY: 'scroll',
            fixedContentPos: true,
            callbacks: {
                beforeOpen: function() { $('html').addClass('mfp-helper'); },
                close: function() { $('html').removeClass('mfp-helper'); },
				/* added 23/7/2021 */
				ajaxContentAdded: function() {
					/* Project Image Carousel */
					$('.image__carousel').each( function(index) {
						var selector = $(this);
						selector.owlCarousel({
							singleItem: true,
							navigation : true,
							pagination : true,
							autoHeight : false,
							slideSpeed: 300,
							paginationSpeed: 400,
							autoPlay : selector.data('autoplay'),
							transitionStyle : 'fade',
							navigationText : ['', ''],
							afterInit: makePages,
							afterUpdate: makePages
						});
						function makePages() {
							$.each(this.owl.userItems, function(i) {
								$('.owl-controls .owl-page').eq(i)
									.css({
										'background': 'url(' + $(this).find('img').attr('src') + ')',
										'background-size': 'cover'
									})
							});
						}
					});
                    $('.image__carousel-wrap').each( function(index) {
                        var selector = $(this),
                            sync1    = $(".image__carousel-sync1"),
                            sync2    = $(".image__carousel-sync2"),
                            visible  = selector.data('visible'),
                            autoplay = selector.data('autoplay');

                        sync1.owlCarousel({
                            singleItem      : true,
                            transitionStyle : "fade",
                            autoHeight      : true,
                            slideSpeed      : 300,
                            autoPlay        : autoplay,
                            navigation      : true,
                            pagination      : false,
                            navigationText  : ['', ''],
                            afterAction     : syncPosition,
                            responsiveRefreshRate : 200
                        });
                        
                        sync2.owlCarousel({
                            items             : 5,
                            itemsDesktop      : [1199,4],
                            itemsDesktopSmall : [979,4],
                            itemsTablet       : [768,3],
                            itemsMobile       : [479,2],
                            navigation        : false,
                            pagination        : false,
                            responsiveRefreshRate : 100,
                            afterInit : function(el){
                                el.find(".owl-item").eq(0).addClass("synced");
                            }
                        });

                        function syncPosition(el){
                            var current = this.currentItem;
                            sync2.find(".owl-item").removeClass("synced").eq(current).addClass("synced")
                            if( sync2.data("owlCarousel") !== undefined ){
                                center(current)
                            }
                        }

                        sync2.on("click", ".owl-item", function(e){
                            e.preventDefault();
                            var number = jQuery(this).data("owlItem");
                            sync1.trigger("owl.goTo",number);
                        });

                        function center(number){
                            var sync2visible = sync2.data("owlCarousel").owl.visibleItems;
                            var num = number;
                            var found = false;
                            for(var i in sync2visible){
                              if(num === sync2visible[i]){
                                var found = true;
                              }
                            }

                            if(found===false){
                                if(num>sync2visible[sync2visible.length-1]){
                                    sync2.trigger("owl.goTo", num - sync2visible.length+2)
                                }else{
                                    if(num - 1 === -1){
                                      num = 0;
                                    }
                                    sync2.trigger("owl.goTo", num);
                                }
                            } else if(num === sync2visible[sync2visible.length-1]){
                                sync2.trigger("owl.goTo", sync2visible[1])
                            } else if(num === sync2visible[0]){
                                sync2.trigger("owl.goTo", num-1)
                            }
                        }
                    });
				}
            },
            gallery: {
                enabled: true
            },
        });    
    });

    /* Project popup content without next/previous button */
    $('.single-ajax-popup').magnificPopup({
        type: 'ajax',
        alignTop: true,
        overflowY: 'scroll',
        fixedContentPos: true,
        callbacks: {
            beforeOpen: function() { $('html').addClass('mfp-helper'); },
            close: function() { $('html').removeClass('mfp-helper'); },
			/* added 23/7/2021 */
			ajaxContentAdded: function() {
				/* Project Image Carousel */
				$('.image__carousel').each( function(index) {
					var selector = $(this);
					selector.owlCarousel({
						singleItem: true,
						navigation : true,
						pagination : true,
						autoHeight : false,
						slideSpeed: 300,
						paginationSpeed: 400,
						autoPlay : selector.data('autoplay'),
						transitionStyle : 'fade',
						navigationText : ['', ''],
						afterInit: makePages,
						afterUpdate: makePages
					});
					function makePages() {
						$.each(this.owl.userItems, function(i) {
							$('.owl-controls .owl-page').eq(i)
								.css({
									'background': 'url(' + $(this).find('img').attr('src') + ')',
									'background-size': 'cover'
								})
						});
					}
				});
                $('.image__carousel-wrap').each( function(index) {
                        var selector = $(this),
                            sync1    = $(".image__carousel-sync1"),
                            sync2    = $(".image__carousel-sync2"),
                            visible  = selector.data('visible'),
                            autoplay = selector.data('autoplay');

                        sync1.owlCarousel({
                            singleItem      : true,
                            transitionStyle : "fade",
                            autoHeight      : true,
                            slideSpeed      : 300,
                            autoPlay        : autoplay,
                            navigation      : true,
                            pagination      : false,
                            navigationText  : ['', ''],
                            afterAction     : syncPosition,
                            responsiveRefreshRate : 200
                        });
                        
                        sync2.owlCarousel({
                            items             : 5,
                            itemsDesktop      : [1199,4],
                            itemsDesktopSmall : [979,4],
                            itemsTablet       : [768,3],
                            itemsMobile       : [479,2],
                            navigation        : false,
                            pagination        : false,
                            responsiveRefreshRate : 100,
                            afterInit : function(el){
                                el.find(".owl-item").eq(0).addClass("synced");
                            }
                        });

                        function syncPosition(el){
                            var current = this.currentItem;
                            sync2.find(".owl-item").removeClass("synced").eq(current).addClass("synced")
                            if( sync2.data("owlCarousel") !== undefined ){
                                center(current)
                            }
                        }

                        sync2.on("click", ".owl-item", function(e){
                            e.preventDefault();
                            var number = jQuery(this).data("owlItem");
                            sync1.trigger("owl.goTo",number);
                        });

                        function center(number){
                            var sync2visible = sync2.data("owlCarousel").owl.visibleItems;
                            var num = number;
                            var found = false;
                            for(var i in sync2visible){
                              if(num === sync2visible[i]){
                                var found = true;
                              }
                            }

                            if(found===false){
                                if(num>sync2visible[sync2visible.length-1]){
                                    sync2.trigger("owl.goTo", num - sync2visible.length+2)
                                }else{
                                    if(num - 1 === -1){
                                      num = 0;
                                    }
                                    sync2.trigger("owl.goTo", num);
                                }
                            } else if(num === sync2visible[sync2visible.length-1]){
                                sync2.trigger("owl.goTo", sync2visible[1])
                            } else if(num === sync2visible[0]){
                                sync2.trigger("owl.goTo", num-1)
                            }
                        }
                    });
			}
        },
    });
    
    /* popup youtube, video, gmaps -> use in OT Video Tour */
    $('.popup-youtube').magnificPopup({
        disableOn: 700,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false,
    });
    
	/* --------------------------------------------------
	* owlCarousel
	* --------------------------------------------------*/
	/*Gallery Post*/
	$('.slider-post').each( function() {
        var selector = $(this);
        selector.owlCarousel({
        	items : 1,
	        autoplay: selector.data('autoplay'),
	        slideSpeed : selector.data('speed'),
	        paginationSpeed : selector.data('navspeed'),
	        rewindSpeed : selector.data('rewinspeed'),
	        singleItem:true,
	        transitionStyle : selector.data('transition'),
        });
    });    

	/* Client Logo */
    $('.client__slides').each( function() {
        var selector = $(this);
        selector.owlCarousel({
        	items : selector.data('visible'),
		    itemsDesktop : [1199, 4],
	        itemsDesktopSmall : [979, 3],
	        itemsTablet : [768, 3],
	        itemsTabletSmall : [767, 2],
	        itemsMobile : [479, 1],
		    navigation : false,
			pagination : false,
			autoPlay : true
        });
    });

    /* Portfolio Carousel Style */
    $('.portfolio__carousel').each( function() {
        var selector = $(this);
        selector.owlCarousel({
        	items : selector.data('visible'),
	   		itemsDesktop : [1199,3],
			itemsDesktopSmall : [979,2],
			itemsTablet : [768, 2],
	        itemsTabletSmall : false,
	        itemsMobile : [479, 1],
	        navigation: true,
	        pagination: false,
	        autoPlay : selector.data('autoplay'),
	   		navigationText : ['', ''],
        });
    });

    /* Testimonials Carousel */
    $('.testimonial__carousel').each( function() {
        var selector = $(this);
        selector.owlCarousel({
        	items : selector.data('visible'),
			itemsDesktop : [1199,2],
			itemsDesktopSmall : [980,2],
		    itemsTablet: [768,1],
		    itemsTabletSmall: false,
		    itemsMobile : [479,1],
		    navigation : false,
			autoHeight : selector.data('autoheight'),
			autoPlay : selector.data('autoplay'),
			slideSpeed : selector.data('speed'),
	        paginationSpeed : selector.data('navspeed'),
	        rewindSpeed : selector.data('rewinspeed'),
	   		navigationText : ['', ''],
        });
    });    

    /* Testimonials Carousel Group */
    $('.testimonial__carousel_group').each( function() {
        var selector = $(this);
        selector.owlCarousel({
        	items      : 1,
			singleItem :true,
		    navigation : false,
			autoHeight : selector.data('autoheight'),
			autoPlay   : selector.data('autoplay'),
			slideSpeed : selector.data('speed'),
	        paginationSpeed : selector.data('navspeed'),
	        rewindSpeed : selector.data('rewinspeed'),
	   		navigationText : ['', ''],
        });
    });

    /* Project Image Carousel */
    $('.image__carousel').each( function() {
        var selector = $(this);
        selector.owlCarousel({
        	singleItem : true,
	      	navigation : true,
	   		pagination : true,
	   		autoHeight : false,
	   		slideSpeed : 300,
			paginationSpeed : 400,
			autoPlay : selector.data('autoplay'),
			transitionStyle : 'fade',
	   		navigationText  : ['', ''],
			afterInit: makePages,
			afterUpdate: makePages
        });
        function makePages() {
			$.each(this.owl.userItems, function(i) {
				$('.owl-controls > .owl-pagination > .owl-page').eq(i)
					.css({
						'background': 'url(' + $(this).find('img').attr('src') + ')',
						'background-size': 'cover'
					})
			});
		}
    });

    $('.image__carousel-wrap').each( function() {
        var selector = $(this),
            sync1    = $(".image__carousel-sync1"),
            sync2    = $(".image__carousel-sync2"),
            visible  = selector.data('visible'),
            autoplay = selector.data('autoplay');

        sync1.owlCarousel({
            singleItem      : true,
            transitionStyle : "fade",
            autoHeight      : true,
            slideSpeed      : 300,
            autoPlay        : autoplay,
            navigation      : true,
            pagination      : false,
            navigationText  : ['', ''],
            afterAction     : syncPosition,
            responsiveRefreshRate : 200
        });
        
        sync2.owlCarousel({
            items             : 5,
            itemsDesktop      : [1199,4],
            itemsDesktopSmall : [979,4],
            itemsTablet       : [768,3],
            itemsMobile       : [479,2],
            navigation        : false,
            pagination        : false,
            responsiveRefreshRate : 100,
            afterInit : function(el){
                el.find(".owl-item").eq(0).addClass("synced");
            }
        });

        function syncPosition(el){
            var current = this.currentItem;
            sync2.find(".owl-item").removeClass("synced").eq(current).addClass("synced")
            if( sync2.data("owlCarousel") !== undefined ){
                center(current)
            }
        }

        sync2.on("click", ".owl-item", function(e){
            e.preventDefault();
            var number = jQuery(this).data("owlItem");
            sync1.trigger("owl.goTo",number);
        });

        function center(number){
            var sync2visible = sync2.data("owlCarousel").owl.visibleItems;
            var num = number;
            var found = false;
            for(var i in sync2visible){
              if(num === sync2visible[i]){
                var found = true;
              }
            }

            if(found===false){
                if(num>sync2visible[sync2visible.length-1]){
                    sync2.trigger("owl.goTo", num - sync2visible.length+2)
                }else{
                    if(num - 1 === -1){
                      num = 0;
                    }
                    sync2.trigger("owl.goTo", num);
                }
            } else if(num === sync2visible[sync2visible.length-1]){
                sync2.trigger("owl.goTo", sync2visible[1])
            } else if(num === sync2visible[0]){
                sync2.trigger("owl.goTo", num-1)
            }
        }
    });

    /* Blog Carousel */
    $('.blog-carousel').each( function() {
        var selector = $(this);
        selector.owlCarousel({
        	items : selector.data('visible'),
			itemsDesktop : [1199, 3],
	        itemsDesktopSmall : [979, 2],
	        itemsTablet : [768, 2],
	        itemsTabletSmall : [767, 2],
	        itemsMobile : [479, 1],
		    navigation : false,
			pagination : true,			
			autoPlay : selector.data('autoplay'),
			slideSpeed : selector.data('speed'),
	        paginationSpeed : selector.data('navspeed'),
	        rewindSpeed : selector.data('rewinspeed'),
        });
    });

	$('.text-slider').each( function() {
        var selector = $(this);
        selector.owlCarousel({
            items : 1,
			singleItem:true,	
		    navigation: false,
			pagination: false,
			mouseDrag: false,
			touchDrag: false,
			autoPlay: 4000, 
			transitionStyle: "fade"
        });
    });

	/* Simple Slider */
    $('.simple__slider').each( function() {
        var selector = $(this);
        selector.owlCarousel({
            items: 1,
	        singleItem: true,
	        navigation: false,
	        pagination: false,
	        mouseDrag: false,
	        touchDrag: false,
	        autoPlay: 4000,
	        transitionStyle: "fade"
        });
    });

    $('.carousel-single-navi').each( function () {
        var $next    = $(this).data('next');
        var $prev    = $(this).data('prev');        
        $(this).owlCarousel({
            items: 1,
	        singleItem: true,
	        navigation: true,
	        navigationText : [$prev, $next],
	        pagination: false,
	        mouseDrag: false,
	        touchDrag: false,
	        transitionStyle: "fade"
        });
    }); 

    /* logo carousel hover */
	$(".client__slides img").on("mouseenter", function () {
	 	$(this).fadeTo(150,.5);
	}).on("mouseleave", function () {
	 	$(this).fadeTo(150,1);	 
  	});

  	$('.process-carousel-wrap').each( function() {
  		var selector = $(this),
            sync1    = $(".process-sync1"),
            sync2    = $(".process-sync2"),
            visible  = selector.data('visible');

		sync1.owlCarousel({
			singleItem : true,
			transitionStyle : "fade",
			autoHeight : true,
			slideSpeed : 1500,
			navigation: false,
			pagination:false,
			afterAction : syncPosition,
			responsiveRefreshRate : 200
		});
		
		sync2.owlCarousel({
			items : visible,
			itemsDesktop      : [1199,3],
			itemsDesktopSmall     : [979,3],
			itemsTablet       : [768,2],
			itemsMobile       : [479,2],
			pagination:false,
			responsiveRefreshRate : 100,
			afterInit : function(el){
				el.find(".owl-item").eq(0).addClass("synced");
			}
		});

		function syncPosition(el){
			var current = this.currentItem;
			sync2.find(".owl-item").removeClass("synced").eq(current).addClass("synced")
			if( sync2.data("owlCarousel") !== undefined ){
				center(current)
			}
		}

		sync2.on("click", ".owl-item", function(e){
			e.preventDefault();
			var number = jQuery(this).data("owlItem");
			sync1.trigger("owl.goTo",number);
		});

		function center(number){
			var sync2visible = sync2.data("owlCarousel").owl.visibleItems;
			var num = number;
			var found = false;
			for(var i in sync2visible){
			  if(num === sync2visible[i]){
				var found = true;
			  }
			}

			if(found===false){
				if(num>sync2visible[sync2visible.length-1]){
					sync2.trigger("owl.goTo", num - sync2visible.length+2)
				}else{
					if(num - 1 === -1){
					  num = 0;
					}
					sync2.trigger("owl.goTo", num);
				}
			} else if(num === sync2visible[sync2visible.length-1]){
				sync2.trigger("owl.goTo", sync2visible[1])
			} else if(num === sync2visible[0]){
				sync2.trigger("owl.goTo", num-1)
			}
		}
  	});

	/*Portfolio Filter*/  
	$('.testimonial-masonry').isotope({
		itemSelector: '.item',		
		animationEngine : 'css',	
		masonry: {
            columnWidth: '.item-testi-grid-sizer'
        },	
	});	

	$('.services-masonry').isotope({
		itemSelector: '.item',	
		animationEngine : 'css',	
		masonry: {
            columnWidth: '.item-service-grid-sizer'
        },		
	});	

    $('.projects-grids').isotope({
        itemSelector: '.grid-items',  
        animationEngine : 'css',    
        masonry: {
            columnWidth: '.grid-sizers'
        },      
    }); 

    $('.archi-image-gallery').isotope({
        itemSelector: '.project-item',  
        animationEngine : 'css',    
        masonry: {
            columnWidth: '.project-item-sizer'
        },      
    });

    /*Portfolio Filter*/
    $('.projects-grid-wrapper').each( function(){
        var $container = $(this).find('.projects-grid'); 
        $container.isotope({ 
            itemSelector : '.project-item', 
            animationEngine : 'css',
            masonry: {
                columnWidth: '.project-item-sizer'
            }
        });

        var $optionSets  = $(this).find('.project_filters'),
            $optionLinks = $optionSets.find('a');

        $optionLinks.on('click', function(){
            var $this = $(this);

            if ( $this.hasClass('selected') ) {
                return false;
            }
            var $optionSet = $this.parents('.project_filters');
                $optionSet.find('.selected').removeClass('selected');
                $this.addClass('selected');

            var selector = $(this).attr('data-filter');
                $container.isotope({ 
                    filter: selector 
                });
            return false;
        });
    });

    if( $('#projects_grid').length > 0 ){
        var $container = $('#projects_grid');
        $container.isotope({ 
            /*set itemSelector so .grid-sizer is not used in layout*/
            itemSelector: '.project-item',
            animationEngine : 'css',
            masonry: {
                /*use element for option*/
                columnWidth: '.project-item-sizer'
            }
        });

        $('.project_filters a').click(function(){
            var $this = $(this);

            if ( $this.hasClass('selected') ) {
                return false;
            }
            var $optionSets = $this.parents('.project_filters');
                $optionSets.find('.selected').removeClass('selected');
                $this.addClass('selected');

            var selector = $(this).attr('data-filter');
                $container.isotope({ 
                    filter: selector 
                });
            return false;
        });
    }; 

    /* Royal Preloader */
    if ( $('#royal_preloader').length ) {
        var $selector       = $('#royal_preloader'),
            $width          = $selector.data('width'),
            $height         = $selector.data('height'),
            $color          = $selector.data('color'),
            $bgcolor        = $selector.data('bgcolor'),
            $logourl        = $selector.data('url');
        
        Royal_Preloader.config({
            mode           : 'logo',
            logo           : $logourl,
            logo_size      : [$width, $height],
            showProgress   : true,
            showPercentage : true,
            text_colour: $color,
            background:  $bgcolor,
        });
    } 

    if ( $('#back-to-top').length ) {
        var scrollTrigger = 500,
            backToTop = function () {
                var scrollTop = $(window).scrollTop();
                if (scrollTop > scrollTrigger) {
                    $('#back-to-top').addClass('show');
                } else {
                    $('#back-to-top').removeClass('show');
                }
            };
        backToTop();
        $(window).on('scroll', function () {
            backToTop();
        });
        $('#back-to-top').on('click', function (e) {
            e.preventDefault();
            $('html,body').animate({
                scrollTop: 0
            }, 700);
        });
    }

})(jQuery);