from brownie import FundMe
from scripts.useful_code import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    minimum = fund_me.getEntranceFee()
    print(minimum)
    print("Funding...")
    fund_me.send({"from": account, "value": minimum})
    

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fundAddress = fund_me.fundMeArray(account.address)
    print(fundAddress)
    fund_me.withdraw({"from": account})
    print(fundAddress)

def main():
    fund()
    withdraw()