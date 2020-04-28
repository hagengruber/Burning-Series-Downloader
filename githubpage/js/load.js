window.onload = setTimeout(animation_fade_out, 2000);

function animation_fade_out() {
	
	document.getElementById("load").style.opacity = 0;
	document.getElementById("load_in").style.animation = "fadeout 1s";
	setTimeout(animation_vis, 1000);
	
};

function animation_vis() {
	
	document.getElementById("load_in").style.visibility = "hidden";
	
}