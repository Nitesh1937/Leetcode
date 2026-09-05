class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp=""
        j=0
        for i in range(1,len(strs)):
            while j < len(strs[0]) and j < len(strs[i]) and strs[0][j] == strs[i][j]:
                temp+=strs[0][j]
                j+=1
            strs[0]=temp
            temp=""  
            j=0
            
        return strs[0]