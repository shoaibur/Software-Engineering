class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        '''
        T: O(n)
        S: O(26) = O(1); to store seen set.
        '''
        if len(A) != len(B): return False
        
        if A == B:
            seen = set()
            for char in A:
                if char in seen:
                    return True
                seen.add(char)
            return False
        
        a, b = [], []
        for i in range(len(A)):
            if A[i] != B[i]:
                a.append(A[i])
                b.append(B[i])
                if len(a) > 2: return False
        if len(a) != 2: return False
        if a[::-1] != b: return False
        
        return True

    
    
    # In Java
    '''
    class Solution {
    public boolean buddyStrings(String A, String B) {
        if (A.length() != B.length()) {
            return false;
        }
        if (A.equals(B)) {
            
            HashSet<Character> seen = new HashSet<>();
            for (int i = 0; i < A.length(); i++) {
                if (seen.contains(A.charAt(i))) {
                    return true;
                }
                seen.add(A.charAt(i));
            }
            return false;
        }
        ArrayList<Character> a = new ArrayList<>();
        ArrayList<Character> b = new ArrayList<>();
        for (int i = 0; i < A.length(); i++) {
            if (A.charAt(i) != B.charAt(i)) {
                a.add(A.charAt(i));
                b.add(B.charAt(i));
                if (a.size() > 2) {
                    return false;
                }
            }
        }
        if (a.size() != 2) {
            return false;
        }
        if (a.get(0) != b.get(1) || a.get(1) != b.get(0)) {
            return false;
        }
        return true;
    }
}
    '''
