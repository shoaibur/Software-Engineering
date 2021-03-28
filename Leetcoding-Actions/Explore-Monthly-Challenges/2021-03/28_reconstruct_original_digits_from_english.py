class Solution:
    def originalDigits(self, s: str) -> str:
        '''
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
        
        T: O(1) and S: O(1)
        
        '''
        char_counter = Counter(s)
        digit_counter = {}
        digit_counter["0"] = char_counter["z"]
        digit_counter["2"] = char_counter["w"]
        digit_counter["4"] = char_counter["u"]
        digit_counter["6"] = char_counter["x"]
        digit_counter["8"] = char_counter["g"]
        digit_counter["3"] = char_counter["h"] - digit_counter["8"]
        digit_counter["5"] = char_counter["f"] - digit_counter["4"]
        digit_counter["7"] = char_counter["v"] - digit_counter["5"]
        digit_counter["1"] = char_counter["o"] - digit_counter["0"] - digit_counter["2"] - digit_counter["4"]
        digit_counter["9"] = char_counter["i"] - digit_counter["5"] - digit_counter["6"] - digit_counter["8"]
        
        original_digits = ""
        for digit in digit_counter:
            if digit_counter[digit] > 0:
                original_digits += digit * digit_counter[digit]
        
        return ''.join(sorted(original_digits))
