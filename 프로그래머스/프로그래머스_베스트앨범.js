function solution(genres, plays) {
  const total = new Map();
  const genre = {};

  for (let i = 0; i < plays.length; i++) {
    if (total.has(genres[i])) {
      total.set(genres[i], total.get(genres[i]) + plays[i]);
    } else {
      total.set(genres[i], plays[i]);
    }

    genre[genres[i]] = (genre[genres[i]] || []).concat([[i, plays[i]]]);
  }

  const total_array = Array.from(total);
  total_array.sort((a, b) => b[1] - a[1]);

  var answer = [];

  for (const [g, _] of total_array) {
    genre[g].sort((a, b) => (b[1] === a[1] ? a[0] - b[0] : b[1] - a[1]));

    let cnt = 0;
    for (const [idx, _] of genre[g]) {
      cnt++;
      answer.push(idx);

      if (cnt >= 2) break;
    }
  }
  console.log(genre);
  return answer;
}
