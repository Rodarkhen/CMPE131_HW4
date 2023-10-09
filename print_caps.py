def allcaps(func):
    # Define a new function that wraps the original function
    def wrapper():
        # Call the original function and split its return value into words
        result = func()
        # words = result.split()
        print(result.upper())
        # Iterate through each word and make it uppercase, then add it to the result string.
        # for i, word in enumerate(words):
            # print(word.upper(), end=' ' if i < len(words) - 1 else '')

    # Return the wrapper function
    return wrapper

@allcaps
def greet():
    return "Hello World!"

def main():
    greet()
    
main()
