function big() {
    function sub1() {
        var x = 7;
        sub2(); // sub2 is called here
    }

    function sub2() {
        var y = x;
        // Under STATIC scoping:
        // The parser looks for 'x' in sub2 (not found).
        // It then looks in the STATIC PARENT (where sub2 was defined), which is 'big'.
        // It finds 'x = 3'.
        // It ignores the 'x = 7' in sub1 because sub1 is not a static ancestor of sub2.
    }

    var x = 3;
    sub1();
}

function big() {
    function sub1() {
        var x = 7;
        sub2();
    }

    function sub2() {
        var y = x;
        // Under DYNAMIC scoping:
        // 1. Search sub2 (local) -> Not found.
        // 2. Search the CALLER (dynamic parent).
        //    If sub2 was called by sub1, it finds x = 7.
        //    If sub2 was called directly by big, it finds x = 3.
    }

    var x = 3;
    sub1(); // Calling sequence: big -> sub1 -> sub2
}