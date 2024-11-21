var recoverSecret = function (triplets) {
    let characters = [];
    let queque = [];
    triplets.forEach(triplet => {
        queque.push([triplet[0], triplet[1]]);
        queque.push([triplet[1], triplet[2]]);
        queque.push([triplet[0], triplet[2]]);
        }
    );

    let [first, second] = queque.shift();
    characters.push(first);
    characters.push(second);
    queque.push([first, second]);

    while (queque.length) {
        let [first, second] = queque.shift();
        let indexFirst = characters.indexOf(first);
        let indexSecond = characters.indexOf(second);
        if (indexFirst === -1 && indexSecond === -1) {
            queque.push([first, second]);
        } else if (indexFirst === -1) {
            characters.splice(indexSecond, 0, first);
            queque.push([first, second]);
        } else if (indexSecond === -1) {
            characters.push(second);
            queque.push([first, second]);
        } else if (indexFirst > indexSecond) {
            characters.splice(indexFirst, 1);
            characters.splice(indexSecond, 0, first);
            queque.push([first, second]);
        }
    }
    return characters.join('');
}