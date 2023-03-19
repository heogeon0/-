function StoTime(str) {
  const [H, M, S] = str.split(":");
  return H * 3600 + M * 60 + S * 1;
}

function TimeToS(time) {
  let HH = (time / 3600) | 0;
  let MM = ((time / 60) | 0) % 60;
  let SS = time % 60;
  HH = HH > 9 ? HH : "0" + HH;
  MM = MM > 9 ? MM : "0" + MM;
  SS = SS > 9 ? SS : "0" + SS;
  return `${HH}:${MM}:${SS}`;
}

function solution(play_time, adv_time, logs) {
  const pt = StoTime(play_time);
  const at = StoTime(adv_time);

  const time_table = new Array(pt).fill(0);

  logs.forEach((log) => {
    let [s, e] = log.split("-");
    time_table[StoTime(s)] += 1;
    time_table[StoTime(e)] -= 1;
  });

  for (let i = 1; i < pt; i++) {
    time_table[i] += time_table[i - 1];
  }

  for (let i = 1; i < pt; i++) {
    time_table[i] += time_table[i - 1];
  }

  let sum = time_table[at - 1];
  let idx = 0;

  for (let i = at - 1; i < pt; i++) {
    if (sum < time_table[i] - time_table[i - at]) {
      sum = time_table[i] - time_table[i - at];
      idx = i - at + 1;
    }
  }

  console.log(idx);
  var answer = "";
  return TimeToS(idx);
}
