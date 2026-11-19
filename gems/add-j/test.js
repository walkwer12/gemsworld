const{Block, Blockchain} = require("./add");

// Here, The Blockchain constructor is called.
// The chain array is initialized.
// The Genesis Block is automatically created.
let m = new Blockchain();

//first block after genesis block
m.addBlock(new Block(2, 30, 25));

//seocond block
m.addBlock(new Block(3, 10, 12));

//thrid block
m.addBlock(new Block(4, 40, 60));

console.log(JSON.stringify(m, null, 2));

// - JSON.stringify() converts a JavaScript object into a JSON string.
// - m is the blockchain object we want to display.
// - null means we are not applying any custom filtering or replacement.
// - 2 specifies the indentation of two spaces to make the output readable.
