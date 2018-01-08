import os
print "hello"
os.system('ls')
os.system('bitcoind -regtest -daemon')
print "create network complete begin to wait"
os.system('sleep 5')
os.system('bitcoin-cli -regtest getinfo')
os.system('sleep 10000')
