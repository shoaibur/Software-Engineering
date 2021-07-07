class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        '''
        T: O(n) and S: O(m)
        n = # of integers in arr
        m = # of integers in pieces
        '''
        piecesDict = {}
        for item in pieces:
            piecesDict[item[0]] = item
        
        i = 0
        while i < len(arr):
            
            if arr[i] in piecesDict:
                if len(piecesDict) == 0: return False
                
                piece = piecesDict[arr[i]]
                L = len(piece)
                if arr[i:i+L] == piece:
                    piecesDict.pop(arr[i])
                    i += L
                else:
                    i += 1
            else:
                i += 1
        
        return len(piecesDict) == 0
