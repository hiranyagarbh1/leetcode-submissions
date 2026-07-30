# Last updated: 30/07/2026, 15:41:36
1class Solution:
2    def topKFrequent(self, words: List[str], k: int) -> List[str]:
3
4        counts = Counter(words)
5
6        sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
7        
8        return [word for word, freq in sorted_words[:k]]
9        