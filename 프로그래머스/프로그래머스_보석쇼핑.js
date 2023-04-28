function solution(gems) {
  var [start, end] = [0, 0];
  var target = new Set(gems);
  var answer = [0, gems.length + 1];
  var lst = new Map();

  lst.set(gems[0], 1);

  while (end < gems.length) {
    if (lst.size === target.size) {
      if (end - start < answer[1] - answer[0]) answer = [start + 1, end + 1];
      lst.set(gems[start], lst.get(gems[start]) - 1);
      if (lst.get(gems[start]) === 0) lst.delete(gems[start]);
      start += 1;
    } else {
      end++;
      lst.set(gems[end], (lst.get(gems[end]) || 0) + 1);
    }
  }

  return answer;
}
