def keypad_combinations(nums):
    num2letters = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz', '0':'', '1':''}
    words = [num2letters[num] for num in nums]
    x = [letter for letter in words[0]]
    for word in words[1:]:
      out = []
        y = [letter for letter in word]
        for char in y:
            for item in x:
                out.append(item + char)
        x = out
    return out
  
