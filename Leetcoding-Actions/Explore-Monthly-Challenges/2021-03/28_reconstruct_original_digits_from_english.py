class Solution:
    def originalDigits(self, s: str) -> str:
        '''
        T: O(1) and S: O(1)
        '''
        char2digits = {
            "z": [0],
            "e": [0, 1, 3, 3, 5, 7, 8, 9],
            "r": [0, 3, 4],
            "o": [0, 1, 2, 4],
            "n": [1, 7, 9, 9],
            "t": [2, 3, 8],
            "w": [2],
            "h": [3, 8],
            "f": [4, 5],
            "u": [4],
            "i": [5, 6, 8, 9],
            "v": [5, 7],
            "s": [6, 7],
            "x": [6],
            "g": [8]
        }
        counter = Counter(s)
        digits = {}
        digits["0"] = counter["z"]
        digits["2"] = counter["w"]
        digits["4"] = counter["u"]
        digits["6"] = counter["x"]
        digits["8"] = counter["g"]
        digits["3"] = counter["h"] - digits["8"]
        digits["5"] = counter["f"] - digits["4"]
        digits["7"] = counter["v"] - digits["5"]
        digits["1"] = counter["o"] - digits["0"] - digits["2"] - digits["4"]
        digits["9"] = counter["i"] - digits["5"] - digits["6"] - digits["8"]
        
        ans = ""
        for digit in digits:
            if digits[digit] > 0:
                ans += digit * digits[digit]
        
        return ''.join(sorted(ans))
