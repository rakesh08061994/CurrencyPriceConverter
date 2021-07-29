import time

def currencyConverter():
    try:
        with open("currencyData.txt") as open_file:
            readline_file = open_file.readline()
            storeDict = {}
            for line in open_file:
                splitFormation = line.split("\t")
                storeDictKeys = splitFormation[0]
                storeDict[storeDictKeys] = splitFormation[1]
            userInput = int(input("Enter Amount of INR :  "))
            print("--- Please choose from currency options ---")
            keylist = list(storeDict)
            for i in keylist:
                print(i)
            name = input("In which currency you want to convert INR :")
            countryName = name.title()
            print(countryName)
            if countryName in storeDict:
                print("Please Wait... System has been uploaded your request.")
                time.sleep(2)
                print(
                    f"{userInput} INR = {userInput * float(storeDict[countryName])} {name} ")
            else:
                print(
                    "This Currency is not present in the given list. Please chhose correct one.")
    except FileNotFoundError:
        print("File is not attached or Wrong file name")
    except ValueError:
        print("Input is not correct please input carefully")


# -------------------------------------------*-----------------------------------------------------
if __name__ == "__main__":
    currencyConverter()
    
    
    
    
    
    
    
