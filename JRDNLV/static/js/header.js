function frenchToEnglish() {
	this.innerHTML = "Essays";
}

function englishToFrench() {
	this.innerHTML = "Essais";
}

function init() {
	essays = document.getElementById("essays-link");

	essays.onmouseover = englishToFrench;
	essays.onmouseout = frenchToEnglish;
}

window.onload = init;
