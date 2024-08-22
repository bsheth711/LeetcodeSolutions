class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ret = []
        words = sentence.split(' ')

        for word in words:

            best = None

            for root in dictionary:
                try:
                    i = word.index(root)

                    if i != 0:
                        continue

                    if best:
                        if len(best) > len(root):
                            best = root
                    else:
                        best = root 

                except:
                    pass

           
            if best:
                ret.append(best)
            else:
                ret.append(word)
             
        return ' '.join(ret)