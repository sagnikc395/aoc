const input = "145852-616942";
//TODO
/**
 * to check if the adjacent digits are same or not
 */
const adjacentSame = (num: number) => {
  const strNum = num.toString();
  for (let i = 0; i < strNum.length; i++) {
    if (num[i]) {
      //todo
    }
  }
};

const main = () => {
  let passCount = 0;
  const arr = input.split("-").map((item) => parseInt(item));
  for (let i = arr[0]; i < arr[1]; i++) {
    let temp = arr[i].toString();
  }
};

main();
