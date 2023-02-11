import fs, { read } from "fs";
import Keypad from "./keypad.js";

const readInput = (readFile) => {
  const file = fs.readFileSync(readFile, "utf-8").split("\n");
  return file;
};

let keypad = new Keypad();
console.log(keypad.pressAll(readInput("./input.txt")));
