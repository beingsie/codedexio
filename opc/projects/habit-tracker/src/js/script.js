const dotw = document.getElementById("dotw");
const dotwDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
for (let x = 0; x < dotwDays.length; x++) {
	let dayotw = dotwDays[x];
	dotw.innerHTML += `
				<p class="text-center text-white font-semibold">${dayotw}</p>
		`;
}

const griddy = document.getElementById("griddy");
for (let i = 0; i < 30; i++) {
	let dayNum = 1;
	dayNum += i;

	griddy.innerHTML += `
				<div class="check-box flex items-center justify-center">
						<div class="check-box-overlay"></div>
						<p class="date-text text-2xl font-semibold text-white opacity-25">${dayNum}</p>
				</div>
		`;
}

const checkBoxes = document.querySelectorAll(".check-box");
const cbo = document.querySelectorAll(".check-box-overlay");
let streakTracker = document.getElementById("streakTracker");
const highestStreakTracker = document.getElementById("highestStreakTracker");
let streak = 0;
let highestStreak = 0;
let tracker = 0;
let lastClickedNumber = 0;
let streakStartElement = null;
let streakElements = [];

checkBoxes.forEach((checkbox, index) => {
	console.log(`Setting up checkbox ${index + 1}`); // Debug log
	checkbox.addEventListener("click", () => {
		let cboOverlay = checkbox.querySelector(".check-box-overlay");
		let dateText = checkbox.querySelector(".date-text");
		let clickedNumber = parseInt(dateText.textContent);

		console.log(
			`Clicked number: ${clickedNumber}, Last clicked number: ${lastClickedNumber}`,
		); // Debug log

		cboOverlay.style = "transform: scale(1.5);";
		dateText.classList.add("text-white", "opacity-100");

		if (streak === 0 || clickedNumber === lastClickedNumber + 1) {
			tracker += 1;
			streak += 1;
			streakElements.push(cboOverlay);

			if (streak === 2) {
				streakElements[1].style.backgroundColor = "#26A641";
			} else if (streak > 2 && streak < 5) {
				streakElements.forEach((el) => (el.style.backgroundColor = "#39d353"));
			} else if (streak >= 5 && streak < 7) {
				streakElements.forEach((el) => (el.style.backgroundColor = "#AD64D0"));
			} else if (streak >= 7) {
				streakElements.forEach((el) => (el.style.backgroundColor = "#FF8642"));
			}

			lastClickedNumber = clickedNumber;
		} else {
			tracker = 1;
			streak = 1;
			lastClickedNumber = clickedNumber;
			streakStartElement = cboOverlay;
			streakElements = [cboOverlay];
		}

		if (streak > highestStreak) {
			highestStreak = streak;
			highestStreakTracker.innerText = highestStreak;
		}

		streakTracker.innerText = streak;
		console.log(`Streak: ${streak}`); // Debug log
	});
});

function resetProgress() {
	const resetBtn = document.getElementById("resetBtn");

	resetBtn.addEventListener("click", () => {
		tracker = 0;
		streak = 0;
		highestStreak = 0;
		lastClickedNumber = 0;
		streakStartElement = null;
		streakElements = [];
		streakTracker.innerText = streak;
		highestStreakTracker.innerText = 0;

		griddy.classList.add("wobble-hor-bottom");
		
		setTimeout(() => {
			griddy.classList.remove("wobble-hor-bottom");
		}, 300);

		checkBoxes.forEach((checkbox) => {
			let cboOverlay = checkbox.querySelector(".check-box-overlay");
			let dateText = checkbox.querySelector(".date-text");

			cboOverlay.style = "transform: scale(0);";
			cboOverlay.style.backgroundColor = "initial";
			dateText.classList.remove("opacity-100");
			dateText.classList.add("text-white", "opacity-25");
		});
	});
}

resetProgress();
