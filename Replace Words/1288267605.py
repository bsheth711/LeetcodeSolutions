class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ret = []
        words = sentence.split(' ')

        for word in words:

            best = word

            for root in dictionary:
                try:
                    i = word.index(root)

                    if i != 0:
                        continue

                    if len(best) > len(root):
                        best = root

                except:
                    pass

           
            ret.append(best)
             
        return ' '.join(ret)