'use strict';

console.log('reader: Starting up...');

const path = require('path');
const fs = require('fs');
const pyReadFile = path.join(__dirname , '/py/read.py');
const child_process = require('child_process');
const baseOptions = require('./base-options');

function rc533Reader(options){

  function readerOnData(data){
    	console.log('reader-on-json', data);
  }

  function cleanup(){
    	console.log('reader-closed');
      process.exit();
  }

  let opts = Object.assign({}, baseOptions, options);

  console.log('reader: Spawning python toolkit...');
  let reader = child_process.spawn('python', ['-u', pyReadFile );

  reader
    .once('close', cleanup);

  reader
    .stdout
    .pipe(parse())
    .on('data', readerOnData);
}

module.export = rc533Reader;
