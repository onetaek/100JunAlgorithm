// 최소공배수(LCM) 계산 함수
function getLCM(a, b) {
  let max = Math.max(a, b);
  let min = Math.min(a, b);
  let lcm = max;

  while (true) {
    if (lcm % min === 0) {
      return lcm;
    }
    lcm += max;
  }
}

function solution(arr) {
  let answer = 0;

  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      const lcm = getLCM(arr[i], arr[j]);
      answer += lcm;
    }
  }

  return answer;
}

// 테스트
const arr = [1, 2, 3];
console.log(solution(arr)); // 출력: 11