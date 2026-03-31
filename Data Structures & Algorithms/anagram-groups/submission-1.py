class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_data = {}
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch) - ord('a')] +=1
            key = tuple(count)
            if key not in map_data:
                map_data[key] = []
            map_data[key].append(word)
        return list(map_data.values())
        


        