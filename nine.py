def revert_words(sentence):
  words = sentence.split()
  reversed_words = [word[::-1] for word in words]
 
  reversed_sentence = " ".join(reversed_words)

  return reversed_sentence

sentence = "Welcome to clicknext"
reversed_sentence = revert_words(sentence)
print(reversed_sentence)