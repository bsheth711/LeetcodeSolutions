/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function(k, n) {
    res = [];
    dfs(res, [], 0, k, n, 1);
    return res;
    
};

function dfs(res, cur, curTotal, k, n, start) {
    if (cur.length == k && curTotal == n) {
        res.push([...cur]);
        return;
    }
    else if (cur.length > k || curTotal >= n) {
        return;
    }

    for (let i = start; i < 10; ++i) {
        cur.push(i);
        dfs(res, cur, curTotal + i, k, n, start = i + 1);
        cur.pop();
    }
}