'use strict';

const { FileSystemWallet, Gateway } = require('fabric-network');
const path = require('path');

const ccpPath = path.resolve(__dirname, '..', '..', 'first-network', 'connection-org1.json');

async function main() {
    try {

        var a = "['a', 'b', 'c']";
        a = a.replace(/'/g, '"');
        var a1 = JSON.parse(a);
        console.log(a);
        console.log(a1);

    } catch (error) {
        console.error(`Failed to evaluate transaction: ${error}`);
        process.exit(1);
    }
}

main();
