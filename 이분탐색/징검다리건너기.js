function solution(stones, k) {
  var s = 1, e = 200000000
  var answer = 0;
  
  while (s <= e) {
      var mid = Math.floor((s + e) / 2)
      var flag= 0, cnt = 0
      
      for (var i = 0; i<stones.length; i++) {
          if (stones[i] - mid < 0 ) cnt ++
          else cnt = 0
          
          if (cnt >= k) {
              flag = 1
              break
          }
      }
      

      if (flag) {
          e = mid - 1
      }
      else {
          s = mid + 1
          answer = mid
      }
  }
  
  return answer;
}