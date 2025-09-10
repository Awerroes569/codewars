function composeNewUsedCoins(usedCoins, coin) {
    let coinsConvertedToArray = usedCoins.split(',');
    coinsConvertedToArray.push(coin.toString());
    //console.log('arrays money', coinsConvertedToArray);
    coinsConvertedToArray.sort((a, b) => a - b);
    //console.log('sorted arrays money', coinsConvertedToArray);
    const result = coinsConvertedToArray.join(',');
    //console.log('result', result);
    return result;

}

function countChange(money, coins) {
    const solutions = new Set();
    const used = new Set();
    
    function useCoins(money, coins, usedCoins) {
        for (let coin of coins) {
            let newMoney = money - coin;
            //console.log("newMoney", money, coin, newMoney)
            if (newMoney < 0) {
                continue;
            }
            let newUsedCoins = composeNewUsedCoins(usedCoins, coin);
            if (!used.has(newUsedCoins)) {
                used.add(newUsedCoins);
                if (newMoney > 0) {
                    useCoins(newMoney, coins, newUsedCoins);
                } else {
                    solutions.add(newUsedCoins);
                }
            }
        }
    }

    useCoins(money, coins, '0');

    return solutions.size;
}
  
/*solutions
used collection
dto(money,coins, sofar)
for every coin:
    if new money>-1
    make new sofar
        if sofar not in used:
            add sofar to used
                if new money>0
                dto( new money, coins , sofar)
                else:
                    add sofar to solutions

                    */

composeNewUsedCoins('10,7,2,5,9', 4);
console.log('result', countChange(11, [5, 7]));