class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)
        for s in strs:
            lookup_list = [0]*26
            for i in s:
                lookup_list[ord(i)-ord('a')]+=1
            ana_map[tuple(lookup_list)].append(s)
        return list(ana_map.values())