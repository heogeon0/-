function solution(routes) {
  routes.sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]));

  let stand = -30001;
  var answer = 0;

  console.log(routes);

  routes.forEach(([s, e]) => {
    if (s > stand) {
      stand = e;
      answer++;
    }

    if (e < stand) {
      stand = e;
    }
  });

  return answer;
}
