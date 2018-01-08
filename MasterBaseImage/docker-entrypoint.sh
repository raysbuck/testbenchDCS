#!/bin/bash

echo "create private network"

bitcoind -listen -port=18333 -regtest -daemon -server -reindex

while :
do
        sleep 1
done
