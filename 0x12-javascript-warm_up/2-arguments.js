const process = require('process');

if (process.argv > 2) {
    if (process.argv.length === 3) {
        console.log('Argument found');
    } else {
        console.log('Arguments found');
    }
} else {
    console.log('No argument');
}
