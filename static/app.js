const pingOutput = document.querySelector("#ping-json");

if (pingOutput) {
	fetch("/api/ping")
		.then((response) => response.json())
		.then((data) => {
			pingOutput.textContent = JSON.stringify(data, null, 2);
		})
		.catch(() => {
			pingOutput.textContent = "Failed to load /api/ping";
		});
}
