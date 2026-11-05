def reverseWords(input):
    words = input.split(" ")
    words = words[-1 : : -1]
    ans = " ".join(words)
    return ans

if __name__ == "__main__":
    input = "I love you"
    ans = reverseWords(input)
    print(ans)
