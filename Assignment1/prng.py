# While true:
# Sleep for 1 second.
# Open file prng-service.txt
# Read file
# If line in file is “run”:
# Generate random number
# Erase “run” from prng-service.txt
# Write random number in to prng-service.txt
# Close file
import time
import random

while True:
    time.sleep(1)
    with open("prng-service.txt", "r") as file:
        line = file.readline().strip()
    
    if line == "run":
        random_number = random.randint(1, 100)
        
        with open("prng-service.txt", "w") as file:
            file.truncate(0) #erase run
            file.write(str(random_number))
            
    file.close()