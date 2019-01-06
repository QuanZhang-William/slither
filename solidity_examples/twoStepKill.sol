contract Suicide {
    address public owner;
    uint256 public a;

    modifier onlyOwner{
      if(msg.sender != owner) revert();
      a = 5;
      _;
    }

    function setOwner() public{
        owner = msg.sender;
    }

    function kill(address addr) onlyOwner public{
        selfdestruct(msg.sender);
    }

    function caller() public{
        called();
    }

    function called() public{
        a = 10;
    }

}
