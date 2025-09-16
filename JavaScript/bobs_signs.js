var SignMaster = function () {
    this.prices = {};
};

SignMaster.prototype.changePrices = function (prices) {
    this.prices = prices;
};

SignMaster.prototype.estimatePrice = function (oldSign, newSign) {
    const addCost = this.prices.add;
    const removeCost = this.prices.rem;

    console.log('addCost', addCost, 'removeCost', removeCost);

    //ESTIMATE REMOVING ITEMS
    //to remove = new sign - remove old signs
    let oldSignItems = Array.from(oldSign);
    console.log('oldSignItems', oldSignItems);
    let newSignItems = Array.from(newSign);
    console.log('newSignItems', newSignItems);

    let oldToModify = oldSign;
    let newToModify = newSign;

    for (let char of newSignItems) {
        oldToModify = oldToModify.replace(char, '');
    }
    for (let char of oldSignItems) {
        newToModify = newToModify.replace(char, '');
    }

    console.log('oldToModify', oldToModify);
    console.log('newToModify', newToModify);
    const removingCost = oldToModify.length * this.prices.rem;
    const addingCost = newToModify.length * this.prices.add;
    console.log('total cost', removingCost + addingCost);
    return removingCost + addingCost;
};

const sm = new SignMaster();

//oldToModify 1cen8fom6j97zq69tvf
//newToModify c6d5j3p5balqk8x92eg

sm.changePrices({ 'add': 50, 'rem': 36 });
sm.estimatePrice('1cen8fom6j97zq69tvf', 'c6d5j3p5balqk8x92eg');

