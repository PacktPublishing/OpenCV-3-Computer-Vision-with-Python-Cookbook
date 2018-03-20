# OpenCV 3 Computer Vision with Python Cookbook
This is the code repository for [OpenCV 3 Computer Vision with Python Cookbook](https://www.packtpub.com/application-development/opencv-3-computer-vision-python-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781788474443), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
OpenCV 3 is a native cross-platform library for computer vision, machine learning, and image processing. OpenCV's convenient high-level APIs hide very powerful internals designed for computational efficiency and with a strong focus on real-time applications that can take advantage of multicore and GPU processing. This book will help you tackle increasingly challenging computer vision problems by providing number of recipes that you can use to improvise your existing applications.

In this book, you will learn how to process an image by manipulating pixels and analyze an image using histograms. We’ll guide you through segmenting images into homogeous regions and extracting meaningful objects. Then you’ll learn how to apply image filters to enhance image content and exploit the image geometry in order to relay different views of a pictured scene. Then we’ll explore techniques to achieve camera calibration and perform multiple-view analysis.
## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
import argparse
import cv2
parser = argparse.ArgumentParser()
parser.add_argument('--path', default='../data/Lena.png', help='Image path.')
params = parser.parse_args()
img = cv2.imread(params.path)
```

All the required information to get started with the respective recipes is mentioned in the recipes.

## Related Products
* [Computer Vision with OpenCV 3 and Qt5](https://www.packtpub.com/application-development/computer-vision-opencv-3-and-qt5?utm_source=github&utm_medium=repository&utm_campaign=9781788472395)

* [Building Advanced OpenCV3 Projects with Python [Video]](https://www.packtpub.com/application-development/building-advanced-opencv3-projects-python-video?utm_source=github&utm_medium=repository&utm_campaign=9781788394291)

* [Learning OpenCV 3 Computer Vision with Python - Second Edition](https://www.packtpub.com/application-development/learning-opencv-3-computer-vision-python-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781785283840)

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
