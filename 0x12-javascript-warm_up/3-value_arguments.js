#!/usr/bin/node
import process from 'node:process';

if (!process.argv[2]) {
	console.log("No argument");
}
else {
	console.log(process.argv[2]);
}
