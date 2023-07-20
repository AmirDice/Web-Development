let menu = document.querySelector('.fa-bars');
let navbar = document.querySelector('.navbar');

menu.addEventListener('click',function(){
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('nav-toggle');
});

window.addEventListener('scroll', () =>{
    menu.classList.remove('fa-times');
    navbar.classList.remove('nav-toggle');
});

/* darkmode toggle*/

function toggle_light_mode() {
    var app = document.getElementsByTagName("BODY")[0];
    if (localStorage.lightMode == "dark") {
	localStorage.lightMode = "light";
	app.setAttribute("light-mode", "light");
    } else {
	localStorage.lightMode = "dark";
	app.setAttribute("light-mode", "dark");
    }		
}
var app = document.getElementsByTagName("BODY",)[0];
    if (localStorage.lightMode == "dark") {
        app.setAttribute("light-mode", "dark");
    }


// INSERT JS HERE


// SOCIAL PANEL JS
const floating_btn = document.querySelector('.floating-btn');
const close_btn = document.querySelector('.close-btn');
const social_panel_container = document.querySelector('.social-panel-container');

floating_btn.addEventListener('click', () => {
	social_panel_container.classList.toggle('visible')
});

close_btn.addEventListener('click', () => {
	social_panel_container.classList.remove('visible')
});
