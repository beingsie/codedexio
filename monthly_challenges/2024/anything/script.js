// Do it
window.onload = function() {
    // Get elements
    const challengeTag = document.getElementById("challengeTag");
    const miniDino = document.getElementById("miniDino");
    const anythingHeading = document.getElementById("mainHeading");
    const mainHeadingArrow = document.getElementById("mainHeadingArrow");

    // Add fadeInBounce animation through class to tag
    challengeTag.classList.add("bounceUp");

    setTimeout(() => {
        miniDino.classList.add("bounceUpDown");
        miniDino.style.opacity = "1";
    }, 140);

    setTimeout(() => {
        anythingHeading.classList.add("rotate-in-down-left")
    }, 145);
}