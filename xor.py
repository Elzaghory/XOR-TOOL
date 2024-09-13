import colorama
from colorama import Fore, init, Back, Style

colorama.init(autoreset=True)

def e1(encoded_hex_e1, key_user_e1): 
    x1 = bytearray.fromhex(encoded_hex_e1) 
    key_bytes = key_user_e1.encode('ascii') 
    x3 = len(key_bytes)

    for i in range(len(x1)): 
     x1[i] ^= key_bytes[i % x3] 

    return x1 

def e2(encoded_hex_e2, encoded_string_e2): 
    x1_e2 = bytearray.fromhex(encoded_hex_e2) 
    key_bytes_e2 = encoded_string_e2.encode('ascii') 
    x3_e2 = len(key_bytes_e2)

    for i in range(len(x1_e2)): 
     x1_e2[i] ^= key_bytes_e2[i % x3_e2] 

    return x1_e2
   
def e3(input_user_e3, key_user_e3): 
    x1_e3 = bytearray.fromhex(input_user_e3) 
    key_bytes_e3 = bytearray.fromhex(key_user_e3)
    x3_e3 = len(key_bytes_e3)

    for i in range(len(x1_e3)): 
     x1_e3[i] ^= key_bytes_e3[i % x3_e3] 

    return x1_e3 

def e4(input_user_e4, key_user_e4): 
    x1_e4 = bytearray.fromhex(input_user_e4) 
    key_bytes_e4 = key_user_e4.encode('ascii') 
    x3_e4 = len(key_bytes_e4)

    for i in range(len(x1_e4)): 
     x1_e4[i] ^= key_bytes_e4[i % x3_e4] 

    return x1_e4 

def e5(encoded_hex_e5, key_user_e5): 
    x1_e5 = bytearray.fromhex(encoded_hex_e5) # Convert the hex string to the bytes  # result =  ]P]Y\x1a U.G)=2\\>1Y)\x1c  *bytes
    key_bytes_e5 = key_user_e5.encode('ascii') # Convert the key to the bytes 
    x3_e5 = len(key_bytes_e5)

    for i in range(len(x1_e5)): 
     x1_e5[i] ^= key_bytes_e5[i % x3_e5] 

    return x1_e5.decode('ascii') # Convert the result back to the string

def e6(encoded_hex_e6, encoded_string_e6): 
    x1_e6 = bytearray.fromhex(encoded_hex_e6) 
    key_bytes_e6 = encoded_string_e6.encode('ascii')
    x3_e6 = len(key_bytes_e6)

    for i in range(len(x1_e6)): 
     x1_e6[i] ^= key_bytes_e6[i % x3_e6] 

    return x1_e6.decode('ascii') 

def e7(input_user_e7, key_user_e7): 
    x1_e7 = bytearray.fromhex(input_user_e7) 
    key_bytes_e7 = bytearray.fromhex(key_user_e7)
    x3_e7 = len(key_bytes_e7)

    for i in range(len(x1_e7)): 
     x1_e7[i] ^= key_bytes_e7[i % x3_e7]

    return x1_e7.decode('ascii')

def e8(input_user_e8, key_user_e8): 
    x1_e8 = bytearray.fromhex(input_user_e8) 
    key_bytes_e8 = key_user_e8.encode('ascii') 
    x3_e8 = len(key_bytes_e8)

    for i in range(len(x1_e8)): 
     x1_e8[i] ^= key_bytes_e8[i % x3_e8] 

    return x1_e8.decode('ascii')

def d1(input_user_d1, key_user_d1): 
    x1_d1 = bytearray.fromhex(input_user_d1) 
    key_bytes_d1 = key_user_d1.encode('ascii') 
    x3_d1 = len(key_bytes_d1)

    for i in range(len(x1_d1)): 
     x1_d1[i] ^= key_bytes_d1[i % x3_d1] 

    return x1_d1.decode('ascii') 

