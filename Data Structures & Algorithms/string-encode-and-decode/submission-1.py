class Solution:
    SEPARATOR = "#!_"

    def encode(self, strs: List[str]) -> str:
        strs_encoded = []
        for curr_str in strs:
            strs_encoded.append(self.SEPARATOR)
            strs_encoded.append(str(len(curr_str)))
            strs_encoded.append(self.SEPARATOR)
            strs_encoded.append(curr_str)
        return ''.join(strs_encoded)
        

    def decode(self, s: str) -> List[str]:
        strs_decoded = []
        current_index = 0
        sep_len = len(self.SEPARATOR)
        while(current_index < len(s)):
            current_index += sep_len
            next_div = s.index(self.SEPARATOR, current_index)
            str_len = int(s[current_index:next_div])
            current_index = next_div + sep_len
            strs_decoded.append(s[current_index:current_index+str_len])
            current_index+=str_len
        return strs_decoded