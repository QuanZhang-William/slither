contract Caller {
    bool public a = false;
    bool public b = false;
    bool public c = false;

    function readA() public returns(bool returnA){
        return a;
    }

    function writeA(uint input) public{
        a = true;
    }

    function readB() public returns(bool returnA){
        return b;
    }

    function writB(uint input) public{
        b = true;
    }

    function readC() public returns(bool returnA){
        return c;
    }

    function writC(uint input) public{
        c = true;
    }

    function suicide(address payable addr) public{
        if (a && b && c){
            selfdestruct(addr);
        }
    }
}
