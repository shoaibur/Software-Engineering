class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        uniqueEmails = set()
        for email in emails:
            local, domain = email.split('@')
            local = ''.join(local.split('.'))
            local = local.split('+')[0]
            uniqueEmails.add(f"{local}@{domain}")
        return len(uniqueEmails)
