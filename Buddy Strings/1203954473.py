class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        wrong = 0
        comboCount = defaultdict(lambda: 0)
        count = defaultdict(lambda: 0)

        for i, (a, b) in enumerate(zip(s, goal)):
            if a != b:
                wrong += 1

            comboCount[a] += 1
            comboCount[b] -= 1

            count[a] += 1

        for letter in comboCount:
            if comboCount[letter] != 0:
                return False
        
        hasSame = False

        for letter in count:
            if count[letter] >= 2:
                hasSame = True
                break
        
        if wrong != 2 and not (wrong == 0 and hasSame):
            return False
        
        return True
        