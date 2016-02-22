/* 
 * Thanks to Chris Buttery for the following fade code!
 * http://www.chrisbuttery.com/articles/fade-in-fade-out-with-javascript/
 */
function fadeIn(el, display) {
    el.style.opacity = 0;
    el.style.display = display || 'block';

    (function fade() {
        var val = parseFloat(el.style.opacity);
        if (!((val += 0.01) > 1)) {
            el.style.opacity = val;
            requestAnimationFrame(fade);
        }
    })();
}

var el = document.querySelector('.js-fade');
fadeIn(el, 'inline');
