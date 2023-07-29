class Solution(object):
    def toGoatLatin(self, sentence):
        
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
      
        words = sentence.split()
        
        
        res = []
        
       
        for i, word in enumerate(words):
           
            if word[0] in vowels:
               
                res.append(word + 'ma' + 'a'*(i+1))
            else:
                
                res.append(word[1:] + word[0] + 'ma' + 'a'*(i+1))
                
       
        return ' '.join(res)
    
txt= str(input())
s = Solution()
result = s.toGoatLatin(txt)
print(result)