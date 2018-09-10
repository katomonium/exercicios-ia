var roomTheRobotIs = 0;
var rooms = [true, true, true, true];
var dirtyness = [0, 0, 0, 0];
let DIRTY_AMOUNT = 15

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
		increaseDirty(this.id);
	});
	automaticMode();

});

function cleanRoom(roomId){
	if(dirtyness[roomId] > 0){
		dirtyness[roomTheRobotIs] = 0;
		$('#action').text("Cleaning...")
		setTimeout(
			() => {
				$('#action').text("")
				$("#"+roomId).css("background-color", "white");
				$("#"+roomId).text(dirtyness[roomId]);
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

function goToNextRoom(){
	switch(roomTheRobotIs){
		case 0:
			right();
			break;
		case 1:
			down();
			break;
		case 2:
			up();
			break;
		case 3:
			left();
			break;
	}
}

function goToPreviousRoom(){
	switch(roomTheRobotIs){
		case 0:
			down();
			break;
		case 1:
			left();
			break;
		case 2:
			right();
			break;
		case 3:
			up();
			break;
	}
}

function getNextRoom(){
	switch(roomTheRobotIs){
		case 0:
			return 1;
			break;
		case 1:
			return 3;
			break;
		case 2:
			return 0;
			break;
		case 3:
			return 2;
			break;
	}
}

function getPreviousRoom(){
	switch(roomTheRobotIs){
		case 1:
			return 0;
			break;
		case 3:
			return 1;
			break;
		case 0:
			return 2;
			break;
		case 2:
			return 3;
			break;
	}
}

function decideRoom(){
	if(dirtyness[roomTheRobotIs] > dirtyness[getNextRoom()] && dirtyness[roomTheRobotIs] > dirtyness[getPreviousRoom()]){
		cleanRoom(roomTheRobotIs);
		return;
	}
	if(dirtyness[getNextRoom()] > dirtyness[getPreviousRoom()]){
		goToNextRoom();
	}
	else{
		goToPreviousRoom();
	}
}

function automaticDirty(){
	for(var i = 0; i < 4; i++){
		increaseDirty(i);
	}
}

function increaseDirty(i){
	dirtyness[i] = dirtyness[i] + DIRTY_AMOUNT;
	$('#'+i).text(dirtyness[i]);
	if(dirtyness[i] > 99){
		rooms[i] = false;
		$("#"+i).css("background-color", "red");
	}
}

function automaticMode(){
	console.log("loco");
	// automaticDirty();


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
		// goToNextRoom();
		decideRoom();
		setTimeout(
				() => {automaticMode()},
				2000
		);
	}
}
