if ($(window).width() <= 480) {
    /* Mobile-specific code */
    // Remove the "nav navbar-nav" classes from the social link icons
    $('#links').removeClass('nav navbar-nav');
            
    // Replace the footer text with a simpler statement
    $('#footer-text p').text('Copyright Owen Jow 2015');
    
    // Remove some mobile-unnecessary text
    $('.pull-right').text('');
    
    // Collapse navbar after a selection is made
    $('.nav a').on('click', function(){
        $(".navbar-toggle").click();
    });
} else {
    /* Non-mobile specific code */
    var addEntryAnimation = function() {
    	var pos = $(this).offset().top;
    	var scrollTop = $(window).scrollTop();
        
    	if (pos < scrollTop + 625 || scrollTop + $(window).height() > $(document).height() - 50) {
    		// $(this).addClass('slideLeft');
            $(this).fadeTo(750, 1, 'linear'); // 750 ms animation
    	}
    };

    // Trigger CSS animations when the element in question is scrolled to
    $(window).scroll(function() {
        $('.transp-box-hidden').each(addEntryAnimation);
    });
}

/* Fun for the whole family */
// Reveal hidden text upon superscript click
$('#superscript0').click(function() {
    $('#hidden-footnote').addClass('fadeIn');
});

$('#superscript1').click(function() {
    $('#replace1').text(' (every once in a while)');
});

$('#superscript2').click(function() {
    $('#replace2').text(' (all the time)');
});
