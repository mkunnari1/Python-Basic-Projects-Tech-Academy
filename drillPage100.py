

def start():
    import os
    listDir = os.listdir("C:\\Users\\HP\\OneDrive\\Documents\\Python-Projects\\Python-Basic-Projects-Tech-Academy\\A\\")

    fPath = 'C:\\Users\\HP\\OneDrive\\Documents\\Python-Projects\\Python-Basic-Projects-Tech-Academy\\A\\'
    #print(listDir) #hashed out unless necessary to check if function is working
            
    for file in listDir:
        if".txt" in file:
            #be sure to convert the mtime into a str value or else it won't concatenate!!! 
            print(os.path.join(fPath, file)+' '+str(os.path.getmtime("C:\\A\\"+file)))
    

    
        
    

























if __name__ == '__main__':
    start()
