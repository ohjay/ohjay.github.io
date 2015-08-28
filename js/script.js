// Collapse navbar after a selection is made (on mobile)
if ($(window).width() <= 480 || $(window).height() <= 480) {
    $('.nav a').on('click', function(){
        $(".navbar-toggle").click();
    });
}
