class Solution:

    #Basic encoding using 500 blocks and getting length with the ppadding
    #Without using non Ascii Characters
    def encode(self, strs: List[str]) -> str:
        return "".join(txt.encode('utf-8').hex() + "$" for txt in strs)

    def decode(self, s: str) -> List[str]:
        return [bytes.fromhex(h).decode('utf-8') for h in s.split("$")[:-1]]
