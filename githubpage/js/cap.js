var element = document.getElementsByClassName("btn")[0];

var cap = document.getElementsByClassName("cap")[0];
	
element.addEventListener('mouseover', function(event) { 
	
	cap.style.top = element.offsetTop - 40 + "px";
	cap.style.left = element.offsetLeft + "px";
	cap.style.width = element.offsetWidth + "px";
	cap.style.opacity = 1;
	
 });
 
 element.addEventListener('mouseout', function(event) { 

	cap.style.opacity = 0;
	
 });