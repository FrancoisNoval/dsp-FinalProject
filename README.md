# Program Pengukuran Detak Jantung secara Realtime menggunakan Sinyal r-PPG dan Respirasi

## Deskripsi Proyek
Proyek ini adalah implementasi sistem monitoring detak jantung (Heart Rate) dan sinyal respirasi secara real-time menggunakan teknologi computer vision dan pemrosesan sinyal. Data diperoleh dari video webcam, diproses menggunakan teknik Remote Photoplethysmography (rPPG) dan analisis sinyal untuk menghasilkan statistik detak jantung (BPM) serta sinyal respirasi. Sistem ini divisualisasikan menggunakan grafik interaktif Python.

**Catatan**: 
Proyek ini merupakan tugas mata kuliah _IF 3024_ Prodi Teknik Informatika yang dibimbing oleh dosen Martin C.T. Manulang


Fitur utama:
- Deteksi wajah menggunakan MediaPipe Face Detection.
- Penghitungan rPPG (Heart Rate) dan sinyal respirasi secara real-time.
- Visualisasi sinyal dengan matplotlib.
- Logging statistik detak jantung ke file untuk analisis lebih lanjut

## Informasi Anggota
1. - **Nama:** Francois Novalentino Sinurat 
- **NIM:** 121140007  
2. - **Nama:** Dimas Azi Razab Aizar 
- **NIM:** 121140135 
## Instruksi Instalasi

### Prasyarat
1. Python 3.8 atau lebih baru.
2. Pastikan Anda memiliki kamera (webcam) yang terhubung dengan baik.

## Instalasi

1. Clone repository:
```bash
git https://github.com/FrancoisNoval/dsp-FinalProject.git
cd dsp-FinalProject
```

2. Buat virtual environment (opsional tapi disarankan):
```bash
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
# atau
venv\Scripts\activate  # Untuk Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Penggunaan

Jalankan program utama:
```bash
python main.py
```

### Kontrol
1. Pastikan webcam Anda aktif.
2. Jalankan program menggunakan perintah di atas.
3. Ikuti output di terminal untuk melihat nilai BPM dan pernapasan secara real-time.
4. Tekan tombol **q** untuk keluar dari program.
5. Data BPM akan tersimpan secara otomatis di file `bpm_log.txt` untuk analisis lebih lanjut.

## Referensi
Referensi untuk pembuatan kode ini menggunakan [Youtube](https://youtu.be/Q9MK-vtWzUM?si=0Sb0RGTczBeF2UaG), [ChatGPT](https://chatgpt.com/share/676a54d8-1280-800b-9507-2a24a56de649)
