function burnRope(raw, start) {
    let rope = [...raw];
    if (rope[start[0]][start[1]] !== "R") {
        return -1;
    } else {
        rope[start[0]][start[1]] = "";
    }
    let count = 0;
    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    let queue = [start];
     
    while (queue.length > 0) {
        let subqueue = [];
        while (queue.length > 0) {
            let current = queue.shift();
            for (let direction of directions) {
                let row = current[0] + direction[0];
                let col = current[1] + direction[1];
                try {
                    if (rope[row][col] === "R") {
                        rope[row][col] = "";
                        subqueue.push([row, col]);
                    }
                } catch (e) {
                    continue;
                }
            }  
        }
        if (subqueue.length > 0) {
            count++;
            queue = [...subqueue];
        }
    }
    return count;
}