def allcaps(func):
    # Define a new function that wraps the original function
    def wrapper():
        # Call the original function and split its return value into words
        result = func()
        words = result.split()

        # Create an empty string to store the capitalized result.
        capitalized_result = ""

        # Iterate through each word and make it uppercase, then add it to the result string.
        for word in words:
            capitalized_word = word.upper()
            capitalized_result += capitalized_word + " "
            
        # Remove the trailing space
        capitalized_result = capitalized_result.strip()
        
        print(capitalized_result)
    # Return the wrapper function
    return wrapper
'''
@allcaps
def greet():
    return "Hello World"

def main():
    greet()
    
main()
'''