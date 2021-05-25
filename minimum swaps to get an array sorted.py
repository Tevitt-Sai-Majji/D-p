class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        n=len(nums)
        l=[]
        for i in range(n):
            p=[]
            p.append(nums[i])
            p.append(i)
            l.append(p)
        l.sort(key=lambda x:x[0])
        vi=[False for i in range(n)]
        swaps=0
        for i in range(n):
            if vi[i] or l[i][1]==i:
                continue
            cyc=0
            j=i
            while not vi[j]:
                vi[j]=True
                j=l[j][1]
                cyc+=1
            if cyc>0:
                swaps+=(cyc-1)
        return swaps
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minSwaps(nums)
        print(ans)
