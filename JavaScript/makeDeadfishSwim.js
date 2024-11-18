function parse(data) {
    let result = [];
    let current = 0;
    const actions = {
        i: () => current++,
        d: () => current--,
        s: () => current *= current,
        o: () => result.push(current)
    };
    for (let instruction of data) {
        try {
            actions[instruction]();
        }
        catch (e) {
            continue;
        }
        actions[instruction]();
    }
    return result; 
}
