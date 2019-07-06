def getInfo():
    var1 = input("Please provide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    return(var1,var2)


def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        
        try:
            var3 = int(var1) + int(var2)
            print("{} + {} = {}".format(var1,var2,var3))
            go = False
        except ValueError:
            print("You did not provide a numeric value")
        except:
            print("Oops, you provided invalid input, program will now close")
      

if __name__ == "__main__":
    compute()
