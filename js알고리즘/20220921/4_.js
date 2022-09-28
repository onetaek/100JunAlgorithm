function solution(points){
    lean_1 = (points[1]-points[3])/(points[0]-points[2])
    lean_2 = (points[1]-points[5])/(points[0]-points[4])
    lean_3 = (points[3]-points[5])/(points[2]-points[4])

    if(lean_1 == lean_2 && lean_2 == lean_3){
        return 0
    }

    A = Math.sqrt(Math.pow(points[0]-points[2],2)+Math.pow(points[1]-points[3],2))
    B = Math.sqrt(Math.pow(points[0]-points[4],2)+Math.pow(points[1]-points[5],2))
    C = Math.sqrt(Math.pow(points[2]-points[4],2)+Math.pow(points[3]-points[5],2))
    S = (A + B + C) / 2
    return Math.sqrt(S*(S-A)*(S-B)*(S-C))*2
}

console.log(solution([0,0,0,5,5,0]))