# Kalkulator Sederhana dengan PyQt5

Kode ini adalah implementasi kalkulator sederhana yang menggunakan library PyQt5 untuk membangun antarmuka pengguna. Kalkulator ini dapat melakukan operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, dan pembagian. Berikut adalah penjelasan singkat tentang bagaimana kode ini berfungsi:

1. `on_click(text)`: Ini adalah fungsi yang akan dipanggil ketika tombol pada kalkulator ditekan. Fungsi ini akan melakukan tindakan berdasarkan teks tombol yang ditekan. Jika tombol "=" ditekan, ia akan mencoba menghitung hasil ekspresi matematika yang ada di layar dan menampilkannya. Jika tombol "C" ditekan, ia akan menghapus layar. Untuk tombol lainnya, ia akan menambahkan teks tombol tersebut ke layar.

2. `app = QApplication(sys.argv)`: Ini adalah inisialisasi aplikasi PyQt5.

3. `window = QWidget()`: Ini adalah inisialisasi jendela utama aplikasi.

4. `layout = QVBoxLayout()`: Ini adalah tata letak vertikal untuk menempatkan elemen-elemen antarmuka pengguna.

5. `display = QLineEdit()`: Ini adalah kotak teks yang digunakan untuk menampilkan ekspresi matematika dan hasilnya. Kotak teks ini tidak dapat diedit secara manual oleh pengguna.

6. `button_grid`: Ini adalah daftar yang berisi teks tombol yang akan ditampilkan pada kalkulator.

7. Selanjutnya, kode mengatur tombol-tombol pada tata letak dengan mengikuti tata letak matriks seperti yang didefinisikan dalam `button_grid`. Tombol-tombol ini akan terhubung ke fungsi `on_click()` untuk menangani tindakan pengguna.

## Menjalankan Kode

Anda dapat menjalankan kode ini dengan menggunakan interpreter Python yang sudah memiliki library PyQt5 terinstal. Pastikan Anda sudah menginstal PyQt5 sebelum menjalankan kode ini. Jika belum, Anda dapat menginstalnya dengan perintah berikut:

```bash
pip install PyQt5
```

1. Salin kode di atas dan simpan dalam sebuah file dengan ekstensi `.py`.

2. Jalankan file tersebut dengan perintah berikut melalui terminal:

   ```bash
   python nama_file.py
   ```

   Gantilah `nama_file.py` dengan nama file tempat Anda menyimpan kode ini.

## Hasil

Setelah kode dijalankan, jendela aplikasi kalkulator akan muncul. Anda dapat mengklik tombol angka, tombol operasi matematika, tombol "C" untuk menghapus, dan tombol "=" untuk menghitung hasil perhitungan. Hasil perhitungan akan ditampilkan di layar kalkulator.

Selamat mencoba menggunakan kalkulator sederhana ini!
