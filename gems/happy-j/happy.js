const crypto = require("crypto");

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
      .update(this.id + this.n + this.ph + this.date)
      .digest("hex");
  }
}

class Blockchain {
  constructor() {
    this.chain = [this.createGenesisBlock()];
  }

  createGenesisBlock() {
    return new Block(1, 0, "0");
  }

  getBlock() {
    return this.chain[this.chain.length - 1];
  }

  addBlock(b) {
    b.ph = this.getBlock().h;
    b.h = b.callHash();
    this.chain.push(b);
  }
}

function checkHappy(n) {
  let numbers = [];
  // If the number appears again,
  // it means we are stuck in a cycle
  while (n !== 1) {
    if (numbers.includes(n)) {
      return false;
    }

    numbers.push(n);

    let sum = 0;
    while (n > 0) {
      let digit = n % 10;
      sum = sum + digit * digit;
      n = Math.floor(n / 10);
    }

    n = sum;
  }
  return true;
}

module.exports = {
  Block: Block,
  Blockchain: Blockchain,
  checkHappy: checkHappy,
};
