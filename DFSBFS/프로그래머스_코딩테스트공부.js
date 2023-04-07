function solution(alp, cop, problems) {
  var timeTable = new Array(301).fill(0).map((i) => new Array(2).fill([]));
  problems.push([0, 0, 1, 0, 1], [0, 0, 0, 1, 1]);

  const q = [alp, cop, 0];
  console.log(timeTable);
  //     while (q.length) {
  //         let [nalp, nclp, time] = q.shift()

  //         problems.forEach(([alp_req, cop_req, alp_rwd, cop_rwd, cost]) => {
  //             if (nalp >= alp_req && nclp >= cop_req) {
  //                 nalp += alp_rwd
  //                 nclp += cop_rwd

  //                 time += cost

  //             }
  //         })
  //     }
  var answer = 0;
  return answer;
}
