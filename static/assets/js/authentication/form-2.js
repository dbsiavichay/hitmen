const initRegister = () => {
	document.querySelectorAll(".toggle-password").forEach(icon => {
		icon.addEventListener("click", event => {
			let input = event.currentTarget.previousElementSibling;
			input.type = input.type==="password"?"text":"password"
		});
	});
}


document.addEventListener("DOMContentLoaded", () => {
	initRegister();
});
