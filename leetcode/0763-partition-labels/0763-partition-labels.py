class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = {}

        for idx, ch in enumerate(s):
            hash[ch] = idx

        size = 0
        end = 0
        i = 0

        output = []

        while i < len(s):

            if i > end:
                output.append(size)
                end = hash[s[i]]
                size = 0
            else:
                end = max(end, hash[s[i]])

            size += 1
            i += 1

        output.append(size)
        return output
        