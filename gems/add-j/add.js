const crypto = require("crypto");

class Block {
  constructor(id, n1, n2, ph = "") {
    this.id = id;
    this.n1 = n1;
    this.n2 = n2;
    this.sum = n1 + n2;
    this.ph = ph;
    this.date = Date.now();
    this.h = this.callHash();
  }

  callHash() {
    return crypto
      .createHash("sha256")
      .update(
        this.id + this.n1 + this.n2 + this.sum + this.ph + this.date + this.h,
      )
      .digest("hex");
  }
}

class Blockchain {
  constructor() {
    this.chain = [this.createGenesisBlock()];
  }

  createGenesisBlock() {
    return new Block(1, 0, 0, "0");
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

module.exports = {
  Block: Block,
  Blockchain: Blockchain,
};
