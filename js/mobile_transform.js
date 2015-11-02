var mobileTransform = function() {
    if ($(window).width() <= 480) {
        $("p").css({"width": "90%", "margin-left": "auto", "margin-right": "auto"})
              .html('. . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br><br>'
                  + "Hi! Bad news: you've arrived at the landing page for Owen Jow's website. "
                  + "Since that probably wasn't your intended destination, I've constructed "
                  + "this as a buffer against the gruesome remainder of this site's contents. "
                  + "If you possess any vestige of control over your mental facilities, you'll turn back now.<br><br>"
                  + "That was your final warning.<br><br>"
                  + '<a href="portfolio" id="portfolio">Portfolio</a>&nbsp;&nbsp;|&nbsp;&nbsp;'
                  + '<a href="blog" id="blog">Blog</a>&nbsp;&nbsp;|&nbsp;&nbsp;'
                  + '<a href="cs61a" id="cs61a">CS 61A</a><br>'
                  + '. . . . . . . . . . . . . . . . . . . . . . . . . . . . .');
    }
};
        
mobileTransform();
$(window).resize(function() {
    mobileTransform();
});
