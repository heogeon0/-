function solution(n, stations, w) {
  var answer = 0;
  var start = 1;

  for (let station of stations) {
    var leftRange = station - w;
    if (leftRange - start > 0) {
      answer += Math.ceil((leftRange - start) / (2 * w + 1));
    }
    start = station + w + 1;
  }

  if (n + 1 - start > 0) answer += Math.ceil((n + 1 - start) / (2 * w + 1));

  return answer;
}
