class Solution(object):
    def quickSort(self,arr,low,high):
        if low < high:
            pivot_index=self.partition(arr, low, high)
            self.quickSort(arr,low,pivot_index-1)
            self.quickSort(arr,pivot_index+1,high)
    def partition(self,arr,low,high):
        pivot=arr[high]
        i=low - 1
        for j in range(low,high):
            if arr[j]<=pivot:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i + 1],arr[high]=arr[high],arr[i + 1]
        return i+1
    def targetIndices(self,nums,target):
        self.quickSort(nums,0,len(nums)-1)
        result=[]
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)
        return result