if ($(window).width() <= 480 || $(window).height() <= 480) {
    /* Mobile-specific code */
    // Remove the "nav navbar-nav" classes from the social link icons
    $('#links').removeClass('nav navbar-nav');
            
    // Replace the footer text with a simpler statement
    $('#footer-text p').text('Copyright Owen Jow 2015');
    
    // Collapse navbar after a selection is made
    $('.nav a').on('click', function(){
        $(".navbar-toggle").click();
    });
} else {
    /* Non-mobile specific code */
    var addAnimation = function() {
    	var imagePos = $(this).offset().top;
    	var topOfWindow = $(window).scrollTop();
    
    	if (imagePos < topOfWindow + 400 || $(window).scrollTop() + $(window).height() > $(document).height() - 50) {
    		$(this).addClass('slideLeft');
    	}
    };

    // Trigger CSS animations when the element in question is scrolled to
    $(window).scroll(function() {
    	$('.info-text').each(addAnimation);
        $('.transp-box-hidden').each(addAnimation);
    });
}

/* Fun for the whole family */
// Reveal hidden text upon superscript click
$('#superscript').click(function() {
    $('#hidden-footnote').addClass('fadeIn');
});
