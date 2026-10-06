# atbash cipher is a cipher that
# reverses orders of letters in a 
# particular word, it reverses letters based
# on a reversed version of the alphabet (z , y , x...)
# an example is : Hello becomes Svool
import string as s
def atbash(txt):
    lcase = s.ascii_lowercase
    ucase = s.ascii_uppercase
    t1 = lcase[::-1]
    t2 = ucase[::-1]
    table = str.maketrans(lcase + ucase , t1 + t2)
    return txt.translate(table)
if __name__ == '__main__':
    msg = input("Enter a string of text: ")
    s = atbash(msg)
    print(f"Ciphered text: {s}")