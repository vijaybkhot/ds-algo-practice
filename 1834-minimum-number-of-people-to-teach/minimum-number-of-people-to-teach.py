from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        conflict_users = set()
        for u, v in friendships:
            if not set(languages[u-1]) & set(languages[v-1]):  # no common language
                conflict_users.add(u)
                conflict_users.add(v)

        if not conflict_users:
            return 0

        lang_count = defaultdict(int)
        for user in conflict_users:
            for lang in languages[user-1]:
                lang_count[lang] += 1

        max_freq = max(lang_count.values())
        return len(conflict_users) - max_freq
