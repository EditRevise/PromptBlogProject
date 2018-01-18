document.addEventListener('DOMContentLoaded', function () {
    var header = document.getElementById('page-header');
    var b = 0, // Header color value for blue
        bStep = 1, // How much to change on every step
        bCoefficientAdjust = -1; // How much to change the step value when limit reached
    var MAX_B = 255, // Max value for blue
        MIN_B = 0, // Min value for blue
        INTERVAL = 10; // Interval duration in ms

    /** When run incrementally, causes the header color to oscillate. */
    function stepBlue () {
        b += bStep;
        if (b === MAX_B || b === MIN_B) {
            bStep *= bCoefficientAdjust;
        }
        header.style.color = 'rgb(128,128,' + b.toString() + ')';
    }
    setInterval(stepBlue, INTERVAL);
});

// TODO: Put code in this file or other files as you see fit.
// (You probably want to remove the oscillating header color, too!)
