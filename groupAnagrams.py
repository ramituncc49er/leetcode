"""Sorting with HashMaps"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        olist = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            olist[sortedS].append(s)
        return list(olist.values())

"""HashTables with Element frequency"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        olist = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            olist[tuple(freq)].append(s)
        return list(olist.values())