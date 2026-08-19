class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        res = []
        for i in nums:
            freq_map[i]+=1
        freq_list = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            res.append(freq_list[i][0])
        return res