function addColons() {
    var df = parseInt($(".container").css('font-size'), 10) * 0.65;
    var width = $('.container').width();
    $('.below-mh-subtitle').text(": " + Array(Math.floor(width / df)).join(' :'));
}

addColons();
$(window).resize(function() {
    addColons();
});

// The secret page navigation option (aka hotkeys!)
$(document).keypress(function(evt) {
    base = document.location.origin;
    switch (evt.charCode) {
        case 'b'.charCodeAt(): // blog root
            document.location.href = base + '/blog';
            break;
        case 'c'.charCodeAt():
            document.location.href = base + '/cs61a';
            break;
        case 'g'.charCodeAt():
            document.location.href = base + '/graphics';
            break;
        case 'i'.charCodeAt():
            document.location.href = base;
            break;
        case 'p'.charCodeAt():
            document.location.href = base + '/portfolio';
            break;
    }
});
