contract Caller {
    uint public a = 0;
    uint public b = 0;

    function writeA(uint input) public{
        a = 10;
    }

    function writB(uint input) public{
        b = 10;
    }

    function readAB(uint input) public{
        if (a == 10 && b == 10){
            a = 100;
        }
    }
}
