//program to check whether a number is prime or not. I fit is then add block to blockchain

const crypto = require("crypto"); //standard crypto library that needs to be imported

class Block {
  constructor(id, n, ph = "") {
    this.id = id;
    this.n = n;
    this.ph = ph;
    this.date = Date.now();
    this.h = this.callHash();
  }

  callHash() {
    return crypto
      .createHash("sha256")
      .update(this.id + this.n + this.ph + this.date) //do not have to include this.h in this.
      .digest("hex");
  }
}

class Blockchain {
  constructor() {
    this.chain = [this.createGenesisBlock()];
  }

  createGenesisBlock() {
    return new Block(1, 0, "0"); //creating the first block in the chain
  }

  getBlock() {
    return this.chain[this.chain.length - 1];
  }

  addBlock(b) {
    b.ph = this.getBlock().h; //hashing all the details of the recent block
    //need to properly call the function getBlock() instead of just typing 'getBlock'
    b.h = b.callHash(); //hashing the details of the current block
    this.chain.push(b);
  }
}

function checkPrime(n) {
  if (n <= 1) {
    return false;
  }

  for (let i = 2; i < n; i++) {
    if (n % i === 0) {
      return false;
    }
  }

  return true;
}

module.exports = {
  Block: Block,
  Blockchain: Blockchain,
  checkPrime: checkPrime,
};
