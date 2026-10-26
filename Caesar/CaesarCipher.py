''' caesar cipher is a type of cipher
that works by determining a fixed number of
an offset , offseting the alphabet by that number,
and making translations based on it '''
import string as s
inj = int(input("enter offset: "))
def caesar(argument):
    boi = s.ascii_uppercase
    BOI = s.ascii_lowercase
    boi2 = boi[inj:] + boi[:inj]
    BOI2 = BOI[inj:] + BOI[:inj]
    tb = str.maketrans(boi + BOI , boi2 + BOI2)
    return argument.translate(tb)
if __name__ == '__main__':
    z = input("enter text: ")
    skr = caesar(z)
    print("ciphered text:" , skr)