$(document).ready(function() {
    var typed = '';
    var hash = 'U2FsdGVkX1/0yqSyURFbIDOIvJ5TuGPskR76xBbrDEXCBnoXnUTxmVdsmgHS3Hiqef/CdbAi11/P4T4Z7SJObw==';
    var numAttempts = 0;
    var result = null;

    $(window).bind("keypress", function(evt) {
        if (typed.length < 65 && numAttempts < 65) {
            typed += String.fromCharCode(evt.keyCode);
            result = CryptoJS.AES.decrypt(hash, typed).toString(CryptoJS.enc.Latin1);
            if (/^http:[a-z\.\/]{10,}\/$/.test(result)) {
                window.location = result;
            } else if (Math.random() < 0.005) {
                window.location = '/restricted/access';
            }
            numAttempts += 1;
        } else if (Math.random() < 0.01) {
            window.location = '/restricted/access';
        }
    });
});
