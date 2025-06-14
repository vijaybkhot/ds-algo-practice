class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
        
        return True
    # def __init__(self, size):
    #     self.parent = [-1]*(size+1)
    
    # def find(self, x):
    #     if self.parent[x] < 0:
    #         return x
    #     self.parent[x] = self.find(self.parent[x])
    #     return self.parent[x]
    
    # def union(self, x, y):
    #     rootX, rootY = self.find(x), self.find(y)
    #     if rootX == rootY:
    #         return False
        
    #     if self.parent[rootX] < self.parent[rootY]:
    #         self.parent[rootX] += self.parent[rootY]
    #         self.parent[rootY] = rootX
    #     else:
    #         self.parent[rootY] += self.parent[rootX]
    #         self.parent[rootX] = rootY
        
    #     return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_index_map = defaultdict(set)
        email_name_map = defaultdict(str)
        for idx, account in enumerate(accounts):
            name = account[0]
            emails = account[1:]
            for email in emails:
                email_index_map[email].add(idx)
                email_name_map[email] = name

        uf = UnionFind()
        # Union all emails in same index
        for key_email in email_index_map:
            uf.find(key_email)
            for idx in email_index_map[key_email]:
                emails = accounts[idx][1:]
                for email in emails:
                    uf.union(key_email, email)
        parent_email_map = defaultdict(list)

        for email in uf.parent:
            parent_email = uf.find(email)
            parent_email_map[parent_email].append(email)
        
        res = []

        for parent_email in parent_email_map:
            parent_name = email_name_map[parent_email]
            emails = parent_email_map[parent_email]
            curr_account = [parent_name, *sorted(emails)]
            res.append(curr_account)
        
        return res

        























#         # self.parent = [i for i in range(len(accounts))]
#         # self.emails_dict = defaultdict(set)
#         # for idx, acc in enumerate(accounts):
#         #     emails = acc[1:]
#         #     self.emails_dict[idx].add(emails)

#         # def find(x):
#         #     if self.parent[x] < 0:
#         #         return x
#         #     self.parent[x] = find(self.parent[x])
#         #     return self.parent[x]

#         # def union(x, y):
#         #     rootX = find(x)
#         #     rootY = find(y)
#         #     if rootX == rootY:
#         #         return False
#         #     if self.parent[rootX] > self.parent[rootY]:
#         #         rootX, rootY = rootY, rootX
            
#         #     self.parent[rootX] += self.parent[rootY]
#         #     self.parent[rootY] = rootX
#         #     return True

#         # root_set = set()
#         # acc_dict = defaultdict()
#         # res = []
#         # for idx, details in enumerate(accounts):
#         #     name = details[0]
#         #     emails = details[1:]
#         #     if name not in root_set:
#         #         root_set.add(name)
#         #         root = (name, idx)
#         #         for email in emails:
#         #             acc_dict[email] = root
#         #     elif name in root_set:
#         #         # Check for any intersection
#         #         existing_root = None
#         #         for email in emails:
#         #             if email in acc_dict:
#         #                 existing_root = acc_dict[email]
#         #         if existing_root:
#         #             for email in emails:
#         #                 acc_dict[email] = existing_root
#         #         else:
#         #             root = (name, idx)
#         #             for email in emails:
#         #                 acc_dict[email] = root
#         # rev_acc_dict = defaultdict(list)
#         # for email in acc_dict:
#         #     key = acc_dict[email]
#         #     rev_acc_dict[key].append(email)
        
#         # for key in rev_acc_dict:
#         #     user, idx = key
#         #     emails = rev_acc_dict[key]
#         #     emails.sort()
#         #     curr_acc = [user] + emails
#         #     res.append(curr_acc)


#         # return res

#         parent = {}

#         def find(x):
#             if parent[x] != x:
#                 parent[x] = find(parent[x])
#             return parent[x]

#         def union(x, y):
#             parent.setdefault(x, x)
#             parent.setdefault(y, y)
#             parent[find(x)] = find(y)

#         email_to_name = {}

#         # Step 1: For each email, initialize parent and map email -> name
#         for account in accounts:
#             name = account[0]
#             for email in account[1:]:
#                 if email not in parent:
#                     parent[email] = email
#                 email_to_name[email] = name

#         # Step 2: Union emails of the same account
#         for account in accounts:
#             first_email = account[1]
#             for email in account[2:]:
#                 union(first_email, email)

#         # Step 3: Group emails by their parent
#         groups = defaultdict(list)
#         for email in parent:
#             root = find(email)
#             groups[root].append(email)

#         # Step 4: Build final result
#         res = []
#         for root_email, emails in groups.items():
#             res.append([email_to_name[root_email]] + sorted(emails))

#         return res