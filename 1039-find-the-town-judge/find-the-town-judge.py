class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if len(trust) > n-1:
        #     return -1
        
        # judge = trust[0][1]

        # for i in range(1, len(trust)):
        #     if trust[i][1] != judge:
        #         return -1
        
        # return judge
        if n == 1 and not trust:
            return 1
        trust_map = {}
        judge = -1
        for fromTrust, toTrust in trust:
            if toTrust not in trust_map:
                trust_map[toTrust] = [set(), set()]
            if fromTrust not in trust_map:
                trust_map[fromTrust] = [set(), set()]
            trust_map[toTrust][0].add(fromTrust)
            trust_map[fromTrust][1].add(toTrust)
        for person in trust_map:
            if len(trust_map[person][0]) == n-1 and len(trust_map[person][1]) == 0:
                judge = person
        
        return judge
        