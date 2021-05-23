class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        mat=[[0 for i in range(y+1)] for j in range(x+1)]
        for i in range(x+1):
            for j in range(y+1):
                if i==0 or j==0:
                    mat[i][j]=0
                elif s1[i-1]==s2[j-1]:
                    mat[i][j]=mat[i-1][j-1]+1
                else:
                    mat[i][j]=max(mat[i][j-1],mat[i-1][j])
        return mat[-1][-1]
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
