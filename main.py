import cv2
import numpy as np
import mediapipe as mp
from collections import deque
import time
import matplotlib.pyplot as plt
from signal_processing import bandpass_filter  # Import fungsi dari modul

# Logika utama program
fs = 30  # Assumed frame rate
buffer_size = fs * 10
green_values = deque(maxlen=buffer_size)
respiration_signal = deque(maxlen=buffer_size)
timestamps = deque(maxlen=buffer_size)

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)

# Initialize video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")
start_time = time.time()

# Set up plots
plt.ion()
fig, ax = plt.subplots(2, 1, figsize=(10, 6))
line1, = ax[0].plot([], [], label="Heart Rate (rPPG)", color="green")
line2, = ax[1].plot([], [], label="Respiration", color="blue")
ax[0].set_title("rPPG Signal (Heart Rate)")
ax[1].set_title("Respiration Signal")
ax[0].legend()
ax[1].legend()
plt.tight_layout()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Exiting.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_detection.process(rgb_frame)
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            margin = 20
            roi = rgb_frame[max(0, y-margin):min(y+h+margin, ih), max(0, x-margin):min(x+w+margin, iw)]

            mean_green = np.mean(roi[:, :, 1])
            green_values.append(mean_green)
            respiration_signal.append(np.mean(mean_green - np.mean(green_values)))
            timestamps.append(time.time() - start_time)

            if len(green_values) == buffer_size:
                filtered_rppg = bandpass_filter(list(green_values), 0.8, 2.5, fs)
                filtered_respiration = bandpass_filter(list(respiration_signal), 0.1, 0.5, fs)

                line1.set_xdata(timestamps)
                line1.set_ydata(filtered_rppg)
                line2.set_xdata(timestamps)
                line2.set_ydata(filtered_respiration)

                ax[0].relim()
                ax[0].autoscale_view()
                ax[1].relim()
                ax[1].autoscale_view()
                plt.pause(0.01)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
plt.ioff()
plt.show()
