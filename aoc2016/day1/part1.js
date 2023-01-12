const manhattan = require('manhattan');
const input = require('./input');
let directions = ['N','E','W','S'];


//north 

let current_direction = 0;
const rotate = l_or_r => {
    if(l_or_r === 'R'){
        current_direction = (current_direction + 1) % directions.length; 
    } else {
        //turning left is like turning right 3 times.
        // makes it easier than I alwuyas increase and dont have to worry about the negative values 
        current_direction = (current_direction +3)%directions.length; 
    }
};

let coords = [0,0];
let move = {
    N: v => (coords[1]-=v),
    E: v => (coords[0]+=v),
    W: v => (coords[1]+=v),
    S: v => (coords[0]-=v),
};

input.forEach(action => {
    let {turn,walk} = action;
    rotate(turn);

    let facing = directions[current_direction];
    move[facing](walk);
});

console.log(manhattan([0,0],coords));


