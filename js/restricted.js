$(document).ready(function() {
    var typed = '';
    var hash = 'k2U2FsdGVkX1+cBoCEYZoj9dMWVmR1cxPbMaU0dMfPrUlbzeAif9y8B0dKhkzPlXpjDgLIh8ILL/QcjX5O9OG/fg==';
    var numAttempts = 0;
    var result = null;
                    
    $(window).bind("keypress", function(evt) {
        if (typed.length < 65 && numAttempts < 65) {
            typed += String.fromCharCode(evt.keyCode);
            result = CryptoJS.AES.decrypt(hash, typed).toString(CryptoJS.enc.Latin1);
            if (/^http:[a-z\.\/]{10,}\/$/.test(result)) {
                window.location = result;
            }
            numAttempts += 1;
        }
    });
});
