# While true:
# //1 to generate new image or 2 to exit
# Request for input
# If input == 1:
# Open prng-service.txt
# Write “run” in prng-service.txt
# Sleep for 5 seconds
# Read pseudo random number from prng-service.txt
# Open image-service.txt
# Erase data in image-service.txt
# Write pseudo random number
# Sleep for 5 seconds
# Read and output image-service.txt
# Close image-service.txt
# Close prng-service.txt
# else if input ==2
# return
# else
# print (“unknown option”
import time
while True:
    print("Enter 1 for an image 2 to exit: ")
    user_input = input()
    if user_input == "1":
        with open("prng-service.txt", "w") as prng:
            prng.write("run")
        time.sleep(5)
        
        with open("prng-service.txt", "r") as prng:
            prng_content = prng.read()
            
        with open("image-service.txt", "w") as image:
            image.truncate(0)
            image.write(str(prng_content))
        time.sleep(5)
        
        with open("image-service.txt", "r") as file:
            content = file.read()
        
        print(content)
        file.close()
        prng.close()
        image.close()
        
    elif user_input == "2":
        break
    
    else:
        print("unknown option")
    
        
            
    