def d2(input_user_d2, key_user_d2): 
    x1_d2 = bytearray.fromhex(input_user_d2) 
    key_bytes_d2 = bytearray.fromhex(key_user_d2)
    x3_d2 = len(key_bytes_d2)

    for i in range(len(x1_d2)): 
     x1_d2[i] ^= key_bytes_d2[i % x3_d2] 

    return x1_d2.decode('ascii') 

def d3(encoded_hex_d3, key_user_d3): 
    x1_d3 = bytearray.fromhex(encoded_hex_d3) 
    key_bytes_d3 = key_user_d3.encode('ascii')
    x3_d3 = len(key_bytes_d3)

    for i in range(len(x1_d3)): 
     x1_d3[i] ^= key_bytes_d3[i % x3_d3] 

    return x1_d3.decode('ascii')  

def d4(encoded_hex_d4, encoded_string_d4): 
    x1_d4 = bytearray.fromhex(encoded_hex_d4)
    key_bytes_d4 = encoded_string_d4.encode('ascii') 
    x3_d4 = len(key_bytes_d4)

    for i in range(len(x1_d4)): 
     x1_d4[i] ^= key_bytes_d4[i % x3_d4] 

    return x1_d4.decode('ascii')  

def d5(input_user_d5, key_user_d5): 
    x1_d5 = bytearray.fromhex(input_user_d5) 
    key_bytes_d5 = key_user_d5.encode('ascii') 
    x3_d5 = len(key_bytes_d5)

    for i in range(len(x1_d5)): 
     x1_d5[i] ^= key_bytes_d5[i % x3_d5] 

    return x1_d5  

def d6(input_user_d6, key_user_d6): 
    x1_d6 = bytearray.fromhex(input_user_d6) 
    key_bytes_d6 = bytearray.fromhex(key_user_d6)
    x3_d6 = len(key_bytes_d6)

    for i in range(len(x1_d6)): 
     x1_d6[i] ^= key_bytes_d6[i % x3_d6] 

    return x1_d6 

def d7(encoded_hex_d7, key_user_d7): 
    x1_d7 = bytearray.fromhex(encoded_hex_d7) 
    key_bytes_d7 = key_user_d7.encode('ascii') 
    x3_d7 = len(key_bytes_d7)

    for i in range(len(x1_d7)): 
     x1_d7[i] ^= key_bytes_d7[i % x3_d7] 

    return x1_d7 

def d8(encoded_hex_d8, encoded_string_d8): 
    x1_d8 = bytearray.fromhex(encoded_hex_d8) 
    key_bytes_d8 = encoded_string_d8.encode('ascii') 
    x3_d8 = len(key_bytes_d8)

    for i in range(len(x1_d8)): 
     x1_d8[i] ^= key_bytes_d8[i % x3_d8] 

    return x1_d8                 

