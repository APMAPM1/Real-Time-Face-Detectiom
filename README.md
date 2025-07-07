# Real-Time Face Detection and Face Count using OpenCV

This is a beginner-friendly Computer Vision project that detects **human faces and counts them in real-time** using a webcam. It uses OpenCV's pre-trained Haar Cascade Classifier to detect faces and draw bounding boxes around them, along with displaying the number of faces detected.

## 🚀 Project Overview
- Real-time face detection using webcam.
- Displays **the number of faces detected** on the screen.
- Uses OpenCV's Haar Cascade pre-trained model.
- Lightweight, fast, and easy to run.

## 📂 Folder Structure

```plaintext
face_detection_project/
│
├── haarcascades/
│    └── haarcascade_frontalface_default.xml
│
├── main.py
│
└── README.md

```

## ⚙️ Requirements

- Python 3.x
- OpenCV

### Install Required Libraries:

```bash
pip install opencv-python
```

### How to Run

```bash
python main.py
```

Your webcam will open automatically.
Blue rectangles will appear around all detected faces.
The number of faces detected will be displayed in real-time.

Press 'q' to exit the program.

## 🔗 Resources

- [OpenCV Haar Cascade Tutorial](https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html)
- [OpenCV Python Documentation](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [Haarcascade Files on GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades)
