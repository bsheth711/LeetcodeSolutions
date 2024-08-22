class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for detail in details:
            if detail[11] > '6' or (detail[11] == '6' and detail[12] != '0'):
                res += 1
        
        return res
        