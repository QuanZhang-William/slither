contract Suicide {
    address public owner;
    uint256 public a;

    modifier onlyOwner{
      if(msg.sender != owner) revert();
      _;
    }

    function setOwner() public{
        owner = msg.sender;
    }

    function kill(address addr) onlyOwner public{
        selfdestruct(msg.sender);
    }


}
