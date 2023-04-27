function solution(user_id, banned_id) {
  const answer = new Set();
  const v = new Array(user_id.length).fill(0);

  var dfs = (idx) => {
    if (idx === banned_id.length) {
      answer.add(v.join(""));
      return;
    }

    const regex = new RegExp(banned_id[idx].replaceAll("*", "."));

    for (let user = 0; user < user_id.length; user++) {
      if (v[user] === 1) continue;

      if (
        user_id[user].length === banned_id[idx].length &&
        user_id[user].match(regex)
      ) {
        v[user] = 1;
        dfs(idx + 1);
        v[user] = 0;
      }
    }
  };

  dfs(0);
  console.log(answer);
  return answer.size;
}
