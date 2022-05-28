// SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {

    mapping(address => uint256) public fundMeArray;

    address[] public fundAddresses;

    address public owner;

    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }

    function send() public payable {

        // uint256 minimumAmount = 50 * 10 ** 18;
        // require(getCorversion(msg.value) >= minimumAmount, "You need to spent more eth!");

        fundMeArray[msg.sender] += msg.value;

        fundAddresses.push(msg.sender);

    }

    function getVersion() public view returns(uint256) {
        return priceFeed.version();
    }

    function getPrice() public view returns(uint256) {
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer);
    }

    function getCorversion(uint256 ethAmount) public view returns(uint256) {
        uint256 priceFeed = getPrice();
        uint256 ethPrice = (ethAmount * priceFeed) / 1000000000000000000;
        return ethPrice;
    }

    function getEntranceFee() public view returns (uint256) {
        uint256 minimum_usd = 1 * 10**18;
        uint256 price_eth = getPrice();
        // uint256 pricision = 1 * 10**18;
        uint256 entranceFee = minimum_usd / price_eth;
        return entranceFee;
    }

    modifier ownerOnly {
        require(msg.sender == owner);
        _;
    }

    function withdraw() public ownerOnly payable {

        address payable value = payable(msg.sender);

        require(value == owner);
        
        value.transfer(address(this).balance);

        for (uint256 index; index < fundAddresses.length; index++) {
            address fundAdd = fundAddresses[index];
            fundMeArray[fundAdd] = 0;
        }

        fundAddresses = new address[](0);
    }

}