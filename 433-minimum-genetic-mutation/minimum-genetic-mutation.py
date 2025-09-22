from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if startGene == endGene:
            return 0
        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])
        visited = {startGene}

        def getMutations(gene):
            mutations = []
            for idx, ch in enumerate(gene):
                for new_char in "ACGT":
                    if ch == new_char:
                        continue
                    new_gene = gene[:idx] + new_char + gene[idx+1:]
                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)      # mark when discovered
                        mutations.append(new_gene)
            return mutations

        while q:
            curr_gene, level = q.popleft()
            if curr_gene == endGene:
                return level
            for m in getMutations(curr_gene):
                q.append((m, level + 1))

        return -1
