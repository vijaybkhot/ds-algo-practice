class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
       

        q = deque()
        q.append((startGene, 0))    # Gene, mutations
        visited = set()
        visited.add(startGene)

        while q:
            gene, mutation = q.popleft()
            if gene == endGene:
                return mutation
            
            for idx in range(len(gene)):
                new_gene = [char for char in gene]
                char_set = set(["A", "C", "G", "T"])
                curr_char = new_gene[idx]
                char_set.remove(curr_char)
                for new_char in char_set:
                    new_gene[idx] = new_char
                    new_gene_str = ''.join(new_gene)
                    print(new_gene_str)
                    if new_gene_str in bank_set and new_gene_str not in visited:
                        print(new_gene_str)
                        visited.add(new_gene_str)
                        q.append((new_gene_str, mutation+1))
        
        return -1

