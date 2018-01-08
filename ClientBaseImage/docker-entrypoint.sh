#!/bin/bash

# git clone https://github.com/bitcoin/bitcoin.git ~/bitcoin
# cd ~/bitcoin
# git checkout v0.14.0rc3
# 
# ./autogen.sh
# ./configure
# make
# make install


filename='/root/.bitcoin/central.txt'
exec < $filename
read line
 
echo "create private network"

bitcoind -listen -port=18333 -regtest -daemon -addnode=${line}:18333 -reindex 

sleep 5

echo "join private network"
bitcoin-cli -regtest addnode ${line}:18333 add
#bitcoin-cli -regtest addnode 10.0.2.15:18333 add 
python client.py



