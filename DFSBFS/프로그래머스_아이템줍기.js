1;
2;
3;
4;
5;
6;
7;
8;
9;
10;
11;
12;
13;
14;
15;
16;
17;
18;
19;
20;
21;
22;
23;
24;
25;
26;
27;
28;
29;
30;
31;
32;
33;
34;
35;
36;
37;
38;
39;
40;
function solution(rect, chartX, chartY, itemX, itemY) {
  var N = 103;
  var chart = new Array(N).fill(0).map((i) => new Array(N).fill(0));
  // console.log(chart)
  rect.forEach((r) => {
    const [x1, y1, x2, y2] = r.map((i) => i * 2);
    for (let i = x1; i <= x2; i++) {
      for (let j = y1; j <= y2; j++) {
        if (i === x1 || i === x2 || j === y1 || j === y2) {
          if (chart[i][j] === 0) chart[i][j] = 1;
        } else {
          chart[i][j] = 2;
        }
      }
    }
  });
  var answer = 0;

  const Q = [[chartX * 2, chartY * 2, 0]];
  chart[chartX * 2][chartY * 2] = 0;

  while (Q.length) {
    const [nx, ny, cnt] = Q.shift();
    if (nx === itemX * 2 && ny === itemY * 2) {
      return cnt / 2;
    }

    for (let [x, y] of [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ]) {
      const [dx, dy] = [nx + x, ny + y];

      if (chart[dx][dy] === 1) {
        Q.push([dx, dy, cnt + 1]);
        chart[dx][dy] = 0;
      }
    }
  }
  return answer;
}
