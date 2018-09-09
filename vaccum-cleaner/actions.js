var roomTheRobotIs = 0;
var rooms = [true, true, true, true];

$(document).ready(function() {	

	$('#RIGHT').click(function() {
		right();
	});

	$('#LEFT').click(function() {
		left();
	});

	$('#DOWN').click(function() {
		down();
	});

	$('#UP').click(function() {
		up();
	});

	$('.room').click(function() {
		// alert(this.id);
		rooms[this.id] = false;
		$("#"+this.id).css("background-color", "red");
		// cleanRoom(roomTheRobotIs);
	});
	automaticMode();

});
function wait(ms) {
    var start = Date.now(),
        now = start;
    while (now - start < ms) {
      now = Date.now();
    }
}

function cleanRoom(roomId){
	if(rooms[roomId] == false){
		$('#action').text("Cleaning...")
		setTimeout(
			() => {
				$('#action').text("")
				$("#"+roomId).css("background-color", "white");
				rooms[roomId] = true;

			}, 
			2000
		);
	}
}

function right() {
	if(roomTheRobotIs == 0){
		roomTheRobotIs = 1;
	}
	if(roomTheRobotIs == 2){
		roomTheRobotIs = 3;
	}
	cleanRoom(roomTheRobotIs);
	$('#r1').animate({left: '250px'});
}


function left() {
	if(roomTheRobotIs == 1){
		roomTheRobotIs = 0;
	}
	if(roomTheRobotIs == 3){
		roomTheRobotIs = 2;
	}
	cleanRoom(roomTheRobotIs);
	$('#r1').animate({left: '0px'});
}

function down() {
	if(roomTheRobotIs == 0){
		roomTheRobotIs = 2;
	}
	if(roomTheRobotIs == 1){
		roomTheRobotIs = 3;
	}
	cleanRoom(roomTheRobotIs);
	$('#r1').animate({top: '250px'});
}

function up() {
	if(roomTheRobotIs == 2){
		roomTheRobotIs = 0;
	}
	if(roomTheRobotIs == 3){
		roomTheRobotIs = 1;
	}
	cleanRoom(roomTheRobotIs);
	$('#r1').animate({top: '0px'});
}

function automaticMode(){
	console.log("loco");
	if(rooms[roomTheRobotIs] == false){
		console.log("entrou if");
		cleanRoom(roomTheRobotIs);
		setTimeout(
			() => {automaticMode()},
			2000
		);
	}
	else{
		console.log("else");
		switch(roomTheRobotIs){
			case 0:
				right();
				setTimeout(
					() => {automaticMode()},
					2000
				);
				break;
			case 1:
				down();
				setTimeout(
					() => {automaticMode()},
					2000
				);
				break;
			case 2:
				up();
				setTimeout(
					() => {automaticMode()},
					2000
				);
				break;
			case 3:
				left();
				setTimeout(
					() => {automaticMode()},
					2000
				);
				break;
		}
	}
}