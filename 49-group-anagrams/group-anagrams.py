class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = defaultdict(list)

        for word in strs:
            anagram = ''.join(sorted(word))
            anagram_map[anagram].append(word)
        
        return [list(anagrams) for anagrams in anagram_map.values()]