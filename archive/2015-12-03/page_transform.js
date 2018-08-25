$(document).ready(function() {
    var pageTransform = function() {
        if ($(window).width() <= 480) {
            $('p').css({"width": "90%", "margin-left": "auto", "margin-right": "auto"})
                  .html('. . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br><br>'
                      + "Hi! Bad news: you've arrived at the landing page for Owen Jow's website. "
                      + "Since that probably wasn't your intended destination, I've constructed "
                      + "this as a buffer against the gruesome remainder of this site's contents. "
                      + "If you possess any vestige of control over your mental faculties, you'll turn back now.<br><br>"
                      + "That was your final warning.<br><br>"
                      + '<a href="portfolio" id="portfolio">Portfolio</a>&nbsp;&nbsp;|&nbsp;&nbsp;'
                      + '<a href="blog" id="blog">Blog</a>&nbsp;&nbsp;|&nbsp;&nbsp;'
                      + '<a href="cs61a" id="cs61a">CS 61A</a><br>'
                      + '. . . . . . . . . . . . . . . . . . . . . . . . . . . . .');
        } else {
            $('p').html('___________________________________________________________<br><br>'
                    + 'Hi! You\'ve reached the landing page for Owen Jow\'s website.<br>'
                    + '<span class="animated-text"></span><br><br>'
                    + '<a href="portfolio" id="portfolio"></a>&nbsp;<span class="pipe"></span>&nbsp;'
                    + '<button type="button" id="skip-button">Look, just cut to the chase.</button>'
                    + '<a href="blog" id="blog"></a>&nbsp;<span class="pipe"></span>&nbsp;'
                    + '<a href="cs61a" id="cs61a"></a><br>'
                    + '___________________________________________________________');
        }
    };
        
    pageTransform();
    $(window).resize(function() {
        pageTransform();
    });
});
