# mask是一个10位十进制的数，某一个为1，则该位的字母为奇数个
# 如字符串为abb，则mask=1（01），第一位a为1，因为a只有1个
# word[i,j]，如果该字符子串为最美子字符串，maski与maskj最多只有一个位不同
# 因为从i到j，如果是最美，就最多1个奇数的字符，其他都为偶数字符
# 用hash表存放mask，判断有没有相同的mask或者相差一个字符的mask
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        word_freq = {}
        word_freq[0] = 1
        mask, res = 0, 0
        for c in word:
            mask ^= 1 << ord(c) - ord('a')
            if mask in word_freq:
                res += word_freq[mask]
            for i in range(10):
                mask1 = mask ^ (1 << i)
                if mask1 in word_freq:
                    res += word_freq[mask1]
            if mask in word_freq:
                word_freq[mask] += 1
            else:
                word_freq[mask] = 1
        return res


print(Solution().wonderfulSubstrings("aab"))
