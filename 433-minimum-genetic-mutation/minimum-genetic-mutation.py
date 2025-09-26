from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        begin_set, end_set = {startGene}, {endGene}
        visited = set()
        steps = 0
        choices = "ACGT"
        
        while begin_set and end_set:
            # Always expand the smaller set
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            
            next_level = set()
            for gene in begin_set:
                if gene in end_set:
                    return steps
                
                visited.add(gene)
                for idx, char in enumerate(gene):
                    for new_char in choices:
                        if new_char == char:
                            continue
                        mutation = gene[:idx] + new_char + gene[idx+1:]
                        if mutation in bank and mutation not in visited:
                            next_level.add(mutation)
            
            begin_set = next_level
            steps += 1
        
        return -1