def main(): 

    #print("\t(=== Tool for xor encryption/decryption ===)")
    #print("\t\tAuthor: Elzaghory\n")



    print(Fore.GREEN + """
  
            ██╗  ██╗ ██████╗ ██████╗      ██████╗ ██████╗ ███████╗██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
            ╚██╗██╔╝██╔═══██╗██╔══██╗    ██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
             ╚███╔╝ ██║   ██║██████╔╝    ██║   ██║██████╔╝█████╗  ██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║
             ██╔██╗ ██║   ██║██╔══██╗    ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
            ██╔╝ ██╗╚██████╔╝██║  ██║    ╚██████╔╝██║     ███████╗██║  ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
            ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
   """)

    print( Fore.GREEN +  "\t ╔════════════════════════════════════════════════════════════════════════════════════════════════════╗ ")
    print( Fore.GREEN +  "\t ║                   "+ Fore.WHITE + "\t\t\tAUTHOR | ELZAGHORY"+ Fore.GREEN + "\t\t\t\t              ║ ")
    print( Fore.GREEN +  "\t ╠════════════════════════════════════════════════════════════════════════════════════════════════════╣ ")
    print( Fore.GREEN +  "\t ║      "+ Fore.WHITE + "\t\t\tTHE TOOL IS FOR XOR ENCRYPTION & DECRYPTION"+ Fore.GREEN +"\t\t\t      ║ ")
    print( Fore.GREEN +  "\t ╚════════════════════════════════════════════════════════════════════════════════════════════════════╝ ")    
   

    print("\n")
    print(Fore.YELLOW +"Which Operation XOR that you want?")
    soklan_xor = print(Fore.WHITE +"Write"+Fore.YELLOW+"'encrypt'"+Fore.WHITE+"for XOR Encryption or "+Fore.YELLOW+"'decrypt'"+Fore.WHITE+" for XOR Decryption")
    pilihan_xor = input("What Is Your Choice? : ")

    if pilihan_xor == "encrypt":
        print("\n")
    elif pilihan_xor == "decrypt":
        print("\n")
    else:
        print("\n")
        print(Fore.WHITE +"\t\t\t\t[===== "+Fore.RED+"Wrong Choice!.....Try Again!"+Fore.WHITE+" =====]")
        print("\n")
        main()

    print(Fore.YELLOW +"What value of input that you want?")
    soklan_input = print(Fore.WHITE +"Write"+Fore.YELLOW+"'text'"+Fore.WHITE+"for input=text or"+Fore.YELLOW+"'hex'"+Fore.WHITE+" for input=hex")
    jenis_input = input("What Is Your Choice? : ")

    if jenis_input == "text":
        print("\n")
    elif jenis_input == "hex":
        print("\n")
    else:
        print("\n")
        print(Fore.WHITE +"\t\t\t\t[===== "+Fore.RED+"Wrong Choice!.....Try Again!"+Fore.WHITE+" =====]")
        print("\n")
        main()


    print(Fore.YELLOW +"What value of key that you want?")
    soklan_key = print(Fore.WHITE +"Write"+Fore.YELLOW+"'text'"+Fore.WHITE+"for key=text or"+Fore.YELLOW+"'hex'"+Fore.WHITE+" for key=hex")
    jenis_key = input("What Is Your Choice? : ")

    if jenis_key == "text":
        print("\n")
    elif jenis_key == "hex":
        print("\n")
    else:
        print("\n")
        print(Fore.WHITE +"\t\t\t\t[===== "+Fore.RED+"Wrong Choice!.....Try Again!"+Fore.WHITE+" =====]")
        print("\n")
        main()

    print(Fore.YELLOW +"What value of output that you want?")
    soklan_output = print(Fore.WHITE +"Write"+Fore.YELLOW+"'text'"+Fore.WHITE+"for output=text or"+Fore.YELLOW+"'hex'"+Fore.WHITE+" for output=hex")
    hasil_output = input("What Is Your Choice? : ")


    if hasil_output == "text":
        print("\n")
    elif hasil_output == "hex":
        print("\n")
    else:
        print("\n")
        print(Fore.WHITE +"\t\t\t\t[===== "+Fore.RED+"Wrong Choice!.....Try Again!"+Fore.WHITE+" =====]")
        print("\n")
        main()


    operation_e1 = [pilihan_xor == "encrypt", jenis_input == "text", jenis_key == "text", hasil_output == "hex"]
    operation_e2 = [pilihan_xor == "encrypt", jenis_input == "text", jenis_key == "hex", hasil_output == "hex"]
    operation_e3 = [pilihan_xor == "encrypt", jenis_input == "hex", jenis_key == "hex", hasil_output == "hex"]
    operation_e4 = [pilihan_xor == "encrypt", jenis_input == "hex", jenis_key == "text", hasil_output == "hex"]
    operation_e5 = [pilihan_xor == "encrypt", jenis_input == "text", jenis_key == "text", hasil_output == "text"]
    operation_e6 = [pilihan_xor == "encrypt", jenis_input == "text", jenis_key == "hex", hasil_output == "text"]
    operation_e7 = [pilihan_xor == "encrypt", jenis_input == "hex", jenis_key == "hex", hasil_output == "text"]
    operation_e8 = [pilihan_xor == "encrypt", jenis_input == "hex", jenis_key == "text", hasil_output == "text"]

    operation_d1 = [pilihan_xor == "decrypt", jenis_input == "hex", jenis_key == "text", hasil_output == "text"]
    operation_d2 = [pilihan_xor == "decrypt", jenis_input == "hex", jenis_key == "hex", hasil_output == "text"]
    operation_d3 = [pilihan_xor == "decrypt", jenis_input == "text", jenis_key == "text", hasil_output == "text"]
    operation_d4 = [pilihan_xor == "decrypt", jenis_input == "text", jenis_key == "hex", hasil_output == "text"]
    operation_d5 = [pilihan_xor == "decrypt", jenis_input == "hex", jenis_key == "text", hasil_output == "hex"]
    operation_d6 = [pilihan_xor == "decrypt", jenis_input == "hex", jenis_key == "hex", hasil_output == "hex"]
    operation_d7 = [pilihan_xor == "decrypt", jenis_input == "text", jenis_key == "text", hasil_output == "hex"]
    operation_d8 = [pilihan_xor == "decrypt", jenis_input == "text", jenis_key == "hex", hasil_output == "hex"]

    if all(operation_e1) :
        input_user_e1 = input("Write your input(text) : ")
        key_user_e1 = input("Write your key(text) : ")
        print("\n")

        encoded_hex_e1 = input_user_e1.encode("utf-8").hex()

        result = e1(encoded_hex_e1, key_user_e1)
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" hex"+Fore.WHITE+" is:", result.hex())
        exit()
    else:
        pass


    if all(operation_e2) :
        input_user_e2 = input("Write your input(text) : ")
        key_user_e2 = input("Write your key(hex) : ")
        print("\n")


        encoded_hex_e2 = input_user_e2.encode("utf-8").hex()

        encoded_string_e2 = bytes.fromhex(key_user_e2).decode('utf-8')

        result_e2 = e2(encoded_hex_e2, encoded_string_e2) 
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" hex"+Fore.WHITE+" is:", result_e2.hex())
        exit()
    else:
        pass

    if all(operation_e3) :
        input_user_e3 = input("Write your input(hex) : ")
        key_user_e3 = input("Write your key(hex) : ")
        print("\n")

        result_e3 = e3(input_user_e3, key_user_e3) 
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" hex"+Fore.WHITE+" is:", result_e3.hex())
        exit()
    else:
        pass

    if all(operation_e4) :
        input_user_e4 = input("Write your input(hex) : ")
        key_user_e4 = input("Write your key(text) : ")
        print("\n")

        result_e4 = e4(input_user_e4, key_user_e4)
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" hex"+Fore.WHITE+" is:", result_e4.hex())
        exit()
    else:
        pass

    if all(operation_e5) :
        input_user_e5 = input("Write your input(text) : ")
        key_user_e5 = input("Write your key(text) : ")
        print("\n")

        encoded_hex_e5 = input_user_e5.encode("utf-8").hex()

        result_e5 = e5(encoded_hex_e5, key_user_e5)
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" text"+Fore.WHITE+" is:", result_e5)
        exit()
    else:
        pass

    if all(operation_e6) :
        input_user_e6 = input("Write your input(text) : ")
        key_user_e6 = input("Write your key(hex) : ")
        print("\n")

        encoded_hex_e6 = input_user_e6.encode("utf-8").hex()

        encoded_string_e6 = bytes.fromhex(key_user_e6).decode('utf-8')

        result_e6 = e6(encoded_hex_e6, encoded_string_e6) 
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" text"+Fore.WHITE+" is:", result_e6)
        exit()
    else:
        pass

    if all(operation_e7) :
        input_user_e7 = input("Write your input(hex) : ")
        key_user_e7 = input("Write your key(hex) : ")
        print("\n")

        result_e7 = e7(input_user_e7, key_user_e7) 
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" text"+Fore.WHITE+" is:", result_e7)
        exit()
    else:
        pass

    if all(operation_e8) :
        input_user_e8 = input("Write your input(hex) : ")
        key_user_e8 = input("Write your key(text) : ")
        print("\n")

        result_e8 = e8(input_user_e8, key_user_e8)
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" text"+Fore.WHITE+" is:", result_e8)
        exit()
    else:
        pass

    if all(operation_d1) :
        input_user_d1 = input("Write your input(hex) : ")
        key_user_d1 = input("Write your key(text) : ")
        print("\n")

        result_d1 = d1(input_user_d1, key_user_d1)
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" text"+Fore.WHITE+" is:", result_d1)
        exit()
    else:
        pass

    if all(operation_d2) :
        input_user_d2 = input("Write your input(hex) : ")
        key_user_d2 = input("Write your key(hex) : ")
        print("\n")

        result_d2 = d2(input_user_d2, key_user_d2) 
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" text"+Fore.WHITE+" is:", result_d2)
        exit()
    else:
        pass

    if all(operation_d3) :
        input_user_d3 = input("Write your input(text) : ")
        key_user_d3 = input("Write your key(text) : ")
        print("\n")

        encoded_hex_d3 = input_user_d3.encode("utf-8").hex()

        result_d3 = d3(encoded_hex_d3, key_user_d3)
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" text"+Fore.WHITE+" is:", result_d3)
        exit()
    else:
        pass

    if all(operation_d4) :
        input_user_d4 = input("Write your input(text) : ")
        key_user_d4 = input("Write your key(hex) : ")
        print("\n")

        encoded_hex_d4 = input_user_d4.encode("utf-8").hex()

        encoded_string_d4 = bytes.fromhex(key_user_d4).decode('utf-8')

        result_d4 = d4(encoded_hex_d4, encoded_string_d4) 
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" text"+Fore.WHITE+" is:", result_d4)
        exit()
    else:
        pass

    if all(operation_d5) :
        input_user_d5 = input("Write your input(hex) : ")
        key_user_d5 = input("Write your key(text) : ")
        print("\n")

        result_d5 = d5(input_user_d5, key_user_d5)
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" hex"+Fore.WHITE+" is:", result_d5.hex())
        exit()
    else:
        pass

    if all(operation_d6) :
        input_user_d6 = input("Write your input(hex) : ")
        key_user_d6 = input("Write your key(hex) : ")
        print("\n")

        result_d6 = d6(input_user_d6, key_user_d6) 
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" hex"+Fore.WHITE+" is:", result_d6.hex())
        exit()
    else:
        pass 

    if all(operation_d7) :
        input_user_d7 = input("Write your input(text) : ")
        key_user_d7 = input("Write your key(text) : ")
        print("\n")

        encoded_hex_d7 = input_user_d7.encode("utf-8").hex()

        result = d7(encoded_hex_d7, key_user_d7)
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" hex"+Fore.WHITE+" is:", result.hex())
        exit()
    else:
        pass

    if all(operation_d8) :
        input_user_d8 = input("Write your input(text) : ")
        key_user_d8 = input("Write your key(hex) : ")
        print("\n")

        
        encoded_hex_d8 = input_user_d8.encode("utf-8").hex()

        
        encoded_string_d8 = bytes.fromhex(key_user_d8).decode('utf-8')
        #encoded_string = ''.join([chr(int(key[i:i+2], 16)) for i in range(0, len(key), 2)])

        result_d8 = d8(encoded_hex_d8, encoded_string_d8) 
        print(Fore.WHITE +"The Output in"+Fore.YELLOW+" hex"+Fore.WHITE+" is:", result_d8.hex())
        exit()
    else:
        pass  

if __name__ == '__main__':
	main()
