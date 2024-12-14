import cv2 # Import modul cv2
import numpy as np # Import modul numpy
import mediapipe as mp # Import modul mediapipe
from collections import deque # Import modul deque
import time # Import modul time
import matplotlib.pyplot as plt # Import modul matplotlib.pyplot
from signal_processing import bandpass_filter  # Import fungsi bandpass_filter dari signal_processing.py

# Fungsi untuk menghitung BPM
def calculate_bpm(signal, fs):
    """
    Menghitung BPM (Beats Per Minute) Heart Rate dari sinyal rPPG.

    Parameters:
    - signal: list atau array 1D, sinyal rPPG yang telah difilter.
    - fs: int, sampling rate sinyal (Hz).

    Returns:
    - float, nilai BPM.
    """
    fft = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), d=1/fs)
    positive_freqs = freqs[freqs > 0]
    positive_fft = abs(fft[freqs > 0])
    peak_freq = positive_freqs[np.argmax(positive_fft)]
    bpm = peak_freq * 60  # Konversi Hz ke BPM
    return bpm

# Logika utama program
fs = 30  # Sampling rate (Hz)
buffer_size = fs * 10
green_values = deque(maxlen=buffer_size)
respiration_signal = deque(maxlen=buffer_size)
timestamps = deque(maxlen=buffer_size)
bpm_values = []  # Untuk menyimpan BPM dari tiap frame

# Inisialisasi detektor wajah dengan MediaPipe
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)

# Inisialisasi webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Gagal membuka webcam.")
    exit()

print("Ketik 'q' untuk keluar dari program.")
start_time = time.time()

# Setting Plot
plt.ion()
fig, ax = plt.subplots(2, 1, figsize=(10, 6))
line1, = ax[0].plot([], [], label="Heart Rate (BPM)", color="green")
line2, = ax[1].plot([], [], label="Respiration", color="blue")
ax[0].set_title("Sinyal rPPG(Heart Rate)")
ax[1].set_title("Sinyal respirasi")
ax[0].legend()
ax[1].legend()
plt.tight_layout()


while True:
    # Membaca frame dari webcam
    ret, frame = cap.read()
    if not ret:
        print("Gagal Membaca Frame")
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
                filtered_rppg = bandpass_filter(list(green_values), 1.25, 2.5, fs)
                filtered_respiration = bandpass_filter(list(respiration_signal), 0.1, 0.5, fs)

                # Hitung BPM
                bpm = calculate_bpm(filtered_rppg, fs)
                bpm_values.append(bpm)

                # Cetak BPM ke terminal
                print(f"Heart Rate Saat ini (BPM): {bpm:.2f}")

                # Log BPM ke file
                with open("bpm_log.txt", "a") as log_file:
                    log_file.write(f"{time.time() - start_time:.2f},{bpm:.2f}\n")

                # Update grafik
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

# Statistik akhir
if bpm_values:
    avg_bpm = np.mean(bpm_values)
    print(f"\nRata-Rata Heart Rate (BPM): {avg_bpm:.2f}")
    print(f"Tersimpan {len(bpm_values)} Data BPM ke bpm_log.txt")
