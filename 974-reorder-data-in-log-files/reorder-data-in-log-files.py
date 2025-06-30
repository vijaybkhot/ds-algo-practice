class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        non_letter_logs = []

        for idx, log in enumerate(logs):
            is_digit = True
            tokens = log.split(" ")
            identifier = tokens[0]
            content = tokens[1:]
            if content[0][0] in "abcdefghijklmnopqrstuvwxyz":
                letter_logs.append([content, identifier, log])
            else:
                non_letter_logs.append(log)
                
        
        letter_logs.sort(key=lambda x: (x[0], x[1]))
        res = [log for _, _, log in letter_logs]
        

        return res + non_letter_logs


        