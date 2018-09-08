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
	})
});

function right() {
	$('#r1').animate({left: '250px'});
}

function left() {
	$('#r1').animate({left: '0px'});
}

function down() {
	$('#r1').animate({top: '250px'});
}

function up() {
	$('#r1').animate({top: '0px'});
}