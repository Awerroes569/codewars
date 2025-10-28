function finance(n) {
    let result = 0;
    for (let i = 0; n; i++){
        result += (3 * i / 2) * (i + 1);
    }
    return result
}