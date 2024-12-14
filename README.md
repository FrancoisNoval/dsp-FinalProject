# Respiratory and rPPG Signal Extraction Project

## Deskripsi Proyek
Proyek ini mengimplementasikan ekstraksi sinyal respirasi dan remote Photoplethysmography (rPPG) menggunakan analisis video real-time dari webcam.

## Prasyarat
- Python 3.8+
- Webcam

## Instalasi

1. Clone repository:
```bash
git clone https://github.com/anda/respiratory-rpg-project.git
cd respiratory-rpg-project
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
- Tekan 'q' untuk keluar dari aplikasi
- Pastikan pencahayaan cukup dan wajah terlihat jelas oleh kamera

## Konfigurasi

Anda dapat memodifikasi parameter dalam `src/signal_extractor.py`:
- `frame_rate`: Kecepatan frame kamera
- `buffer_duration`: Durasi buffer sinyal
- `rpg_bandpass`: Rentang frekuensi untuk sinyal rPPG
- `resp_bandpass`: Rentang frekuensi untuk sinyal respirasi

## Troubleshooting
- Pastikan webcam tidak digunakan oleh aplikasi lain
- Pastikan semua library terinstall dengan benar
- Pemosisian wajah di depan kamera mempengaruhi akurasi

## Lisensi
[Tentukan lisensi Anda]

## Kontributor
[Nama Anda/Kelompok]