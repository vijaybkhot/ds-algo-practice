class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words:
            return []
        str_groups = [[words[0]]]
        curr_group = words[0]

        for word in words[1:]:
            new_group = curr_group
            new_group += " " + word
            if len(new_group) <= maxWidth:
                curr_group = new_group
                str_groups[-1].append(word)
            else:
                str_groups.append([word])
                curr_group = word
        
        res = []
        for idx, group in enumerate(str_groups):
            available_spaces = maxWidth - sum(len(s) for s in group)
            if idx == len(str_groups)-1:
                justified_word = ""
                for i in range(len(group)):
                    justified_word += group[i] + " "
                justified_word = justified_word[:-1]
                print(justified_word)
                left_over_spaces = maxWidth - len(justified_word)
                justified_word += " "* left_over_spaces
                res.append(justified_word)
                continue
            else:
                if len(group) == 1:
                    res.append(group[0] + " " * available_spaces)
                    continue
                else:
                    num_gaps = len(group) - 1
                    space_per_gap = available_spaces // num_gaps
                    extra_spaces = available_spaces % num_gaps

                    justified_word = ""
                    for i in range(num_gaps):
                        justified_word += group[i]
                        # Add extra space to the leftmost gaps
                        spaces_to_add = space_per_gap + (1 if i < extra_spaces else 0)
                        justified_word += ' ' * spaces_to_add
                    justified_word += group[-1]  # last word
                    res.append(justified_word)

                
        return res

