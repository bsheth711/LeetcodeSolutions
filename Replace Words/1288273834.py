class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ret = []
        words = sentence.split(' ')
        roots = set(dictionary)

        for word in words:

            cur = ''

            for i in range(len(word)):
                cur = word[:i + 1]
                if cur in roots:
                    break
            
            ret.append(cur)

        return ' '.join(ret)