################################### Solution 1 (Word by Word matching) ########################################
class Solution:
    def commonPrefix(self,str1,str2):
        result=""
        n1=len(str1)
        n2=len(str2)
        i=0
        j=0
        while i<n1 and j<n2:
            if str1[i]!=str2[j]:
                break
            result+=str1[i]
            i+=1
            j+=1
        return result
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        n=len(strs)
        prefix=strs[0]
        if n==1:
            return prefix
        for i in range(1,n):
            prefix=self.commonPrefix(prefix,strs[i])
            #print (prefix)
        return (prefix)
        
######################################################  solution2 (chracter matching) ###################################

class Solution:
    
    def minimimLength(self,strs,n):
        min_len=len(strs[0])
        for i in range(1,n):
            x=len(strs[i])
            if x<min_len:
                min_len=x
        return min_len 
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        n=len(strs)
        if n==1:
            return strs[0]
        
        result=""
        minlen=self.minimimLength(strs,n)
        for i in range(minlen):
            curr=strs[0][i]
            for j in range(1,n):
                if strs[j][i]!=curr:
                    return result
            result=result+curr
        return (result)
