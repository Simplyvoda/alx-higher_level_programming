#!/usr/bin/node
const process = require('process');
let a = process.argv[2];

if (a/10) {
	console.log('My number:' + ' ' + Math.floor(a));
} else {
	console.log('Not a number');
}
