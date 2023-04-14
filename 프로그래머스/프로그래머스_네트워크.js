function bfs(graph, v, start) {
  v[start] = true;
  var Q = [start];

  while (Q.length) {
    const now = Q.shift();
    for (let i = 0; i < graph[now].length; i++) {
      if (!v[i] && graph[now][i]) {
        v[i] = true;
        Q.push(i);
      }
    }
  }
}

function solution(n, computers) {
  var visitied = new Array(n).fill(false);
  var answer = 0;

  for (let i = 0; i < n; i++) {
    if (!visitied[i]) {
      answer++;
      bfs(computers, visitied, i);
    }
  }

  return answer;
}
