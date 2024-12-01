import os
from PIL import Image
from IPython.display import display


def search_and_display_anime_images(dataset_path="anime_images/data/anime_images"):
    
    if not os.path.exists(dataset_path):
        print(f"The dataset path '{dataset_path}' does not exist. Please verify the path.")
        return


    for _ in iter(int, 1):  
        user_input = input("Do you want to talk? (Type 'stop' to exit, 'Y' for yes, 'N' for no): ")

        if user_input.lower() == "stop":
            print("Thank you for having me!")
            break
        elif user_input.lower() == "y":
            print("Enter the name of the anime you want to search:")
            anime_name = input("Anime name: ").strip().lower()  
            anime_folder = os.path.join(dataset_path, anime_name)  
            
            
            print(f"Looking for anime images in folder: {anime_folder}")

            
            if not os.path.exists(anime_folder) or not os.path.isdir(anime_folder):
                print(f"No folder found for '{anime_name}' under the dataset path. Please try again.")
                continue  
            
            
            valid_extensions = {".jpg", ".jpeg", ".png", ".gif"}  
            image_files = [f for f in os.listdir(anime_folder) if os.path.splitext(f)[1].lower() in valid_extensions]

            image_count = len(image_files)
            print(f"Found {image_count} images for '{anime_name}'.")

            if image_count == 0:
                print("No images to display.")
                continue  

            
            while True:
                try:
                    num_to_display = int(input(f"How many images would you like to see? (Max: {image_count}): "))
                    if 1 <= num_to_display <= image_count:
                        break
                    else:
                        print(f"Please enter a number between 1 and {image_count}.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            
            for i, image_file in enumerate(image_files[:num_to_display]):
                print(f"Displaying image {i+1}/{num_to_display}: {image_file}")
                img_path = os.path.join(anime_folder, image_file)
                img = Image.open(img_path)
                display(img)
        
        elif user_input.lower() == "n":
            print("Okay, let me know if you need anything.")
        else:
            print("I didn't understand that. Please type 'Y', 'N', or 'stop'.")
