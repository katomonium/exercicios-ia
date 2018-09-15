let TABLE = [];
for(var i = 0; i < 8; i++) {
	TABLE.push([]);
	for(var j = 0; j< 8; j++) {
		TABLE[i].push('');
	}
}

const inspect_table = () => {
	let s = '    0 1 2 3 4 5 6 7\n';

	for(var i = 0; i < 8; i++) {
		s += `${i} [ `;
		for(var j = 0; j < 8; j++) {
			if(TABLE[i][j] === '')
				s += '· '
			else
				s += `${TABLE[i][j]} `;
		}
		s += ']\n'
	}

	console.log(s);
}

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

		if(TABLE[i][j] === '') {
			$.ajax({
				type: 'POST',
				url: '/add',
				data: JSON.stringify({ cell: `${i} ${j}` }),
				contentType: "application/json; charset=utf-8",
				dataType: "json",
				success: (data) => {
					draw_many(data.player, true);
					$('#actual').text('Gary');

					setTimeout(() => {
						draw_many(data.ai, false);
					$('#actual').text('Human');
					}, 2000);
				},
				failure: (data) => alert(data)
			});
		}
	});

});

const draw_many = (arr, player) => {
	console.log(arr, arr.length);
	for(let i = 0; i < arr.length; i++) {
		const x = arr[i][0];
		const y = arr[i][2];

		console.log(x, y);
		TABLE[x][y] = player ? 1 : 0;
		draw_circle(x, y, player ? 'black' : 'white');
	}

	inspect_table();
}

const start = () => {
	$.ajax({
		type: 'POST',
		url: '/add',
		data: JSON.stringify({ cmd: 'start' }),
		contentType: "application/json; charset=utf-8",
		dataType: "json",
		success: (data) => {
			for(var i = 0; i < 8; i++) {
				for(var j = 0; j< 8; j++) {
					TABLE[i][j] = '';
					draw_circle(i, j, '')
				}
			}

			TABLE[3][3] = 0;
			TABLE[4][4] = 0;
			TABLE[3][4] = 1;
			TABLE[4][3] = 1;

			draw_circle(3, 3, 'black');
			draw_circle(4, 4, 'black');
			draw_circle(3, 4, 'white');
			draw_circle(4, 3, 'white');
		},
		failure: (data) => alert(data)
	});
}

const render_table = () => {
	console.log('create_table');

	$('#world').append('<table id="table"></table>');
	for(let i = 0; i < 8; i++) {
		$('#table').append(`<tr id="row${i}"></tr>`);
		for(let j = 0; j < 8; j++) {
			const div = `<div id="cell_${i}_${j}" class="cell"></div>`
			$('#row' + i).append(`<td>${div}</td>`);
		}
	}
}

const draw_circle = (i, j, color) => {
	$(`#cell_${i}_${j}`).css('background-color', color);
}
