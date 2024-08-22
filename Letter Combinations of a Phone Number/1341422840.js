/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const mapping = new Map([
        ['2', ['a', 'b', 'c']],
        ['3', ['d', 'e', 'f']],
        ['4', ['g', 'h', 'i']],
        ['5', ['j', 'k', 'l']],
        ['6', ['m', 'n', 'o']],
        ['7', ['p', 'q', 'r', 's']],
        ['8', ['t', 'u', 'v']],
        ['9', ['w', 'x', 'y', 'z']],
    ]);

    res = [];

    dfs(res, [], digits, mapping);

    return res;
};

function dfs(res, cur, digits, mapping) { 
    if (cur.length === digits.length) {
        if (cur.length > 0) {
            res.push(cur.join(''));
        }
        return;
    }

    for (const letter of mapping.get(digits[cur.length])) {
        cur.push(letter);
        dfs(res, cur, digits, mapping);
        cur.pop();
    }
};