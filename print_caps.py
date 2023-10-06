def allcaps(func):
    def wrapper():
        definedFunc = func()
        print(definedFunc.upper())
    return wrapper
'''
@allcaps
def greet():
    return "hello World!"

def main():
    greet()
    
main()
'''