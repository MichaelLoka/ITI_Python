def counting_vowles(sentence):
    vowles = 0
    for i in sentence:
        if i in "aeiou":
            vowles += 1
    print("Number of Vowles is: ", vowles)
    return vowles
