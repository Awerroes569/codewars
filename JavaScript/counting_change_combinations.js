function countChange(money, coins) {
    coins.sort((a, b) => a - b);
    const length = coins.length;

    function useCoins(money, startIndex) {
        if (money === 0) {
            return 1;
        }
        if (money < 0) {
            return 0;
        }

        let solutions = 0; 

        for (let i = startIndex; i < length; i++) {
            solutions += useCoins(money - coins[i], i);
        }

        return solutions;
    }

    return useCoins(money, 0);

}
let money = 4;
let coins = [1, 2];  
console.log('money', money, 'coins', coins, 'result', countChange(money, coins));