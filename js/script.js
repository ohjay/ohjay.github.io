var moveForce = 35; // max popup movement in pixels
var rotateForce = 25; // max popup rotation in degrees

$(document).mousemove(function(e) {
    var docX = $(document).width();
    var docY = $(document).height();
    
    var moveX = (e.pageX - docX / 2) / (docX / 2) * -moveForce;
    var moveY = (e.pageY - docY / 2) / (docY / 2) * -moveForce;
    
    var rotateY = (e.pageX / docX * rotateForce * 2) - rotateForce;
    var rotateX = -((e.pageY / docY * rotateForce * 2) - rotateForce);
    
    $('.popup')
        .css('left', moveX + 'px')
        .css('top', moveY + 'px')
        .css('transform', 'rotateX('+rotateX + 'deg) rotateY('+rotateY + 'deg)');
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
        case 'g'.charCodeAt(): // graphics
            document.location.href = base + '/graphics';
            break;
        case 'p'.charCodeAt(): // portfolio
            document.location.href = base + '/portfolio';
            break;
    }
});
