const pingOutput = document.querySelector("#ping-json");
const booksOutput = document.querySelector("#books-json");

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

if (booksOutput) {
	fetch("/api/books")
		.then((response) => response.json())
		.then((data) => {
			booksOutput.textContent = JSON.stringify(data, null, 2);
		})
		.catch(() => {
			booksOutput.textContent = "Failed to load /api/books";
		});
}
