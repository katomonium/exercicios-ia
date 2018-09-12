var roomTheRobotIs = 0;
var dirtyness = [0, 0, 0, 0];
var DIRTY_AMOUNT = 15;
var greedMode = true;
var auto = true;

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
	
	$('#SUCK').click(function() {
		cleanRoom(roomTheRobotIs);
	});
	
	$('#AUTO').click(function() {
		if(auto) {
			auto = false;
			$(this).text('Auto Off');
		} else {
			auto = true;
			$(this).text('Auto On');
		}
	});

	$('#MODE').click(function() {
		if(auto) {
			if(greedMode) {
				greedMode = false;
				$(this).text('Cycle Mode');
				$("#r1").css("background-color", "#6464b6");
			} else {
				greedMode = true;
				$(this).text('Greed Mode');
				$("#r1").css("background-color", "#64b664");
			}
		}
	});

	$('.room').click(function() {
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
				$("#"+roomId).css("background-color", "#3b444c");
				$("#"+roomId).text(dirtyness[roomId]);
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

	$('#r1').animate({left: '250px'}, 2000);
}


function left() {
	if(roomTheRobotIs == 1){
		roomTheRobotIs = 0;
	}
	if(roomTheRobotIs == 3){
		roomTheRobotIs = 2;
	}

	$('#r1').animate({left: '0px'}, 2000);
}

function down() {
	if(roomTheRobotIs == 0){
		roomTheRobotIs = 2;
	}
	if(roomTheRobotIs == 1){
		roomTheRobotIs = 3;
	}

	$('#r1').animate({top: '250px'}, 2000);
}

function up() {
	if(roomTheRobotIs == 2){
		roomTheRobotIs = 0;
	}
	if(roomTheRobotIs == 3){
		roomTheRobotIs = 1;
	}

	$('#r1').animate({top: '0px'}, 2000);
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
	}
}

function automaticMode(){
	if(dirtyness[roomTheRobotIs] > 0){
		cleanRoom(roomTheRobotIs);
		setTimeout(
			() => {automaticMode()},
			3000
		);
	}
	else{
		if(greedMode) {
			decideRoom();
		} else {
			goToPreviousRoom();
		}
		setTimeout(
			() => {automaticMode()},
			3000
		);
	}
}
