def allcaps(func):
    def wrapper():
        print(func().upper())
    return wrapper

"""@allcaps
def greet():
    return "hello World!"

def main():
    greet()
    
main()"""