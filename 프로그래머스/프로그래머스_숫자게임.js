function solution(A, B) {
  A.sort((a, b) => b - a);
  B.sort((a, b) => a - b);
  var answer = 0;
  for (const a of A) {
    const max = B[B.length - 1];
    if (a < max) {
      answer++;
      B.pop();
    }
  }

  return answer;
}
