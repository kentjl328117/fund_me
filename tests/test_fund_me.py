from scripts.useful_code import get_account, LOCAL_BLOCKCHAIN
from scripts.deploy import deploy_fundMe
from brownie import accounts, network, exceptions
import pytest

def test_fund_withdraw():
    account = get_account()
    fundMe = deploy_fundMe()
    minimum = fundMe.getEntranceFee()
    tx = fundMe.send({"from": account, "value": minimum})
    tx.wait(1)
    assert fundMe.fundMeArray(account.address) == minimum
    tx = fundMe.withdraw({"from": account})
    tx.wait(1)
    assert fundMe.fundMeArray(account.address) == 0

def test_onlyOwner():
    if network.show_active() not in LOCAL_BLOCKCHAIN:
        pytest.skip("For Network Development Only!")
    account = accounts.add()
    fundMe = deploy_fundMe()
    fundMe.withdraw({"from": account})
    with pytest.raises(exceptions.VirtualMachineError):
        fundMe.withdraw({"from": account})