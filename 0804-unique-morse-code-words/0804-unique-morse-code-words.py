class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
         "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
         "..-","...-",".--","-..-","-.--","--.."]

        morse_index = {}
        for i in range(len(morse)):
            morse_index[i] = morse[i]

        letter = "abcdefghijklmnopqrstuvwxyz"
        letter_index = {}
        for i in range(len(letter)):
            letter_index[letter[i]] = i

        def change(inner):
            res = ""
            for ch in inner:
                idx = letter_index[ch]
                res += morse_index[idx]
            return res

        result = set()
        for word in words:
            name = change(word)
            result.add(name)

        return len(result)

                

            

        