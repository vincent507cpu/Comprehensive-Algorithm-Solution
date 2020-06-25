import heapq

class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # Write your code here
        heapq.heapify(nums)
        topk = heapq.nlargest(k, nums)
        topk.sort()
        topk.reverse()
        return topk