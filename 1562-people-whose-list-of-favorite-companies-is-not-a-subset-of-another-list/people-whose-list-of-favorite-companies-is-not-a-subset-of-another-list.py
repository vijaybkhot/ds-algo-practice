class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        company_index_map = defaultdict(set)
        for idx, companies in enumerate(favoriteCompanies):
            for company in companies:
                company_index_map[company].add(idx)
        
        res = []
        for idx, companies in enumerate(favoriteCompanies):
            set_intersect = None
            for company in companies:
                if set_intersect is None:
                    set_intersect = company_index_map[company]
                else:
                    set_intersect = set_intersect & company_index_map[company]
            set_intersect.remove(idx)
            if len(set_intersect) == 0:
                res.append(idx)
        
        return res