class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1_start = int(event1[0].split(":")[0]) + float(event1[0].split(":")[1])/100
        event1_end = int(event1[1].split(":")[0]) + float(event1[1].split(":")[1])/100
        event2_start = int(event2[0].split(":")[0]) + float(event2[0].split(":")[1])/100
        event2_end = int(event2[1].split(":")[0]) + float(event2[1].split(":")[1])/100

        return event1_start <= event2_end and event2_start <= event1_end