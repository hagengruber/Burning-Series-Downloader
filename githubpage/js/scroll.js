var scroll = document.getElementById("scroll");
scroll.style.transition = "0.5s";

window.addEventListener('scroll', function(event) {
	
	if(window.pageYOffset > 50) {
		
		scroll.style.opacity = "1";
		
	} else {
		
		scroll.style.opacity = "0";
		
	}
	
});

function scroll_to_top() {
	
	document.getElementsByTagName('body')[0].scrollIntoView({behavior: 'smooth'});
	
}