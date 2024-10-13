# CMRL Face Recognition Project

This project was developed during my internship at **Chennai Metro Rail Limited** under the guidance of **Mr. Sivakumar**.

## Objective
The objective of this project is to develop a **face recognition system** using a combination of **machine learning** and **image processing** techniques. The system leverages the **K-Nearest Neighbors (KNN)** algorithm for face classification, and various Python libraries for other functionalities.

## Key Technologies
- **KNN (K-Nearest Neighbors)**: Used for face classification (via `sklearn.neighbors`).
- **OpenCV (`cv2`)**: For image processing and camera functionalities.
- **NumPy**: For handling matrix operations and numerical computations.
- **OS**: To interact with the operating system (file handling, directory management).
- **CSV**: For reading and writing data in CSV format.
- **Datetime**: To handle timestamps.
- **Win32com.client**: For Component Object Model (COM) interaction.
- **Pickle**: For serialization of Python objects.
- **Subprocess**: For managing external processes.
- **Tkinter**: To build a graphical user interface (GUI) for the project.

## Libraries Used
```python
from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
import tkinter as tk
import subprocess
import win32com.client
