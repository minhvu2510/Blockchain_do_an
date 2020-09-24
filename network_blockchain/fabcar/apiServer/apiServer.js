var express = require('express');
var bodyParser = require('body-parser');
var cors = require('cors')
var app = express();
app.use(cors())

app.use(bodyParser.json());// Setting for Hyperledger Fabric

const { FileSystemWallet, Gateway } = require('fabric-network');
const path = require('path');
const ccpPath = path.resolve(__dirname, '..', '..', 'first-network', 'connection-org1.json');

app.get('/api/queryAllCandidates', async function (req, res) {
    try {
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = new FileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        const userExists = await wallet.exists('user1');
        if (!userExists) {
            console.log('An identity for the user "user1" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }

        const gateway = new Gateway();
        await gateway.connect(ccpPath, { wallet, identity: 'user1', discovery: { enabled: true, asLocalhost: true } });

        const network = await gateway.getNetwork('mychannel');

        const contract = network.getContract('fabcar');

        const result = await contract.evaluateTransaction('AnsryAllCandidates');
        console.log(`Transaction has been evaluated, result is: ${result.toString()}`);
        res.status(200).json({response: result.toString()});
    } catch (error) {
        console.error(`Failed to evaluate transaction: ${error}`);
        res.status(500).json({error: error});
        //process.exit(1);
    }
});

app.get('/api/query/:candidate_id', async function (req, res) {
    try {
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = new FileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);
        const userExists = await wallet.exists('user1');
        if (!userExists) {
            console.log('An identity for the user "user1" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }

        const gateway = new Gateway();
        await gateway.connect(ccpPath, { wallet, identity: 'user1', discovery: { enabled: true, asLocalhost: true } });

        const network = await gateway.getNetwork('mychannel');// lấy mạng block
        const contract = network.getContract('fabcar');// lấy smartcontract trong mang
       
        const result = await contract.evaluateTransaction('AnsryCandidate', req.params.candidate_id);
       
        console.log(`Transaction has been evaluated, result is: ${result.toString()}`);
        res.status(200).json({response: result.toString()});
    } catch (error) {
        console.error(`Failed to evaluate transaction: ${error}`);
        res.status(500).json({error: error});
        //process.exit(1);
    }
});

app.post('/api/addCandidate', async function (req, res) {
    try {
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = new FileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);
        const userExists = await wallet.exists('user1');
        if (!userExists) {
            console.log('An identity for the user "user1" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }
        const gateway = new Gateway();
        await gateway.connect(ccpPath, { wallet, identity: 'user1', discovery: { enabled: true, asLocalhost: true } });
        const network = await gateway.getNetwork('mychannel');
        const contract = network.getContract('fabcar');
        // createCar transaction - requires 5 argument, ex: ('createCar', 'CAR12', 'Honda', 'Accord', 'Black', 'Tom')
        // changeCarOwner transaction - requires 2 args , ex: ('changeCarOwner', 'CAR10', 'Dave')
        await contract.submitTransaction('createCandidate', req.body.can_id, req.body.HoTen, req.body.GioiTinh, req.body.DiaChi, req.body.MaDuThi, req.body.NgaySinh, req.body.CMT, req.body.KT, JSON.stringify(req.body.BaiLam), JSON.stringify(req.body.Diem));
        console.log('Transaction has been submitted');
        res.send('Transaction has been submitted');
        // {"can_id" : "THPTQG5", "HoTen" :"Nguyễn Thị Lệ","GioiTinh": "Nam","DiaChi": "Hà Nam","MaDuThi": "K20THPT111","NgaySinh": "11/11/2002", "CMT": "3727272763", "KT": "['A']","BaiLam": {"Toan": {"Ans1": "A"}}, "Diem": {"Toan":10}}
        await gateway.disconnect();
    } catch (error) {
        console.error(`Failed to submit transaction: ${error}`);
        res.send('Failed to submit transaction');
        // process.exit(1);
    }
})

app.put('/api/changePoin', async function (req, res) {
    try {
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = new FileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);
        console.log(`Wallet path: ${req.body.candidate_id}, ${JSON.stringify(req.body.poin)}`);
        const userExists = await wallet.exists('user1');
        if (!userExists) {
            console.log('An identity for the user "user1" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }
        const gateway = new Gateway();
        await gateway.connect(ccpPath, { wallet, identity: 'user1', discovery: { enabled: true, asLocalhost: true } });
        const network = await gateway.getNetwork('mychannel');
        const contract = network.getContract('fabcar');
        await contract.submitTransaction('changePoin', req.body.candidate_id,JSON.stringify(req.body.poin));
        console.log('Transaction has been submitted');
        res.send('Transaction has been submitted');
        await gateway.disconnect();
    } catch (error) {
        console.error(`Failed to submit transaction: ${error}`);
	//process.exit(1);
    }
})

app.put('/api/changeName', async function (req, res) {
    try {
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = new FileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);
        const userExists = await wallet.exists('user1');
        if (!userExists) {
            console.log('An identity for the user "user1" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }
        const gateway = new Gateway();
        await gateway.connect(ccpPath, { wallet, identity: 'user1', discovery: { enabled: true, asLocalhost: true } });
        const network = await gateway.getNetwork('mychannel');
        const contract = network.getContract('fabcar');
        await contract.submitTransaction('changeName', req.body.candidate_id, req.body.Name);
        console.log('Transaction has been submitted');
        // res.send('Transaction has been submitted');
        // const result = {'status': 'ok'}
        res.status(200).json({response: 'ok'});
        // await gateway.disconnect();
    } catch (error) {
        console.error(`Failed to submit transaction: ${error}`);
	//process.exit(1);
    }
})

app.put('/api/changeAddress', async function (req, res) {
    try {
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = new FileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);
        console.log(`Wallet path: ${req.body.candidate_id}, ${req.body.address}`);
        const userExists = await wallet.exists('user1');
        if (!userExists) {
            console.log('An identity for the user "user1" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }
        const gateway = new Gateway();
        await gateway.connect(ccpPath, { wallet, identity: 'user1', discovery: { enabled: true, asLocalhost: true } });
        const network = await gateway.getNetwork('mychannel');
        const contract = network.getContract('fabcar');
        await contract.submitTransaction('changeAddress', req.body.candidate_id, req.body.address);
        console.log('Transaction has been submitted');
        res.status(200).json({response: 'ok'});
    } catch (error) {
        console.error(`Failed to submit transaction: ${error}`);
	//process.exit(1); Hải Phòng
    }
})

app.put('/api/changeIdentify', async function (req, res) {
    try {
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = new FileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);
        const userExists = await wallet.exists('user1');
        if (!userExists) {
            console.log('An identity for the user "user1" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }
        const gateway = new Gateway();
        await gateway.connect(ccpPath, { wallet, identity: 'user1', discovery: { enabled: true, asLocalhost: true } });
        const network = await gateway.getNetwork('mychannel');
        const contract = network.getContract('fabcar');
        await contract.submitTransaction('changeIdentify', req.body.candidate_id, req.body.Identify);
        console.log('Transaction has been submitted');
        res.status(200).json({response: 'ok'});
    } catch (error) {
        console.error(`Failed to submit transaction: ${error}`);
	//process.exit(1);
    }
})
app.put('/api/changeBaiLam', async function (req, res) {
    try {
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = new FileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);
        console.log(`Wallet path: ${req.body.candidate_id}, ${JSON.stringify(req.body.poin)}`);
        const userExists = await wallet.exists('user1');
        if (!userExists) {
            console.log('An identity for the user "user1" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }
        const gateway = new Gateway();
        await gateway.connect(ccpPath, { wallet, identity: 'user1', discovery: { enabled: true, asLocalhost: true } });
        const network = await gateway.getNetwork('mychannel');
        const contract = network.getContract('fabcar');
        await contract.submitTransaction('changeBaiLam', req.body.candidate_id,JSON.stringify(req.body.BaiLam));
        console.log('Transaction has been submitted');
        res.send('Transaction has been submitted');
        await gateway.disconnect();
    } catch (error) {
        console.error(`Failed to submit transaction: ${error}`);
	//process.exit(1);
    }
})
app.put('/api/changeDate', async function (req, res) {
    try {
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = new FileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);
        console.log(`Wallet path: ${req.body.candidate_id}, ${req.body.Date}`);
        const userExists = await wallet.exists('user1');
        if (!userExists) {
            console.log('An identity for the user "user1" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }
        const gateway = new Gateway();
        await gateway.connect(ccpPath, { wallet, identity: 'user1', discovery: { enabled: true, asLocalhost: true } });
        const network = await gateway.getNetwork('mychannel');
        const contract = network.getContract('fabcar');
        await contract.submitTransaction('changeDate', req.body.candidate_id,req.body.Date);
        console.log('Transaction has been submitted');
        res.send('Transaction has been submitted');
        await gateway.disconnect();
    } catch (error) {
        console.error(`Failed to submit transaction: ${error}`);
	//process.exit(1);
    }
})
app.put('/api/changeSex', async function (req, res) {
    try {
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = new FileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);
        console.log(`Wallet path: ${req.body.candidate_id}, ${req.body.Sex}`);
        const userExists = await wallet.exists('user1');
        if (!userExists) {
            console.log('An identity for the user "user1" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }
        const gateway = new Gateway();
        await gateway.connect(ccpPath, { wallet, identity: 'user1', discovery: { enabled: true, asLocalhost: true } });
        const network = await gateway.getNetwork('mychannel');
        const contract = network.getContract('fabcar');
        await contract.submitTransaction('changeGioiTinh', req.body.candidate_id,req.body.Sex);
        console.log('Transaction has been submitted');
        res.send('Transaction has been submitted');
        await gateway.disconnect();
    } catch (error) {
        console.error(`Failed to submit transaction: ${error}`);
	//process.exit(1);
    }
})

app.listen(8081);
