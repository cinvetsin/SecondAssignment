### **Nama:**

Sasha Nabila Fortuna

### **NPM:**

2106632226

### **Link Heroku:**
[https://second-assignment.herokuapp.com/](https://second-assignment.herokuapp.com/)

1. Berikut bagan keterkaitan antara views.py, models.py, urls.py, dan katalog.html.

![logo](https://drive.google.com/file/d/15m2bbMt-Kp1igwLSq5Ww4GXWQugH63Uy/view?usp=sharing)

Django merupakan framework yang mengikuti struktur MVT (Model-View-Template). Model berperan sebagai objek yang menggambarkan entitas dari database dan konfigurasinya. View adalah logika dari aplikasi. Template adalah apa yang ditampilkan kepada pengguna.

Berikut alur saat permintaan diproses di Django. Pertama, permintaan akan masuk ke urlsdan diteruskan ke views. Jika dalam prosesnya memerlukan database, views akan memanggil query ke models dan hasilnya akan dikembalikan ke views. Setelah permintaan telah selesai diproses, hasilnya akan dipetakan ke dalam HTML yang sudah didefinisikan sebelum akhirnya HTML dikembalikan ke pengguna sebagai bentuk dari respons.

2. Kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan untuk mengelola Python Packages. Dengan menggunakan virtual environment, dapat menghindarkan kita dari mengunduh Python Packages secara global yang dapat merusak peralatan sistem maupun proyek lainnya. Tanpa menggunakan virtual environment, kita masih bisa membuat aplikasi web berbasis Django. Hanya saja, kita harus bersedia untuk melakukan overwrite global packages dengan kebutuhan proyek yang sedang dibuat.

3. Cara mengimplementasikan poin 1 sampai dengan 4 di atas:
* Pada poin pertama, kita melakukan import class yang ada di models.py. Setelahnya, kita ambil semua object di dalamnya dan kita mendefinisikan object-object tersebut sesuai keinginan kita. Selanjutnya, lakukan render request dan file template-nya.
* Pada poin kedua, melakukan konfigurasi routing pada file urls.py di folder project_django. Pada file tersebut, kita membuat path untuk project kita.
* Pada poin ketiga, pada data yang telah di-render di views, kita bisa memunculkannya di halaman HTML. Django memiliki sintaks khusus template untuk melakukan mapping, yaitu {{data}}.
* Pada poin terakhir, agar kita bisa menunjukkan proyek kita ke pengguna, kita akan melakukan deploy aplikasi Django. Kita bisa memanfaatkan Heroku sebagai host dari aplikasi yang akan kita deploy.