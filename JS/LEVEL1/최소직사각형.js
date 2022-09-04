function solution(sizes) {
  const minV = [0, 0];

  var answer = 0;

  sizes.forEach((size) => {
    // console.log(Math.min(size[0], size[1]));
    minV[0] = Math.max(minV[0], Math.max(size[0], size[1]));
    minV[1] = Math.max(minV[1], Math.min(size[0], size[1]));
  });
  answer = minV[0] * minV[1];
  return answer;
  console.log(answer);
}

solution([
  [60, 50],
  [30, 70],
  [60, 30],
  [80, 40],
]);
