# Proyek Analisis Data Penyewaan Sepeda

## Informasi Proyek

-   **Nama:** Ade Hilman Mufid
-   **Email:** mufidadehilman@gmail.com
-   **ID Dicoding:** ade_hilman_mufid

Bike Sharing Dashboard

Proyek ini bertujuan untuk menganalisis pola penggunaan layanan Bike Sharing berdasarkan faktor lingkungan dan karakteristik pengguna. Analisis dilakukan menggunakan teknik Exploratory Data Analysis (EDA) untuk memperoleh insight yang dapat membantu pengambilan keputusan operasional dan strategi pemasaran layanan bike sharing.

Pertanyaan Bisnis

1. Bagaimana pengaruh temperatur terhadap jumlah peminjaman sepeda dan pada rentang temperatur berapa tingkat peminjaman mencapai kondisi optimal?
2. Bagaimana pola peminjaman sepeda berdasarkan musim serta bagaimana perbedaan kontribusi antara pengguna casual dan registered pada setiap musim?

Dataset

Dataset yang digunakan merupakan Bike Sharing Dataset yang berisi informasi terkait penyewaan sepeda harian.
Dataset mencakup beberapa variabel penting seperti:

Musim
Kondisi cuaca
Temperatur
Kelembapan
Kecepatan angin
Jumlah pengguna casual
Jumlah pengguna registered
Total peminjaman sepeda

Data Preparation

Tahapan persiapan data yang dilakukan meliputi:
Menghapus data duplikat
Mengubah label kategori agar lebih mudah dipahami
Membuat fitur tambahan seperti:
Kategori temperatur
Klasifikasi hari kerja dan hari libur
Menyimpan dataset yang telah dibersihkan untuk keperluan analisis dan dashboard

Exploratory Data Analysis
Analisis dilakukan untuk memahami hubungan antara variabel lingkungan dan pola penggunaan layanan bike sharing, meliputi:
Analisis hubungan temperatur terhadap jumlah peminjaman sepeda
Analisis pola peminjaman berdasarkan musim
Analisis perbandingan pengguna casual dan registered
Analisis korelasi antar variabel lingkungan

Insight Utama

Peminjaman sepeda meningkat pada temperatur moderat hingga tinggi.
Musim panas dan gugur menunjukkan tingkat penggunaan sepeda tertinggi.
Pengguna registered mendominasi penggunaan layanan bike sharing.
Kelembapan udara cenderung menurunkan tingkat penggunaan sepeda.

Dashboard

Dashboard interaktif dibuat menggunakan Streamlit untuk memvisualisasikan hasil analisis secara dinamis dan memudahkan eksplorasi data.
Dashboard menampilkan:
Analisis pengaruh temperatur terhadap peminjaman sepeda
Perbandingan penggunaan sepeda berdasarkan musim
Perbandingan tipe pengguna
Insight utama hasil analisis

Installation

Clone repository atau download project
Install dependencies
pip install -r requirements.txt

Menjalankan Dashboard

Masuk ke folder project kemudian jalankan:
streamlit run dashboard/dashboard.py

Tools & Libraries

Python
Pandas
Matplotlib
Seaborn
Streamlit

Conclusion

Hasil analisis menunjukkan bahwa faktor lingkungan seperti temperatur dan musim memiliki pengaruh signifikan terhadap tingkat penggunaan layanan bike sharing. Selain itu, pengguna registered menjadi kontributor utama dalam penggunaan layanan, yang menunjukkan bahwa bike sharing tidak hanya digunakan untuk rekreasi tetapi juga sebagai sarana transportasi harian.

👨‍💻 Author

Submission Proyek Analisis Data - Dicoding
