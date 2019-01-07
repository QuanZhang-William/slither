contract Suicide {
    address public owner;
    uint256 public a;

    modifier onlyOwner{
      if(msg.sender != owner) revert();


      modi_set();
      _;
    }

    function modi_set() private{
          if (a == 100){
        a = 1;
      }
        a = 5;
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
        called2();
        called21();
    }

    function called2() public{
        a = 10;
    }

        function called21() public{
        a = 10;

        if (a == 10){
            a = 2;
        }
    }

}
