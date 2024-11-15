function minRepeatingCharacterDifference(text) {
    let characters = {};
    if (text.length < 2) return null;
    for (let i = 0; i < text.length - 1; i++) {
        let character = text[i];
        let diff = text.indexOf(character, i + 1) - i;
        if (diff + i === -1) {
            continue;
        } else if (diff === 1) {
            return [1, character];
        } else if (characters[diff] === undefined) {
            characters[diff] = [character];
        } else {
            characters[diff].push(character);
        }
    }
    if (Object.keys(characters).length === 0) return null;

    let minKey = Object.keys(characters).sort((a,b) => a - b)[0];

    let character = characters[minKey][0];

    return [parseInt(minKey), character];
}

console.log(minRepeatingCharacterDifference('aa'));