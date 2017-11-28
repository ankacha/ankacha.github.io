function setup() {
	//setup code goes in here
	createCanvas(500, 500)
}

function draw() {
	//drawing code goes here
	if(mouseIsPressed){
		fill(0);
	} 
	else {
		fill(244, 206, 255);
	}
			
	line(mouseX, mouseY, 80, 80);
}