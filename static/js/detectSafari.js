var is_safari = userAgentString.indexOf("Safari") > -1;
if ((chromeAgent) && (is_safari)) is_safari = false;

window.onload = function(event) {
    if (is_safari) alert('For best experience, please use Google Chrome')
}