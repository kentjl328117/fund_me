from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN = ["development", "ganache-local"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN or network.show_active() == "mainnet-fork-dev":
       return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mock():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mock.....")

    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(8, Web3.toWei(2000, "ether"), {"from" : get_account()})