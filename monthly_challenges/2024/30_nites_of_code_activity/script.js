// Get the reference to the HTML element with the id "grid-container"
const gridContainer = document.getElementById("grid-container");

// Initialize a variable to keep track of the numbers
let number = 1;

// Loop through 5 rows
for (let row = 0; row < 5; row++) {
    // Loop through 6 columns within each row
    for (let col = 0; col < 6; col++) {
        // Create a new div element to represent a grid item
        const gridItem = document.createElement("div");
        gridItem.classList.add("grid-item"); // Add a CSS class to the grid item

        // Create a new paragraph element to hold the number
        const pTag = document.createElement("p");
        pTag.classList.add("ps2p", "square-activity-none"); // Add CSS classes to the paragraph
        pTag.textContent = number++; // Set the content of the paragraph to the current number

        // Append the paragraph element to the grid item
        gridItem.appendChild(pTag);

        // Append the grid item to the grid container
        gridContainer.appendChild(gridItem);
    }
}

// Function to calculate remaining time in 24-hour format
function calculateRemainingTime() {
    const now = new Date(); // Current date and time
    const endOfDay = new Date(); // Create a new date object

    // Set the end of the day to 23:59:59 (end of the current day)
    endOfDay.setHours(23, 59, 59, 999);

    // Calculate the remaining time in milliseconds
    const remainingTimeMs = endOfDay - now;

    // Convert milliseconds to hours, minutes, and seconds
    const hours = String(Math.floor(remainingTimeMs / (1000 * 60 * 60))).padStart(2, "0");
    const minutes = String(Math.floor((remainingTimeMs % (1000 * 60 * 60)) / (1000 * 60))).padStart(2, "0");
    const seconds = String(Math.floor((remainingTimeMs % (1000 * 60)) / 1000)).padStart(2, "0");

    // Display the remaining time in 24-hour format
    const remainingTimeElement = document.getElementById("remaining-time");
    remainingTimeElement.textContent = `${hours}:${minutes}:${seconds}`;
}

// Call the function to initially display the remaining time
calculateRemainingTime();

// Update the remaining time every second
setInterval(calculateRemainingTime, 1000);

// Function to get and display the current day of the month
function displayCurrentDay() {
    // Get the current date
    const currentDate = new Date();

    // Get the day of the month (1-31)
    const currentDayOfMonth = currentDate.getDate();

    // Display the current day of the month in the specified element
    const currentDayElement = document.getElementById("currentDay");
    currentDayElement.textContent = currentDayOfMonth;
}

// Call the function to display the current day of the month and highlight the corresponding grid item
displayCurrentDay();


// Function to show a success modal with the specified message
function showSuccessModal(message) {
    const alertModal = document.getElementById("alertModal");
    const modalMessage = document.getElementById("modalMessage");
    const modalWrapper = document.getElementById("modalWrapper")

    modalMessage.textContent = message;
    alertModal.style.display = "flex";

    modalWrapper.classList.add("bounceIn")
}

// Function to show an error modal with the specified message
function showErrorModal(message) {
    const alertModal = document.getElementById("alertModal");
    const modalMessage = document.getElementById("modalMessage");
    const modalWrapper = document.getElementById("modalWrapper")

    modalMessage.textContent = message;
    alertModal.style.display = "flex";

    modalWrapper.classList.add("bounceIn")
}

// Function to close the modal
function closeModal() {
    const alertModal = document.getElementById("alertModal");
    alertModal.style.display = "none";
}

// Add click event listener to the close button
const closeButton = document.querySelector(".close");
if (closeButton) {
    closeButton.addEventListener("click", closeModal);
}

// Add click event listener to the alertModal to close it when clicked
const alertModal = document.getElementById("alertModal");
if (alertModal) {
    alertModal.addEventListener("click", closeModal);
}

// Function to update the image based on the username provided by the user
function updateImage() {
    // Get the input element and the image element by their IDs
    const usernameInput = document.getElementById("usernameInput");
    const hatchlingImage = document.getElementById("hatchlingImage");

    // Get the username provided by the user from the input element
    const username = usernameInput.value;

    // Create the URL by appending the username
    const imageUrl = `https://www.codedex.io/api/petStatus?user=${username}`;

    // Check if the username input is empty
    if (username.trim() === "") {
        // Show an error message for empty input
        showErrorModal("Hm.. You're either not a Codédex member or have mistyped your username.");
        return;
    }

    // Create a new image element to check if the new image loads successfully
    const newImage = new Image();
    
    // Set the source of the new image
    newImage.src = imageUrl;

    // Success messages list
    const successMessages = [
        "That's the CUTEST pet!",
        "Your pet is ADORABLE!",
        "What a LOVELY pet!",
        "You have a BEAUTIFUL pet!",
    ];

    newImage.onload = function() {
        // Image loaded successfully
        hatchlingImage.src = imageUrl; // Update the displayed image
    
        // Select a random message from the successMessages array
        const randomIndex = Math.floor(Math.random() * successMessages.length);
        const randomMessage = successMessages[randomIndex];
    
        showSuccessModal(randomMessage);
    
        // Store the URL in localStorage
        localStorage.setItem("imageUrl", imageUrl);
    };    

    // Check if the new image fails to load
    newImage.onerror = function() {
        // Image failed to load
        showError   ("Error updating image URL. Please try again with a valid username.");
    };

    // Store the username in localStorage
    localStorage.setItem("username", username);
}

// Function to load the saved URL from localStorage
function loadSavedUrl() {
    const savedUrl = localStorage.getItem("imageUrl");
    if (savedUrl) {
        const hatchlingImage = document.getElementById("hatchlingImage");
        hatchlingImage.src = savedUrl;
    }
}

// Load the saved URL when the page loads
loadSavedUrl();

