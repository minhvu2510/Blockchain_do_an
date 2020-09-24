[//]: # (SPDX-License-Identifier: CC-BY-4.0)

## Hyperledger Fabric Samples

Please visit the [installation instructions](http://hyperledger-fabric.readthedocs.io/en/latest/install.html)
to ensure you have the correct prerequisites installed. Please use the
version of the documentation that matches the version of the software you
intend to use to ensure alignment.


## Mạng blockchain dựa trên một ví dụ mạng blocchain được cung cấp bởi fabric có kiến trúc như sau:
<img width="483" alt="Picture_block" src="https://user-images.githubusercontent.com/36092539/94166177-35995b80-feb5-11ea-868b-017da3f2d470.png">


## Build mạng blockchain
1: Cài đặt Hyperledger Fabric:
```bash
cd fab1.4
curl -sSL http://bit.ly/2ysbOFE | bash -s -- 1.4.2 1.4.2 0.4.15
```

2: Thiết lập first-network/byfn.sh 
```bash
cd ../first-network
echo y | ./byfn.sh down
echo y | ./byfn.sh up -a -n -s couchdb
```
2: build lại mạng fabric:
```bash
cd first-network
./byfn.sh down
docker rm -f $(docker ps -aq)
docker rmi -f $(docker images | grep fabcar | awk '{print $3}')
cd fabcar/
./startFabric.sh javascript
rm -rf wallet
node enrollAdmin.js
node registerUser.js
node apiServer.js
```
3: Cài đặt Chaincode Fabcar lên tất cả các nút trong kênh
```bash
echo  "Installing smart contract on peer0.org1.example.com"
    docker exec \
        -e CORE_PEER_LOCALMSPID=Org1MSP \
        -e CORE_PEER_ADDRESS=peer0.org1.example.com:7051 \
        -e CORE_PEER_MSPCONFIGPATH=${ORG1_MSPCONFIGPATH} \
        -e CORE_PEER_TLS_ROOTCERT_FILE=${ORG1_TLS_ROOTCERT_FILE} \
        cli \
        peer chaincode install \
            -n fabcar \
            -v 1.0 \
            -p "$CC_SRC_PATH" \
            -l "$CC_RUNTIME_LANGUAGE"
```
4: Khởi tạo Fabcar chaincode trên kênh mychannel

    echo "Instantiating smart contract on mychannel"
    docker exec \
    -e CORE_PEER_LOCALMSPID=Org1MSP \
    -e CORE_PEER_MSPCONFIGPATH=${ORG1_MSPCONFIGPATH} \
    cli \
    peer chaincode instantiate \
        -o orderer.example.com:7050 \
        -C mychannel \
        -n fabcar \
        -l "$CC_RUNTIME_LANGUAGE" \
        -v 1.0 \
        -c '{"Args":[]}' \
        -P "AND('Org1MSP.member','Org2MSP.member')" \
        --tls \
        --cafile ${ORDERER_TLS_ROOTCERT_FILE} \
        --peerAddresses peer0.org1.example.com:7051 \
        --tlsRootCertFiles ${ORG1_TLS_ROOTCERT_FILE}
5: Khởi tạo Ledger
```bash
echo "Submitting initLedger transaction to smart contract on mychannel"
echo "The transaction is sent to the two peers with the chaincode installed (peer0.org1.example.com and peer0.org2.example.com) so that chaincode is built before receiving the following requests"
docker exec \
  -e CORE_PEER_LOCALMSPID=Org1MSP \
  -e CORE_PEER_MSPCONFIGPATH=${ORG1_MSPCONFIGPATH} \
  cli \
  peer chaincode invoke \
    -o orderer.example.com:7050 \
    -C mychannel \
    -n fabcar \
    -c '{"function":"initLedger","Args":[]}' \
    --waitForEvent \
    --tls \
    --cafile ${ORDERER_TLS_ROOTCERT_FILE} \
    --peerAddresses peer0.org1.example.com:7051 \
    --peerAddresses peer0.org2.example.com:9051 \
    --tlsRootCertFiles ${ORG1_TLS_ROOTCERT_FILE} \
    --tlsRootCertFiles ${ORG2_TLS_ROOTCERT_FILE}
```