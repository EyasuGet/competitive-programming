# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

freq = defaultdict(int)

        for d in cpdomains:
            rep, domain = d.split(" ")
            freq[domain] += int(rep)
            subdom =  domain.split(".")
            if len(subdom) > 2:
                freq[".".join(subdom[1:])] += int(rep)
            freq["".join(subdom[-1])] += int(rep)
        
        ans = []
        for key,val in freq.items():
            ans.append(str(val) + " " + str(key))
        return ans