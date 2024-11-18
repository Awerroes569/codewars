function wave(str) {
    let result = [];
    const characters = str.split('');
    for (let i = 0; i < str.length; i++) {
        if (str[i] === ' ') {
            continue;
        }
        let wavedCharacters = [...characters];
        wavedCharacters.splice(i, 1, characters[i].toUpperCase());
        let wave = wavedCharacters.join('');
        result.push(wave);
    }
    return result;
}
