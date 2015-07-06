	(function($) {
	
	$.fn.popup = function(opt) {
	
	var settings, createpopup, body, closepopup;
	
		 settings = $.extend({
		 'popup': 'jquery-popup',
		 'close': 'jquery-popup-close',
		 'closeText': '',
		 'shade': 'jquery-popup-shade'
		 }, opt);
		 
		 body = $('body');
		 
		 closepopup = function(popup, shade) {
		   popup.remove();
		   shade.remove();
		 
		 };
		 
		 createpopup = function(data) {
            var shade, close, popup;		 
		 
		    shade = $('<div />', {
			 class: settings.shade
			}).on('click', function() { 
			// close popup and shade 
			closepopup(popup,shade);
			
			});
			
			close = $('<a />', {
			 text: settings.closeText,
			 class: settings.close,
			 href: '#'
			}).on('click', function() {
			 //close popup and shade
			 closepopup(popup,shade);
			 
			});
			
			popup = $('<div />', {
			 html: data,
			 class: settings.popup
			}).append(close);
			

			body.prepend(shade, popup);
		 };
		 
		 
		 this.on('click', function() {
		   var self = $(this);
		   //console.log(self);
		   
		   $.ajax({
		    url: self.data('content'),
			type: 'get',
			cache: false
		    }).done(function(data) {
			 createpopup(data);
			}).error(function() {
			 createpopup('<h1 align="center">Feature coming soon!</h1>');
			});

		 
		 });
		};
	})(jQuery);