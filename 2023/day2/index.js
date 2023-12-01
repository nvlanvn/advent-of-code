const solution = (input) => {
  let mostCalories = 0;
  for (let i in input) {
    let currentCalories = 0;
    for (let j in input[i]) {
      currentCalories += input[i][j];
    }
    if (currentCalories > mostCalories) {
      mostCalories = currentCalories;
    }
  }
  return mostCalories;
};

process.stdin.resume();
process.stdin.setEncoding("utf-8");
const inputProcess = [];
process.stdin.on("data", function (input) {
  const numberValue = input.split("\n");
  let subArr = [];

  for (let index = 0; index < numberValue.length; index++) {
    const element = parseInt(numberValue[index]);
    if (element) {
      subArr.push(element);
    } else {
      inputProcess.push(subArr);
      subArr = [];
    }
  }
});
process.stdin.on("end", function () {
  console.log(solution(inputProcess));
});
