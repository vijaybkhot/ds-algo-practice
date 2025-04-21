class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # # First attempt:
        # if n == 1 and not trust:
        #     return 1
        # trust_map = {}
        # judge = -1
        # for fromTrust, toTrust in trust:
        #     if toTrust not in trust_map:
        #         trust_map[toTrust] = [set(), set()]
        #     if fromTrust not in trust_map:
        #         trust_map[fromTrust] = [set(), set()]
        #     trust_map[toTrust][0].add(fromTrust)
        #     trust_map[fromTrust][1].add(toTrust)
        # for person in trust_map:
        #     if len(trust_map[person][0]) == n-1 and len(trust_map[person][1]) == 0:
        #         judge = person
        
        # return judge

        # Second attempt:
        trust_map = {}
        for person in range(1, n+1):
            trust_map[person] = [0, 0]  # trustOut, trustIn
        judge = -1
        for trustOut, trustIn in trust:
            trust_map[trustOut][1] += 1
            trust_map[trustIn][0] += 1
            
        for person in trust_map:
            if trust_map[person][0] == n-1 and trust_map[person][1] == 0:
                judge = person
        
        return judge
        