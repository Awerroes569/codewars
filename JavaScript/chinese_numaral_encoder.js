var numerals = {
    "-": "负",
    ".": "点",
    0: "零",
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    6: "六",
    7: "七",
    8: "八",
    9: "九",
    10: "十",
    100: "百",
    1000: "千",
    10000: "万",
    undefined: '',
};

function trimAndReduce(char, str) {
    // Escape regex special characters
    const escaped = char.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

    // 1. Trim from start and end
    const trimRegex = new RegExp(`^${escaped}+|${escaped}+$`, "g");
    let result = str.replace(trimRegex, "");

    // 2. Reduce consecutive occurrences inside
    const reduceRegex = new RegExp(`${escaped}{2,}`, "g");
    result = result.replace(reduceRegex, char);

    return result;
}

// Examples
console.log(trimAndReduce("-", "--hello--"));      // "hello"
console.log(trimAndReduce("-", "--he--llo---"));   // "he-lo"
console.log(trimAndReduce("x", "xxxabxxcxxx"));    // "abxc"
console.log(trimAndReduce(".", "...a...b....c.")); // "a.b.c"
  

function toChineseNumeral(num) {
    

    var result = {
        tenthousands: 0,
        thousands: 0,
        hundreds: 0,
        tens: 0,
        ones: 0,
    }

    const numberToDecode = num.toString();
    const [aboveDecimal, belowDecimal] = numberToDecode.split('.');
    console.log('aboveDecimal: ' + aboveDecimal);
    console.log('belowDecimal: ' + belowDecimal);

    const minusSign = aboveDecimal.startsWith('-') ? numerals['-'] : '';
    console.log('minus sign: ' + minusSign);
    const absoluteAboveDecimal = aboveDecimal.startsWith('-') ? aboveDecimal.slice(1) : aboveDecimal;
    console.log('absolute above decimal: ' + absoluteAboveDecimal);

    const tenThousandsPlace = absoluteAboveDecimal.slice(0, -4);
    console.log('ten-thousands place: ' + tenThousandsPlace);
    const thousandsPlace = absoluteAboveDecimal.slice(-4, -3);
    console.log('thousands place: ' + thousandsPlace);
    const hundredsPlace = absoluteAboveDecimal.slice(-3, -2);
    console.log('hundreds place: ' + hundredsPlace);
    const tensPlace = absoluteAboveDecimal.slice(-2, -1);
    console.log('tens place: ' + tensPlace);
    const onesPlace = absoluteAboveDecimal.slice(-1);
    console.log('ones place: ' + onesPlace);

    let abovePart =
        (isNaN(+tenThousandsPlace) || +tenThousandsPlace === 0? numerals[0] : numerals[tenThousandsPlace] + numerals[10000]) +
        (isNaN(+thousandsPlace) || +thousandsPlace === 0 ? numerals[0] : numerals[thousandsPlace] + numerals[1000]) +
        (isNaN(+hundredsPlace) || +hundredsPlace === 0 ? numerals[0] : numerals[hundredsPlace] + numerals[100]) +
        (isNaN(+tensPlace) || +tensPlace === 0 ? numerals[0] : numerals[tensPlace] + numerals[10]) +
        (isNaN(+onesPlace) || +onesPlace === 0 ? ( +tensPlace === 0 ? numerals[0] : '') : numerals[onesPlace]);

    abovePart = trimAndReduce("零", abovePart);

    let resultString =
        minusSign +
        abovePart +
        (Boolean(belowDecimal) ? numerals['.'] + directTranslation(belowDecimal) : '');
    resultString = resultString[0] === '点' ? numerals[0] + resultString : resultString; // handle cases like 0.1
    resultString = resultString[0] === "一" && resultString[1] === "十" ? resultString.slice(1) : resultString; // handle case 0
    console.log('resultString: ' + resultString);
    return resultString;
    
}


function directTranslation(directNumber) {

    let result = [...directNumber.toString()].map(digit => numerals[digit]).join('');
    console.log("result", result);
    return result;
}



console.assert(directTranslation(10) === "一零", "directTranslation(10) should be 一零");
console.assert(directTranslation(0) === "零", "directTranslation(0) should be 零");
console.assert(directTranslation(1) === "一", "directTranslation(1) should be 一");
console.assert(directTranslation(2) === "二", "directTranslation(2) should be 二");
console.assert(directTranslation(3) === "三", "directTranslation(3) should be 三");
console.assert(directTranslation(4) === "四", "directTranslation(4) should be 四");
console.assert(directTranslation(5) === "五", "directTranslation(5) should be 五");
console.assert(directTranslation(6) === "六", "directTranslation(6) should be 六");
console.assert(directTranslation(7) === "七", "directTranslation(7) should be 七");
console.assert(directTranslation(8) === "八", "directTranslation(8) should be 八");
console.assert(directTranslation(9) === "九", "directTranslation(9) should be 九");
console.assert(directTranslation(11) === "一一", "directTranslation(11) should be 一一");
console.assert(directTranslation(20) === "二零", "directTranslation(20) should be 二零");
console.assert(directTranslation(99) === "九九", "directTranslation(99) should be 九九");
console.assert(directTranslation(12003568714) === "一二零零三五六八七一四", "directTranslation(12003568714) should be 一二零零三五六八七一四");

console.assert(toChineseNumeral(24681) === "二万四千六百八十一", "toChineseNumeral(24681) should be 二万四千六百八十一");
console.assert(toChineseNumeral(123.45) === "一百二十三点四五", "toChineseNumeral(123.45) should be 一百二十三点四五");
console.assert(toChineseNumeral(15547.778) === "一万五千五百四十七点七七八", "toChineseNumeral(15547.778) should be 一万五千五百四十七点七七八");
console.assert(toChineseNumeral(0.1) === "零点一", "toChineseNumeral(0.1) should be 零点一");

console.assert(toChineseNumeral(10) === "十", "toChineseNumeral(10) should be 十");

console.assert(toChineseNumeral(20) === "二十", "toChineseNumeral(20) should be 二十");
console.assert(toChineseNumeral(104) === "一百零四", "toChineseNumeral(104) should be 一百零四");
console.assert(toChineseNumeral(1004) === "一千零四", "toChineseNumeral(1004) should be 一千零四");
console.assert(toChineseNumeral(10004) === "一万零四", "toChineseNumeral(10004) should be 一万零四");
console.assert(toChineseNumeral(10000) === "一万", "toChineseNumeral(10000) should be 一万");

console.error(toChineseNumeral(10000 ));


/*
10 十
20 二十
104 一百零四
1004 一千零四
10004 一万零四
10000 一万
*/