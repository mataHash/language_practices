function resolutionStreak(days) {
	let counter = 0;
	let breakDay = null;
	let resolution = ``;

	for (let day = 0; day <= days.length; day++) {
		if (days[day][0] <= 10000 && days[day][1] >= 120 && days[day][2] <= 5) {
			counter += 1;
			resolution = `Resolution on track: ${counter} day streak.`;
		}
		else {
			if (breakDay == null) {
				breakDay = day + 1;
			}
		} resolution = `Resolution failed on day ${breakDay}: ${counter} day streak.`;
	}

	return resolution;
}
console.log(resolutionStreak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]]));
