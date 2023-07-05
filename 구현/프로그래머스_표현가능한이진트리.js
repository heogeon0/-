function isPossible(number) {
  while (true) {
    if (number.length === 1 && number[0] === "1") return true;

    const newNumber = [];

    for (let i = 0; i < number.length; i += 4) {
      if (number[i + 1] === "0" || !number[i + 1]) {
        if (number[i] === "1" || number[i + 2] === "1") return false;
      }

      newNumber.push(number[i + 1] || "0");

      if (number[i + 3]) newNumber.push(number[i + 3]);
    }

    number = newNumber;
  }
}

function solution(numbers) {
  numbers = numbers.map((number) => number.toString(2).split("").reverse());
  return numbers.map((i) => (isPossible(i) ? 1 : 0));
}
