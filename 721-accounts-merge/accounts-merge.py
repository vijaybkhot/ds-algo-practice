class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # self.parent = [i for i in range(len(accounts))]
        # self.emails_dict = defaultdict(set)
        # for idx, acc in enumerate(accounts):
        #     emails = acc[1:]
        #     self.emails_dict[idx].add(emails)

        # def find(x):
        #     if self.parent[x] < 0:
        #         return x
        #     self.parent[x] = find(self.parent[x])
        #     return self.parent[x]

        # def union(x, y):
        #     rootX = find(x)
        #     rootY = find(y)
        #     if rootX == rootY:
        #         return False
        #     if self.parent[rootX] > self.parent[rootY]:
        #         rootX, rootY = rootY, rootX
            
        #     self.parent[rootX] += self.parent[rootY]
        #     self.parent[rootY] = rootX
        #     return True

        # root_set = set()
        # acc_dict = defaultdict()
        # res = []
        # for idx, details in enumerate(accounts):
        #     name = details[0]
        #     emails = details[1:]
        #     if name not in root_set:
        #         root_set.add(name)
        #         root = (name, idx)
        #         for email in emails:
        #             acc_dict[email] = root
        #     elif name in root_set:
        #         # Check for any intersection
        #         existing_root = None
        #         for email in emails:
        #             if email in acc_dict:
        #                 existing_root = acc_dict[email]
        #         if existing_root:
        #             for email in emails:
        #                 acc_dict[email] = existing_root
        #         else:
        #             root = (name, idx)
        #             for email in emails:
        #                 acc_dict[email] = root
        # rev_acc_dict = defaultdict(list)
        # for email in acc_dict:
        #     key = acc_dict[email]
        #     rev_acc_dict[key].append(email)
        
        # for key in rev_acc_dict:
        #     user, idx = key
        #     emails = rev_acc_dict[key]
        #     emails.sort()
        #     curr_acc = [user] + emails
        #     res.append(curr_acc)


        # return res

        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            parent[find(x)] = find(y)

        email_to_name = {}

        # Step 1: Union all emails that belong to the same account
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                union(first_email, email)
                email_to_name[email] = name

        # Step 2: Group emails by their root parent
        root_to_emails = defaultdict(list)
        for email in email_to_name:
            root_email = find(email)
            root_to_emails[root_email].append(email)

        # Step 3: Build the merged accounts
        res = []
        for root_email, emails in root_to_emails.items():
            name = email_to_name[root_email]
            res.append([name] + sorted(emails))

        return res

        
        