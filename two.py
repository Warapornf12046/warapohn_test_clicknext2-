def are_texts_similar(s1, s2):
    if len(s1) != len(s2):
        return False

    count1 = [0] * 26   
    count2 = [0] * 26
    for i in range(len(s1)):
        pos1 = ord(s1[i].lower()) - ord('a')
        pos2 = ord(s2[i].lower()) - ord('a')
         
        count1[pos1] += 1
        count2[pos2] += 1

    for i in range(26):
        if count1[i] != count2[i]:
            return False

    return True

print(are_texts_similar("Mary", "Army"))     
print(are_texts_similar("Maryy", "Armyy"))   
print(are_texts_similar("Maryy", "Army"))    
print(are_texts_similar("Marym", "Armyy"))  