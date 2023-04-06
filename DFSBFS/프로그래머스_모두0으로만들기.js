function solution(a, edges) {
  const tree = new Array(a.length).fill(0).map((i) => new Array());
  const visit = new Array(a.length).fill(false);
  edges.forEach(([a, b]) => {
    tree[a].push(b);
    tree[b].push(a);
  });

  var sum = 0n;
  const stack = [[0, -1]];

  while (stack.length) {
    const [now, parent] = stack.pop();

    if (visit[now]) {
      a[parent] += a[now];
      sum += BigInt(Math.abs(a[now]));
      continue;
    }
    visit[now] = true;
    stack.push([now, parent]);

    for (const next of tree[now]) {
      if (!visit[next]) {
        stack.push([next, now]);
      }
    }
  }

  return a[0] ? -1 : sum;
}
