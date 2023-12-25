def is_palindrome(word):
    cleaned_word = word.replace(" ", "").lower()
    reversed_word = cleaned_word[::-1]

    return cleaned_word == reversed_word


while True:
    user_input = input("Enter a word or phrase to check if it's a palindrome (type 'exit' to end): ")

    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome!")
    else:
        print(f"{user_input} is not a palindrome.")
