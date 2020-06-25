# my solution

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dct = {}
        
        for domain in cpdomains:
            num, parent = domain.split()
            
            dct[parent] = dct.get(parent, 0) + int(num)
            
            while '.' in parent:
                parent = parent[parent.find('.')+1:]
                dct[parent] = dct.get(parent, 0) + int(num)
                
        return [str(num)+' '+domain for domain, num in dct.items()]