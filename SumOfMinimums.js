function sumOfMinimums(arr) {
    let count = 0;
    const arr = [...arr];
    for (row of arr) {
        count += Math.min(...row);
    }
    return count;
}