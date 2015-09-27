var addLinks = function() {
    $('#skip-button').remove();
    $('.pipe').text(' | ');
    $('#portfolio').text('Portfolio');
    $('#blog').text('Blog');
    $('#cs61a').text('CS61A');
};

$(document).ready(function() {
    $('.animated-text').typed({
        strings: [
            "Don't you miss the quiet of a simpler age?", 
            "I know I do.", 
            "Here you can take a break from the chaos and clutter of life.", 
            "Just pause for a bit. What's the harm?",
            "Close your eyes –",
            "Try to think about something happy.",
            "And then...",
            "When you're totally ready... take a deep breath and move on."],
        typeSpeed: 42,
        backDelay: 500,
        showCursor: false,
        callback: addLinks
    });
    
    $('#skip-button').click(function() {
        $('span.animated-text').replaceWith(
            "<span>When you're totally ready... take a deep breath and move on.</span>"
        );
        addLinks();
    });
});
