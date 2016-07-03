'use strict';

console.log('Starting up...');

const fs = require('fs'),
 	child_process = require('child_process');

const _ = require('lodash'),
	request = require('request'),
	parse = require('json-stream');

console.log('Spawning python toolkit...');

let reader = child_process.spawn('python', ['-u', __dirname + '/python-toolkit/read.py']);
reader.once('close', readerClosed);
reader.stdout.pipe(parse()).on('data', readerOnData);

function readerOnData(data){
  	console.log('json', data);
}

function readerClosed(){
  	console.log('closed');
    process.exit();
}
