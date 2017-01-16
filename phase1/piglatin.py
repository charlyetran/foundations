def translate():
    vowels = ['a','e','i','o','u']
    sentence = input('Translate phrase into Pig Latin:  ')
    sentence = sentence.split()

    for i in range(len(sentence)):
        word = sentence[i]

        if word[0] in vowels:
            sentence[i] = word +'way'
        elif word[0] not in vowels:
            # sentence[i] = word[1:] + word[0] + 'ay'

            prefix = ''
            for j in range(len(word)):
                if word[j] in vowels:
                    break
                else:
                    prefix += word[j]

            sentence[i] = word[len(prefix):] + prefix + 'ay'
        else:
            sentence[i] = word

    return ' '.join(sentence)


if __name__ == '__main__':
    print(translate())