class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(filter(str.isalnum,s))
        cleaned_text = cleaned_text.lower()
        cleaned_text_reversed = cleaned_text[::-1]

        if cleaned_text == cleaned_text_reversed:
            return True
        return False
    

def main():
    solution = Solution()

    word = "A man, a plan, a canal: Panama"

    result = solution.isPalindrome(word)
    print(f"isPalindrome({word!r}) = {result}")


if __name__ == "__main__":
    main()
