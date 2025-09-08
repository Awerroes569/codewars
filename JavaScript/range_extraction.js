function transformToString(arr) {
    if (arr.length > 2) {
        return arr[0].toString() + '-' + arr[arr.length - 1]
    }
    else if (arr.length === 1) {
        return arr[0].toString();
    } else {
        return arr[0].toString() + ',' + arr[1].toString();
    }
}

function solution(list) {
    const superarray = [];

    while (list.length > 0) {
        const subarray = [];
        const initialItem = list.shift();
        subarray.push(initialItem);

        while (list.length > 0) {
            if (list[0] - subarray[subarray.length - 1] === 1) {
                const nextItem = list.shift();
                subarray.push(nextItem);
                if (list.length === 0) {
                    superarray.push(subarray);
                }
            }
            else if (list.length === 1) {
                superarray.push(subarray);
                superarray.push([list.shift()])
            } else {
                superarray.push(subarray);
                break;
            }
        }
    }
    const mappedToString = superarray.map(item => transformToString(item));
    const result = mappedToString.join(',');
    return result;
}