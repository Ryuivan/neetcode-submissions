class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_map = {}

        for n in nums:
            if n in res_map:
                res_map[n] += 1
            else:
                res_map[n] = 1

        sorted_nums = sorted(res_map.keys(), key=lambda x: res_map[x], reverse=True)
        
        # Ambil k elemen pertama
        return sorted_nums[:k]