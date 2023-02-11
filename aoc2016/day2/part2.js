import fs from "fs";
import Keypad from "./keypad.js";

const readFile = (fileInput) => {
  const fileContent = fs.readFileSync(fileInput, "utf-8").split("\n");
  return fileContent;
};

let keypad = new Keypad({ type: "diamond" });

//start on5 , which is on left corner
const DIAMOND_STARTING_POINT = [0, 2];

console.log(keypad.pressAll(readFile("./input.txt"), DIAMOND_STARTING_POINT));
