"""
Create a piechart using matplotlib A by 15% and B is 85%.
"""

def chart(a, b):
    """
    Create a piechart using matplotlib A by 15% and B is 85%.
    """
    import matplotlib.pyplot as plt
    labels = 'A', 'B'
    sizes = [a, b]
    colors = ['gold', 'yellowgreen']
    explode = (0.1, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.show()

chart(15, 85) 


"""
Create (x,y) coordinates using images from folders
"""

def coordinates (folder):
    """
    Create (x,y) coordinates using images from folders
    """
    import os
    import numpy as np
    import cv2
    import matplotlib.pyplot as plt

    # Get the images from the folder
    image_paths = [os.path.join(folder, f) for f in os.listdir(folder)]
    images = []
    for image_path in image_paths:
        images.append(cv2.imread(image_path))

    # Create the coordinates
    x = []
    y = []
    for image in images:
        x.append(image.shape[1]/2)
        y.append(image.shape[0]/2)

    # Plot the coordinates
    plt.scatter(x, y, s=10)
    plt.show()


"""
Classify images from separated by folders and create coordinates for each image
"""

def Classify(images):
    """
    Classify images from separated by folders and create coordinates for each image
    """
    import os
    import numpy as np
    import cv2
    import matplotlib.pyplot as plt

    # Get the images from the folder
    image_paths = [os.path.join(images, f) for f in os.listdir(images)]
    images = []
    for image_path in image_paths:
        images.append(cv2.imread(image_path))

    # Create the coordinates
    x = []
    y = []
    for image in images:
        x.append(image.shape[1]/2)
        y.append(image.shape[0]/2)

    # Plot the coordinates
    plt.scatter(x, y, s=10)
    plt.show()


def randomNumberGenerator(number):
    """
    Create random numbers
    """
    import random
    random_number = random.randint(0, number)
    return random_number

randomNumberGenerator(number=10)