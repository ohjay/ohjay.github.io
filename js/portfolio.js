function updateContent(width) {
    if (width <= 1000) {
        // Replace the footer text with a simpler statement
        $('#footer-text p').text('{ Copyright Owen Jow 2016 }');
    } else {
        $('#footer-text p').html(
            '<i>Built from scratch by... well, you can probably guess. '
            + 'Who else would make an entire website about Owen Jow?</i><br>&copy; Owen Jow 2016<br><br>'
            + '{ Background starring my good friend <a href="/images/kirby_cap.png" style="text-decoration: none" '
            + 'target="_blank">Kirby</a> }'
        );
    }

    if (width <= 767) {
        // Remove the "nav navbar-nav" classes from the social link icons
        $('#links').removeClass('nav navbar-nav');
    
        // Collapse navbar after a selection is made
        $('.nav a').on('click', function() {
            $(".navbar-toggle").click();
        });
    } else {
        $('#links').addClass('nav navbar-nav');
    }
}

$(document).ready(function() {
    var width = $(window).width();
    if (width > 480) {
        /* Non-mobile specific code */
        var addEntryAnimation = function() {
            var pos = $(this).offset().top;
            var scrollTop = $(window).scrollTop();
            
            if (pos < scrollTop + 625 || scrollTop + $(window).height() > $(document).height() - 50) {
                $(this).fadeTo(750, 1, 'linear'); // 750 ms animation
            }
        };

        // Trigger CSS animations when the element in question is scrolled to
        $(window).scroll(function() {
            $('.transp-box-hidden').each(addEntryAnimation);
        });
    }
    
    updateContent(width);
    $(window).resize(function() {
        updateContent($(window).width());
    });
    
    /* Fun for the whole family */
    // Reveal hidden text upon superscript click
    $('#superscript1').click(function() {
        $('#replace1').text(' (every once in a while)');
    });

    $('#superscript2').click(function() {
        $('#replace2').text(' (all the time)');
    });
});
