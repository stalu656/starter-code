def vowelcount(string): 
      count = 0
      for i in range(len(string)): 
            letter = string[i].lower()
            if letter == “a” or letter == ‘e’ or letter == ‘i’ or letter == ‘o’ or letter == ‘u’: 
                 count = count + 1
      return count

print(vowelcount(“hello world”))
