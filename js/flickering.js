const NUM_HASHES = HASHES.length;

function verify(id, accessCode) {
    var token = id.replace(/\s+/g, '').toLowerCase() + accessCode;
    for (var i = 0; i < NUM_HASHES; ++i) {
        var result = CryptoJS.AES.decrypt(HASHES[i], token).toString(CryptoJS.enc.Latin1);
        if (/^https?:\/\/[^\s]+$/.test(result)) {
            window.location = result;
            return true;
        }
    }
    
    // Display denial
    $("#lit-header").removeClass("power-on");
    document.getElementById("go").className = "denied";
    document.getElementById("go").value = "Access Denied";
    
    return false;
}

$(document).ready(function() {
    var state = false;
    var numAttempts = 0;

    $('#access-panel').on('submit', function(evt) {
        evt.preventDefault();
        if (!state && numAttempts < 10) {
            state = true;
            $("#lit-header").addClass("power-on");
            document.getElementById("go").className = "";
            document.getElementById("go").value = "Verifying...";
            
            numAttempts += 1;
            setTimeout(function() {
                verify($('#name').val(), $('#password').val());
                state = false;
            }, 2000);
        }
    });
});
