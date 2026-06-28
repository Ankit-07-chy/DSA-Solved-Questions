class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                px = self.find(x)
                py = self.find(y)

                if px == py:
                    return

                if self.rank[px] > self.rank[py]:
                    self.parent[py] = px
                elif self.rank[px] < self.rank[py]:
                    self.parent[px] = py
                else:
                    self.parent[py] = px
                    self.rank[px] += 1

        n = len(accounts)
        dsu = DSU(n)

        email_owner = {}

        # Union accounts having common emails
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_owner:
                    email_owner[email] = i
                else:
                    dsu.union(i, email_owner[email])

        # Store emails belonging to each parent
        merged = {}

        for i, account in enumerate(accounts):
            parent = dsu.find(i)

            if parent not in merged:
                merged[parent] = set()

            for email in account[1:]:
                merged[parent].add(email)

        result = []

        for parent, emails in merged.items():
            emails = sorted(emails)   # lexicographical order
            result.append([accounts[parent][0]] + emails)

        # only accounts having emails
        return [account for account in result if len(account) > 1]