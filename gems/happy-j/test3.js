const {Block, Blockchain, checkHappy} = require("./happy");

let m = new Blockchain();

let numbers = [3, 5, 32, 8, 7];

for(let i = 0; i <= numbers.length; i++){
    let num = numbers[i];

    if(checkHappy(num)){
        b = new Block(i + 2, num);
        m.addBlock(b);

        console.log("Happy Number: ", num);
        console.log(b);
    }
}

console.log(JSON.stringify(m, null, 2));