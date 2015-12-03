var addLinks = function() {
    $('#skip-button').remove();
    $('.pipe').text(' | ');
    $('#portfolio').text('Portfolio');
    $('#blog').text('Blog');
    $('#cs61a').text('CS 61A');
};

$(document).ready(function() {
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
    
    // The secret page navigation option
    $(document).keypress(function(evt) {
        base = document.location.origin;
        switch (evt.charCode) {
            case 'b'.charCodeAt(): // blog
                document.location.href = base + '/blog';
                break;
            case 'c'.charCodeAt(): // CS 61A
                document.location.href = base + '/cs61a';
                break;
            case 'p'.charCodeAt(): // portfolio
                document.location.href = base + '/portfolio';
                break;
        }
    });
});
