// Bench fixture: inert text. The host never resolves.
fetch("http://sim.invalid/beacon", {method: "POST", body: "hello"});
