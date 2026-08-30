# ZYRR3 - OSINT Social Media Recon Tool

Tool reconnaissance OSINT untuk mencari akun media sosial seseorang berdasarkan nama.

## Fitur

- Pencarian akun **Facebook**, **Instagram**, **TikTok**, dan **Twitter/X**
- Filter URL otomatis (menghapus link video, postingan, dll)
- Menggunakan DuckDuckGo sebagai search engine

## Persyaratan

- Python 3.9+
- Koneksi internet

## Instalasi

```bash
git clone https://github.com/username/Osint-Sosmed-Zyrr3.git
cd Osint-Sosmed-Zyrr3
pip install -r requirements.txt
```

## Cara Penggunaan

```bash
python3 zyrr3.py
```

Masukkan nama target, lalu masukkan kunci akses.

## Kunci Akses

Kunci ada di dalam source code. Coba baca codenya dulu sebelum bertanya!.

## Struktur Project

```
Osint-Sosmed-Zyrr3/
├── zyrr3.py            # Script utama
├── requirements.txt    # Daftar dependency
└── README.md           # Dokumentasi
```

## Dependencies

| Package | Fungsi |
|---------|--------|
| `ddgs` | Search engine API (DuckDuckGo) |
| `pyfiglet` | ASCII art banner |
| `colorama` | Warna terminal |

## Contoh Output

```
 _______  ______  ____ _____
/__  /\ \/ / __ \/ __ \__  /
  / /  \  / /_/ / /_/ //_ <
 / /__ / / _, _/ _, _/__/ /
/____//_/_/ |_/_/ |_/____/

==================================================
       OSINT Social Media Recon Tool
==================================================

  [?] Masukkan nama target : rezzy

  [Facebook]
  [OK] Mencari Facebook...
  [*] Ditemukan 9 akun:
     1. https://www.facebook.com/rezzyracing
     2. https://www.facebook.com/rezzyusa
     ...

  [Instagram]
  [OK] Mencari Instagram...
  [*] Ditemukan 10 akun:
     1. https://www.instagram.com/rezzyghadjar
     2. https://www.instagram.com/rezzy.app
     ...

==================================================
  [+] Total : 27 akun ditemukan
==================================================
```

## Disclaimer

Tool ini dibuat untuk keperluan **educational purposes** dan **authorized testing** saja. Penyalahgunaan tool ini untuk hal yang melanggar hukum adalah tanggung jawab pengguna.

## License

MIT License
