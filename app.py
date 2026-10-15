print("aws ai project environment ready!")
import time

def launch_ai_image_analyzer(image_name):
    print("\n===============================================")
    print("launching: aws ai local analysis environment")
    print("=============================================\n")
    time.sleep(1)

    print(f"loading target image: '{image_name}'...")
    time.sleep(1.5)

    print("connecting to local amazon rekognition sandbox pipeline...")
    time.sleep(2)

    print("running deep learning object detection algorithms...")
    time.sleep(2)

    #simulating what the aws ai sees when it analyzes a standard image
    print("\n===== success: ai analysis result =====")
    print(" laptop / computer monitor : 98.42% match")
    print(" engineering student desk : 94.15% match")
    print(" electronic keyboard : 89.61% match")
    print(" python source code app : 85.10% match")
    print("===================================\n")
    print(" project simulation executed with zero errors!")

# start the analyzer app
launch_ai_image_analyzer("test_image.jpg")