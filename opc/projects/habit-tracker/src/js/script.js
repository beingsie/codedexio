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
let streak = 0;

checkBoxes.forEach((checkbox) => {
	checkbox.addEventListener("click", () => {
		let cboOverlay = checkbox.querySelector(".check-box-overlay");
		let dateText = checkbox.querySelector(".date-text");

		cboOverlay.style = "transform: scale(1.5);";
		dateText.classList.add("text-white", "opacity-100");
		// cboOverlay.classList.add("animate-[ping_1s_ease-in-out_forwards]");

		streak += 1;
		streakTracker.innerText = streak;
	});
});

function resetProgress() {
	const resetBtn = document.getElementById("resetBtn");

	resetBtn.addEventListener("click", () => {
		streak = 0;
		streakTracker.innerText = streak;

		griddy.classList.add("tilt-it");
		setTimeout(() => {
			griddy.classList.remove("tilt-it");
		}, 300);

		checkBoxes.forEach((checkbox) => {
			let cboOverlay = checkbox.querySelector(".check-box-overlay");
			let dateText = checkbox.querySelector(".date-text");

			cboOverlay.style = "transform: scale(0);";
			dateText.classList.remove("opacity-100");
			dateText.classList.add("text-white", "opacity-25");
		});
	});
}

resetProgress();
