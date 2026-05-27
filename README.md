#MINIPROJECT
# Invisible Cloak Project

## Overview
This project is a real-time computer vision application developed using Python and OpenCV. It creates an invisibility effect by detecting a specific cloak color and replacing it with the captured background frame.

---

## Features
- Real-time invisibility effect
- Background capture and replacement
- HSV color masking
- Live webcam processing
- Noise reduction using image processing

---

## Technologies Used
- Python
- OpenCV
- NumPy

---

## Installation

Install the required libraries:

```bash
pip install opencv-python numpy
```

---

## Working

Run the Python file:

- The system captures the background frame for a few seconds using the webcam.
- Each video frame is captured in real time.
- The red-colored cloak is detected using HSV color segmentation.
- A mask is created to identify the cloak region.
- Morphological operations are applied to remove noise from the mask.
- The detected cloak area is replaced with the stored background image.
- The final output frame creates an invisibility effect in real time.
- Press q to exit the application.

---

## Project Outcome
Successfully implemented a real-time invisibility cloak effect demonstrating concepts of computer vision, image segmentation, masking, and video processing.

---
## Team Members

- Nandini Singh
- EN23CS301658

## Future Improvements
- Support for multiple cloak colors
- Improved object detection accuracy
- AI-based background reconstruction
- Better performance optimization
- Mobile and web application integration

---

## Conclusion
The Invisible Cloak Project demonstrates the practical implementation of computer vision and image processing concepts using OpenCV. The project helped in understanding real-time video processing, color detection, masking techniques, and background replacement while creating an interactive and innovative application.

