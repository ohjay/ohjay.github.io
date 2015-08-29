// Collapse navbar after a selection is made (on mobile)
if ($(window).width() <= 480 || $(window).height() <= 480) {
    $('.nav a').on('click', function(){
        $(".navbar-toggle").click();
    });
}

// Trigger CSS animations when the element in question is scrolled to
var addAnimation = function() {
	var imagePos = $(this).offset().top;
	var topOfWindow = $(window).scrollTop();
    
	if (imagePos < topOfWindow + 400 || $(window).scrollTop() + $(window).height() > $(document).height() - 50) {
		$(this).addClass("slideLeft");
	}
}

$(window).scroll(function() {
	$('.info-text').each(addAnimation);
    $('.transp-box-hidden').each(addAnimation);
    $('.transp-box-proj').each(addAnimation);
});
