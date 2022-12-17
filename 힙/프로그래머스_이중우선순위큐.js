function solution(operations) {
    const qq = []
    operations.forEach(operation => {
        let [key, value] = operation.split(' ')
        value = parseInt(value)
        switch (key) {
            case 'I':
                qq.unshift(value)  
                break
                
            case 'D':
                if (qq.length > 0) {
                    value > 0 ? qq.sort((a,b) => a - b) : qq.sort((a,b) => b - a) 
                    qq.pop()
                
                }
         
        }
    })
    var answer = qq.length > 0? [Math.max(...qq), Math.min(...qq)] : [0,0];
    return answer;
}