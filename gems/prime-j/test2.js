const { Block, Blockchain, checkPrime } = require("./prime");

let m = new Blockchain();

// let n1 = 3;
// let n2 = 345;
// let n3 = 8;

//Mistake 1 : Never created a new block to be added to the blockchain. Just directly added it without creating a block
// if (checkPrime(n1)) {
//   let b = new Block(2, n1);
//   m.addBlock(b);
//   console.log("Prime Number: ", n1);
//   console.log(b);
// }

// if (checkPrime(n2)) {
//   let b = new Block(3, n2);
//   m.addBlock(b);
//   console.log("Prime Number: ", n2);
//   console.log(b);
// }

// if (checkPrime(n3)) {
//   let b = new Block(4, n3);
//   m.addBlock(b);
//   console.log("Prime Number: ", n3);
//   console.log(b);
// }

let numbers = [3, 5, 8, 342, 343];

for (let i = 0; i <= numbers.length; i++) {
  let n = numbers[i];

  if (checkPrime(i)) {
    let b = new Block(i + 2, n);
    m.addBlock(b);

    console.log("Prime Number: ", n);

    console.log(b);
  }
}
console.log(JSON.stringify(m, null, 2));
