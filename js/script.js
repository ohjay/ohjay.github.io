// Collapse navbar after a selection is made (on mobile)
if ($(window).width() <= 480 || $(window).height() <= 480) {
    $('.nav a').on('click', function(){
        $(".navbar-toggle").click();
    });
}

// Trigger CSS animations when the element in question is scrolled to
$(window).scroll(function() {
	$('.info-text').each(function(){
	var imagePos = $(this).offset().top;

	var topOfWindow = $(window).scrollTop();
		if (imagePos < topOfWindow + 400) {
			$(this).addClass("slideLeft");
		}
	});
});

$(window).scroll(function() {
	$('.transp-box-hidden').each(function(){
	var imagePos = $(this).offset().top;

	var topOfWindow = $(window).scrollTop();
		if (imagePos < topOfWindow + 400) {
			$(this).addClass("slideLeft");
		}
	});
});
