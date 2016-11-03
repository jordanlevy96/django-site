function frenchToEnglish() {
	this.innerHTML = "Essays";
}

function englishToFrench() {
	this.innerHTML = "Essais";
}

function init() {
	essai = document.getElementById("essay-link");

	essai.onmouseover = frenchToEnglish;
	essai.onmouseout = englishToFrench;
}

window.onload = init;
