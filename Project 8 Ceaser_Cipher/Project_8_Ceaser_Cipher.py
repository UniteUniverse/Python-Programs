print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
while direction =="encode" or direction=="decode":
    text = (input("Type your message:\n").lower())
    shift = int(input("Type the shift number:\n")) %26
    cipher_text=list(text)
    decrypt_text=list(text)
 
    def caesar_cipher():
        def encrypt(cipher_text, shift):
            n=0
            while n<len(cipher_text):
                if cipher_text[n] in alphabet:
                    cipher_text[n]=alphabet[(alphabet.index(cipher_text[n])+shift)]
                    n+=1
                else:
                    cipher_text[n]=cipher_text[n]
                    n+=1

        def decrypt(decrypt_text, shift):
            n=0
            while n<len(decrypt_text):
                if decrypt_text[n] in alphabet:
                    decrypt_text[n]=alphabet[(alphabet.index(decrypt_text[n])-shift)]
                    n+=1
                else:
                    decrypt_text[n]=decrypt_text[n]
                    n+=1
    
        if direction=="encode":
            encrypt(cipher_text,shift)
            print(f"Encrypted Code: {"".join(cipher_text)}")
        else:
            decrypt(decrypt_text,shift)
            print(f"Decrypted Code: {"".join(decrypt_text)}")
    
    caesar_cipher()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()