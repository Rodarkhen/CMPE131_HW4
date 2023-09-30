def increment_int_a(someval):
    someval += 1
    print(f"Inside the function, a = {someval}")
        
def increment_int_b(someval):
    someval['32'] += 1

def main():
    a = 32
    increment_int_a(a)
    print(a)
    b = {'32':0}
    increment_int_b(b)
    print(b)
    
main()