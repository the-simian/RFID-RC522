

let Reader = require('./lib/read');


function rfidRC522(options){

	options.mode = 'read';

	options = options || {};

	let reader = new Reader(options);

	function start(){

	}

	//public api
	return {
		start: start
	};
}

module.exports = rfidRC522;




var rfid = require('')

rfid({
	scan: processCard,
	error,
	close,
	ready,
	cancelOnerror: true,
	options: {
		sectors: []
	}
}).go();


function scan(card){
	card.write(function(){

	})
	card => {
		uuid
	}

	card.read({sectors[0]},function thing(data){
		{
			sector: sdafsadklfjasef
		}
	})

	card.read({})

}

function processCard(card){
	//
	//
	//
}
