from brownie import FundMe, MockV3Aggregator, network, config
from scripts.useful_code import get_account, deploy_mock, LOCAL_BLOCKCHAIN

def deploy_fundMe():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN:
        price_feed_address = config["networks"][network.show_active()]["priceFeed_address"]
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address
    
    fundMe = FundMe.deploy(
        price_feed_address,
        {"from" : account}, 
        publish_source=config["networks"][network.show_active()].get("verify"))

    print(f"The contract address is {fundMe.address}")
    print(fundMe.getEntranceFee())
    return fundMe

def main():
    deploy_fundMe()