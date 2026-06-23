import cv2
import threading
import platform

if platform.system() == "Windows":
    import winsound

    def play_alarm():
        winsound.PlaySound("alarm.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
else:
    def play_alarm():
        print("ALARM! Please add a sound file or install playsound.")

face_cascade = cv2.CascadeClassifier(
    "assets/haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    "assets/haarcascade_eye.xml"
)

cap = cv2.VideoCapture(0)
closed_frames = 0  

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    eyes_detected = False  

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                roi_color,
                (ex, ey),
                (ex+ew, ey+eh),
                (0, 255, 0),
                2
            )
            eyes_detected = True  

   
    if eyes_detected:
        closed_frames = 0
    else:
        closed_frames += 1

    if closed_frames >= 20:
        threading.Thread(target=play_alarm, daemon=True).start()
        closed_frames = 0

    cv2.imshow("Eye Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()