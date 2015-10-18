var addLinks = function() {
    $('#skip-button').remove();
    $('.pipe').text(' | ');
    $('#portfolio').text('Portfolio');
    $('#blog').text('Blog');
    $('#cs61a').text('CS 61A');
};

var mobileTransform = function() {
    if ($(window).width() <= 480) {
        $("p").css({"width": "90%", "margin-left": "auto", "margin-right": "auto"})
              .html('. . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br><br>'
                  + "Hi! Bad news: you've arrived at the landing page for Owen Jow's website. "
                  + "Since that probably wasn't your intended destination, I've constructed "
                  + "this as a buffer against the gruesome remainder of this site's contents. "
                  + "If you possess any vestige of control over your mental facilities, you'll turn back now.<br><br>"
                  + "That was your final warning.<br><br>"
                  + '<a href="portfolio.html" id="portfolio">Portfolio</a>&nbsp;&nbsp;|&nbsp;&nbsp;'
                  + '<a href="blog.html" id="blog">Blog</a>&nbsp;&nbsp;|&nbsp;&nbsp;'
                  + '<a href="cs61a.html" id="cs61a">CS 61A</a><br>'
                  + '. . . . . . . . . . . . . . . . . . . . . . . . . . . . .');
    }
};

$(document).ready(function() {
    mobileTransform();
    $(window).resize(function() {
        mobileTransform();
    });
    
    $('.animated-text').typed({
        strings: [
            "Don't you miss the quiet of a simpler age?", 
            "I know I do.", 
            "Here you can take a break from the chaos and clutter of life.",
            "Just pause for a bit. What's the harm?",
            "After all, you're the most talented, most interesting...",
            "...most EXTRAORDINARY person in the universe.", // - Emmet, the Lego Movie
            "And you can stay here as long as you want, my friend.",
            "When you're totally ready... buckle up and take off again."],
        typeSpeed: 42,
        backDelay: 500,
        showCursor: false,
        callback: addLinks
    });
    
    $('#skip-button').click(function() {
        $('span.animated-text').replaceWith(
            "<span>When you're totally ready... buckle up and take off again.</span>"
        );
        addLinks();
    });
});
