window.onload = init


let menu_nav;

function init(){
	
	menu_nav = document.getElementById("menu_nav");
	menu_nav.style.display = "none";

	menu_logo = document.getElementsByClassName("menu_logo");
	menu_logo[0].onclick = toggle_nav
	

}

function toggle_nav(){
	
	menu_nav = document.getElementById("menu_nav");
	
	if(menu_nav.style.display == "none"){
		menu_nav.style.display = "block";
	}else{
		menu_nav.style.display = "none";
	}
	
}