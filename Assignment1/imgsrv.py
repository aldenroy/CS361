import time

while True:
    time.sleep(1)  # Sleep for 1 second
    
    with open("image-service.txt", "r") as file:
        content = file.read().strip()  #read and remove whitespace

    if content.isdigit():  #check if num
        number = int(content)
        
        num_images = 17  #num images in finder
        image_number = number % num_images
        
        #generate path
        image_path = f"/Users/aldenroy/Documents/GitHub/CS361/Assignment1/archive/image{image_number}.jpg"
        
        #write the image path back to "image-service.txt"
        with open("image-service.txt", "w") as file:
            file.write(image_path)

    file.close()
