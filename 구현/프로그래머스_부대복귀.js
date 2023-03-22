// 2
function solution(n, roads, sources, destination) {
  var dik = new Array(n + 1).fill(100001);
  var route = {};
  roads.forEach(([s, e]) => {
    route[s] = (route[s] || []).concat(e);
    route[e] = (route[e] || []).concat(s);
  });

  var Q = [[destination, 0]];
  dik[destination] = 0;
  while (Q.length) {
    var [now, cost] = Q.shift();

    for (var next of route[now]) {
      if (dik[next] > cost + 1) {
        dik[next] = cost + 1;
        Q.push([next, cost + 1]);
      }
    }
  }

  return sources.map((i) => (dik[i] < 100001 ? dik[i] : -1));
}
