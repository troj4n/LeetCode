################################### Solution 1 ########################################
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
        
