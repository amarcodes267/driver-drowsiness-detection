# Driver Drowsiness Detection

A lightweight Python application for real-time face and eye detection using OpenCV. This project demonstrates a basic driver drowsiness detection prototype by detecting facial regions and eye positions from a live webcam feed.

## Features

- Real-time face detection using Haar cascades.
- Eye detection inside detected face regions.
- Live webcam preview with annotated bounding boxes.
- Easily extendable for drowsiness alerts and audio notifications.

## Technologies

- Python 3
- OpenCV (`opencv-python`)
- Windows `winsound` module for audio alerts

## Project Structure

- `main.py` - Main application script for webcam face and eye detection.
- `assets/haarcascade_frontalface_default.xml` - Haar cascade for face detection.
- `assets/haarcascade_eye.xml` - Haar cascade for eye detection.
- `alarm.wav` - Optional alarm sound file for alert extension.
- `requirements.txt` - Python dependencies.
- `screenshots/` - Sample screenshots or visual output examples.

## Prerequisites

- Python 3.8 or later
- Webcam or camera device

## Installation

1. Clone the repository:

```bash
git clone https://github.com/amarcodes267/driver-drowsiness-detection.git
cd driver-drowsiness-detection
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

- Windows PowerShell:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- Command Prompt:
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

4. Install required packages:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The webcam window will open and show detected faces and eyes. Press `q` to exit the application.

## Notes

- Drowsiness is detected when eyes are closed for 20+ consecutive frames, triggering an alarm sound automatically.
- The alarm uses the Windows `winsound` module and plays `alarm.wav`.
- For higher accuracy, the detection model can be extended with blink rate analysis or head pose estimation.

## License

This project is available under the MIT License.
