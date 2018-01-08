import thread
import os
import logging
import random
import daemon
logging.basicConfig(level=logging.INFO)


#create daemon
def  create_daemon():
    logging.info("Begin to Create Daemon")
    os.system('bitcoind -regtest -daemon')
    logging.info("create network complete")

#join pravite network
def join_network():
    logging.info("Begin to join pravite network")
    os.system('bitcoin-cli -regtest addnode a onetry')
    logging.info("Begin to join pravite network complete")

#show information 
def show():
    logging.info("Test")

def generateblock(blocknumber):
    os.system('bitcoin-cli -regtest generate '+str(blocknumber))
    logging.info("generate "+str(blocknumber) +"block")

#get balance
def getbalance():
    os.system("bitcoin-cli -regtest getbalance")
#main flow


logging.info("Start main flow")
with daemon.DaemonContext():
    while 1:
        #logging.info("server is running")
        #os.system('sleep 5')
        #logging.info("generate sleep time")
        #sleeptime = random.randint(0,15)
        #logging.info("sleeptime is  "+str(sleeptime))
        #os.system('sleep '+str(sleeptime))
        #blocknumber = random.randint(100,300)
        generateblock(1)
        #logging.info("getbalance")
        #getbalance()
