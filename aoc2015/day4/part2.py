import hashlib


def main():
    inputStr="ckczppom"

    substr="000000"
    number = 0 

    while True:
        data = inputStr+str(number)
        hashVal = hashlib.md5(data.encode())
        hexVal = hashVal.hexdigest()
        print(f"{data} ---> hash value is {hexVal}")
        if hexVal.startswith(substr):
            print(f"Solution : {data} and postfix value  {number}")
            break
        number+=1

main()
    
