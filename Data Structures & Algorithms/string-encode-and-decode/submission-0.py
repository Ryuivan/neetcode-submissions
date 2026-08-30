class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''

        for s in strs:
            encoded_string += str(len(s)) + '#' + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        left = 0
        
        while left < len(s):
            right = left

            while s[right] != '#':
                right += 1

            word_count = int(s[left:right])
            word = s[right + 1:right + 1 + word_count]
            decoded_string.append(word)

            left = right + 1 + word_count
        
        return decoded_string