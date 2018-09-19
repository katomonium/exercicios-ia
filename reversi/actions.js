let TABLE = [];
for(var i = 0; i < 8; i++) {
	TABLE.push([]);
	for(var j = 0; j< 8; j++) {
		TABLE[i].push('');
	}
}

READY = true;
var tabuleiro;
var jogador = true;

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
		if(!READY)
			return;

		READY = false;
		const id = e.target.id.split('_');
		const i = parseInt(id[1]);
		const j = parseInt(id[2]);

		if(TABLE[i][j] === '') {
			console.log('oi')
			console.log(tabuleiro)
			console.log('oi')
			$.ajax({
				type: 'POST',
				url: 'http://127.0.0.1:5000/play',
				data: JSON.stringify({ cmd: '', cell: `${i} ${j}`, tabuleiro: tabuleiro, jogador: jogador}),
				contentType: "application/json; charset=utf-8",
				dataType: "json",
				success: (data) => {
					tabuleiro = data['tabuleiro']
					console.log(data);
					atualizarTabuleiro(tabuleiro);
					// draw_many(data.player, true);
					// $('#actual').text('Gary');

					// setTimeout(() => {
					// 	draw_many(data.ai, false);
					// $('#actual').text('Human');
					// }, 2000);
					jogador = !jogador;
					READY = true;
				},
				failure: (data) => alert(data)
			});
		}
	});

});

// const draw_many = (arr, player) => {
// 	console.log(arr, arr.length);
// 	for(let i = 0; i < arr.length; i++) {
// 		const x = arr[i][0];
// 		const y = arr[i][2];

// 		console.log(x, y);
// 		TABLE[x][y] = player ? 1 : 0;
// 		draw_circle(x, y, player ? 'black' : 'white');
// 	}

// 	inspect_table();
// }

function start(){
	for(var i = 0; i < 8; i++) {
		for(var j = 0; j< 8; j++) {
			TABLE[i][j] = '';
		}
	}

	TABLE[3][3] = 1;
	TABLE[4][4] = 1;
	TABLE[3][4] = 0;
	TABLE[4][3] = 0;

	$.ajax({
		type: 'POST',
		url: 'http://127.0.0.1:5000/start',
		data: JSON.stringify({ table: TABLE }),
		contentType: "application/json; charset=utf-8",
		dataType: "json",
		success: (data) => {
			atualizarTabuleiro(data['tabuleiro']);
			console.log(data);
			tabuleiro = data['tabuleiro'];
		},
		failure: (data) => alert(data)
	});
}

function atualizarTabuleiro(tabuleiro){
	for(var i = 0; i < tabuleiro.length; i++) {
		for(var j = 0; j< tabuleiro[0].length; j++) {
			draw_circle(i, j, tabuleiro[i][j])
		}
	}
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

const draw_circle = (i, j, cor) => {
	var color;
	if(cor == 'P'){
		color = 'black';
	}
	else if(cor == 'B'){
		color = 'white';
	}
	else{
		color = '';
	}
	$(`#cell_${i}_${j}`).css('background-color', color);
}
