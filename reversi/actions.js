let TABLE = [];
for(var i = 0; i < 8; i++) {
	TABLE.push([]);
	for(var j = 0; j< 8; j++) {
		TABLE[i].push('');
	}
}

let PLAYER = true;

$(document).ready(function() {
	console.log('document ready :3');

	render_table();
	start();

	$('#RESET').click(() => {
		start();
	});

	$('.cell').click((e) => {
		const id = e.target.id.split('_');
		const i = parseInt(id[1]);
		const j = parseInt(id[2]);
		console.log(`cell_${i}_${j}: ${TABLE[i][j]} - ${PLAYER}`);

		if(TABLE[i][j] === '') {
			draw_circle(i, j, PLAYER);

			TABLE[i][j] = PLAYER ? 1 : 0;

			for(var x = 0; x < 8; x++) {
				console.log(TABLE[x]);
			}
			PLAYER = !PLAYER;
			const txt = PLAYER ? 'Human' : 'Gary';
			$('#actual').text(txt);
		}
	});

});

const start = () => {
	for(var i = 0; i < 8; i++) {
		for(var j = 0; j< 8; j++) {
			TABLE[i][j] = '';
		}
	}

	TABLE[3][3] = 0;
	TABLE[4][4] = 0;
	TABLE[3][4] = 1;
	TABLE[4][3] = 1;

	draw_circle(3, 3, false);
	draw_circle(4, 4, false);
	draw_circle(3, 4, true);
	draw_circle(4, 3, true);
}

const render_table = () => {
	console.log('create_table');

	$('#world').append('<table id="table"></table>');
	for(let i = 0; i < 8; i++) {
		$('#table').append(`<tr id="row${i}"></tr>`);
		for(let j = 0; j < 8; j++) {
			$('#row' + i).append(`<td><div id="cell_${i}_${j}" class="cell"></div></td>`);
		}
	}
}

const draw_circle = (i, j, p) => {
	if(p) {
		$(`#cell_${i}_${j}`).css('background-color', 'black');
	} else {
		$(`#cell_${i}_${j}`).css('background-color', 'white');
	}
}
