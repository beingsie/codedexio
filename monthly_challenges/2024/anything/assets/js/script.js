// Do it
window.onload = function() {
    // Get elements
    const challengeTag = document.getElementById("challengeTag");
    const miniDino = document.getElementById("miniDino");
    const anythingHeading = document.getElementById("mainHeading");

    // Add fadeInBounce animation through class to tag
    challengeTag.classList.add("bounceUp");
    challengeTag.style.opacity = "1"

    setTimeout(() => {
        miniDino.classList.add("bounceUpDown");
        miniDino.style.opacity = "1";
    }, 140);

    setTimeout(() => {
        anythingHeading.classList.add("rotate-in-down-left")
    }, 145);
}

const closeBtn = document.getElementById("closeBtn");
const modalWindow = document.getElementById("modalWindow");
const modalContent = document.getElementById("modalContent");
const whatLink = document.getElementById("whatLink");

whatLink.addEventListener("click", openModal);

function openModal(event) {
    // Prevent from reloading upon submission/clicking button
    event.preventDefault();
    // Add classes
    modalWindow.classList.add("active");
    // 0.14 second delay before adding classes
    setTimeout(() => {
        modalContent.classList.add("bounceIn");
    }, 140);
}
// On click run function
closeBtn.addEventListener("click", closeModal);

function closeModal() {
    modalContent.classList.remove("bounceIn");

    setTimeout(() => {
        modalContent.classList.add("slide-out-up");
    }, 140);

    modalContent.classList.remove("slide-out-up");

    setTimeout(() => {
        modalWindow.classList.remove("active");
    }, 720);
}
