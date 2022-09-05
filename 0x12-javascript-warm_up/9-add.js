#!/usr/bin/node
const process = require('process');
let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);

function add(a, b){
	if (a & b) {
		return (a+b);
	} else {
		return (NaN);
	}
}
console.log(add(a, b));
