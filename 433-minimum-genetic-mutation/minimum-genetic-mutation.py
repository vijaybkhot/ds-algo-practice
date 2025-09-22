class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        q = deque([(startGene, 0)])
        visited = set(startGene)

        def getMutations(gene):
            mutations = []
            for idx, char in enumerate(gene):
                for new_char in "ACGT":
                    if char == new_char:
                        continue
                    new_gene = [char for char in gene]
                    new_gene[idx] = new_char
                    new_gene = ''.join(new_gene)
                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        mutations.append(new_gene)
                    
            return mutations
        

        while q:
            curr_gene, level = q.popleft()
            if curr_gene == endGene:
                return level
            
            mutations = getMutations(curr_gene)

            for mutation in mutations:
                q.append((mutation, level+1))
        
        return -1
