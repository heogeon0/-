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
41;
42;
43;
44;
45;
46;
47;
48;
49;
50;
51;
52;
53;
54;
55;
56;
57;
58;
59;
60;
61;
function checkPillar(lsts, x, y) {
  if (y === 0) return true;
  if (lsts.find(([nx, ny, type]) => nx === x && ny === y - 1 && type === 0))
    return true;
  if (lsts.find(([nx, ny, type]) => nx === x && ny === y && type === 1))
    return true;
  if (lsts.find(([nx, ny, type]) => nx === x - 1 && ny === y && type === 1))
    return true;
  return false;
}

function checkFloor(lsts, x, y) {
  if (lsts.find(([nx, ny, type]) => nx === x && ny === y - 1 && type === 0))
    return true;
  if (lsts.find(([nx, ny, type]) => nx === x + 1 && ny === y - 1 && type === 0))
    return true;
  if (
    lsts.find(([nx, ny, type]) => nx === x - 1 && ny === y && type === 1) &&
    lsts.find(([nx, ny, type]) => nx === x + 1 && ny === y && type === 1)
  )
    return true;
  return false;
}

function solution(n, builds) {
  var answer = [];

  builds.forEach((build) => {
    const [x, y, type, isNew] = build;

    if (isNew) {
      let flag;
      if (type) {
        flag = checkFloor(answer, x, y);
      } else {
        flag = checkPillar(answer, x, y);
      }
      if (flag) {
        answer.push([x, y, type]);
      }
    } else {
      const idx = answer.findIndex(
        ([nx, ny, ntype]) => nx === x && ny === y && ntype == type
      );

      answer.splice(idx, 1);
      let flag;
      for (let [nx, ny, ntype] of answer) {
        if (ntype) {
          flag = checkFloor(answer, nx, ny);
        } else {
          flag = checkPillar(answer, nx, ny);
        }

        if (!flag) {
          answer.push([x, y, type]);
          break;
        }
      }
    }
  });

  return answer.sort((a, b) =>
    a[0] === b[0] ? (a[1] === b[1] ? a[2] - b[2] : a[1] - b[1]) : a[0] - b[0]
  );
}
