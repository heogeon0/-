function solution(a) {
  const lst = a
    .reduce((acc, now) => {
      acc[now] ? acc[now][1]++ : (acc[now] = [now, 1]);
      return acc;
    }, [])
    .filter((i) => i)
    .sort((a, b) => b[1] - a[1]);
  var answer = -1;

  for (let i = 0; i < lst.length; i++) {
    if (answer >= lst[i][1]) break;

    let count = 0;

    for (let j = 0; j < a.length; j++) {
      if (a[j + 1] === undefined) continue;
      if (a[j] !== lst[i][0] && a[j + 1] !== lst[i][0]) continue;
      if (a[j] === a[j + 1]) continue;

      count++;
      j++;
    }
    answer = Math.max(count, answer);
  }
  return answer * 2;
}
