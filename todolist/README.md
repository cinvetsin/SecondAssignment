### **Nama:**

Sasha Nabila Fortuna

### **NPM:**

2106632226

### **Link Heroku:**
[https://second-assignment.herokuapp.com/todolist](https://second-assignment.herokuapp.com/todolist)

## **Tugas 4**
**1. Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?**

>CSRF token di-*generate* oleh server ke dalam bentuk string yang acak dan sulit untuk ditebak. CSRF token ini akan ditambahkan ke form secara tersembunyi. CSRF token digunakan sebagai bentuk proteksi dari serangan CSRF (*Cross Site Request Forgery*). Karena bentuk acak, sulit ditebak, dan tersembunyi pada tiap sesi pengguna (*user's session*), para *bad actor* ketika menyalin *static source code* dari halaman kita ke website berbeda akan menjadi tindakan yang sia-sia.
>
>Jika `{% csrf_token %}` tidak disisipkan pada elemen `<form>`, maka para *bad actor* akan dengan mudah untuk mengubah/memalsukan *referred header*. Dengan begitu, hal-hal berbahaya bisa saja terjadi. Misal, jika mengakses internet banking dan terkena serang CSRF, maka mungkin saja terjadi jika uang kita di internet banking dikuras habis.

**2. Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.**

>Kita bisa saja membuat elemen `<form>` secara manual. Hanya saja, ada beberapa hal yang perlu kita perhatikan, terutama mengenai autentikasi pengguna. Ketika melakukan proses autentikasi, berikut hal-hal yang perlu dipikirkan:
>
>1. Cara untuk menyimpan kata sandi dengan aman.
>2. Hal yang perlu dilakukan untuk membantu pengguna ketika lupa dengan kata sandi akunnya.
>3. Cara untuk menyakinkan pengguna untuk menyetel kata sandi yang baik.

**3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**

>Berikut alur data dari submisi pengguna melalui HTML form hingga memunculkan data pada template HTML:
>
>1. Pengguna mengirimkan *request* berupa mengakses browser dan browser akan men-*generate* HTTP ke http://host/path. Selanjutnya, server akan menerima HTTP Request dari pengguna.
>2. Server akan melihat *path* dari *request* pengguna yang akan di-*handle* oleh `views.py`. Jika *path*-nya merujuk pada halaman form HTML, server akan men-*generate*-nya dan menampilkan *layout* HTML ke pengguna.
>3. Selanjutnya, pengguna akan mengisi form. Setelah form itu di-submit pengguna, browser akan men-generate HTTP Request, method, dan arguments ke URL tujuan berdasarkan halaman form HTML. Selanjutnya, server akan menerima HTTP Request dari browser.
>4. Server akan menghandle lagi path dari *request* pengguna di `views.py` dan menjalankan instruksi sesuai dengan kebutuhan dan kegunaan dari aplikasi. Setelah itu, server akan men-*generate* halaman HTML dan browser akan menampilkan *layout* HTML ke pengguna.

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

>1. Pada checklist pertama, kita membuat `django-app` bernama `todolist` dengan perintah `python manage.py startapp todolist`.
>2. Pada checklist kedua, kita membuat path `todolist` pada file `urls.py` baik di folder `project_django` dan folder `todolist`.
>3. Pada checklist ketiga, kita membuat model dari `todolist` dengan atribut `user`, `date`, `title`, dan `description`. `user` sendiri menggunakan field ForeignKey dengan menerima parameter User. ForeignKey ini digunakan saat melakukan pemetaan pada binary relationship.
>4. Pada checklist keempat, implementasikan form registrasi, login, dan logout dengan membuat tampilan HTML nya dan mengatur logika dari tampilan HTML pada `views.py`.
>5. Pada checklist kelima, buat tampilan HTML utama yang menampilkan tabel berisi tanggal pembuatan task, judul task, dan deskripsi task. Lalu, ada nama pengguna yang sedang login, tombol tambah task, dan tombol logout pada `todolist.html`.
>6. Pada checklist keenam, membuat tampilan HTML yang menampilkan form untuk membuat task baru yang berisi judul dan deskripsi task pada `create.html` dan membuat class untuk atribut pada form untuk membuat task baru di `views.py` serta pengaturannya pada `views.py` juga.
>7. Pada checklist ketujuh, membuat routing untuk tampilan registrasi, login, logout, tampilan utama, dan tampilan untuk membuat task baru dengan menambahkan path-nya pada `urls.py`.
>8. Pada checklist kedelapan, lakukan deploy ke link heroku yang sudah pernah dibuat pada tugas sebelumnya.
>9. Pada checklist kesembilan, membuat dua akun dan tiga dummy data saat melakukan inputan pada situs web Heroku kita.

## **Tugas 5**
**1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**

>Berikut perbedaan dari Inline, Internal, dan External CSS:
>* Pada Inline CSS, menggunakan atribut `style` di dalam elemen HTML.
>* Pada Internal CSS, menggunakan elemen `<style>` di dalam head section.
>* Pada External CSS, menggunakan elemen `<link>` untuk menghubungkan ke file external CSS.
>
>Kelebihan Inline CSS adalah elemen-elemen tertentu memiliki style sendiri. Lalu, penggunaan inline CSS juga lebih efektif pada implementasi yang sederhana atau digunakan untuk landing page sehingga proses *load*-nya berjalan lebih cepat. Kekurangannya adalah file tidak di-cache sehingga setiap mengunjungi halaman dengan inline CSS, akan diperlakukan sebagai hal yang baru. *Caching* sendiri sebaiknay digunakan saat proyek yang dibuat semakin kompleks.
>
>Kelebihan dari Internal CSS adalah kita bisa melimit style pada satu halaman. Namun, internal CSS akan dinilai tidak efektif jika pada page tertentu, kita menggunakan style yang sama. Dengan begitu, kita harus menuliskan kembali style-nya untuk halaman yang berbeda.
>
>Kelebihan external CSS adalah style bisa digunakan pada beberapa page sekaligus. Hal ini membuat kita lebih fokus pada hal lain ketimbang web design karena kita tidak perlu mengkhawatirkannya berkat external CSS. Kekurangannya adalah beberpa page akan memiliki tampilan yang sama dan tidak memiliki kontrol untuk elemen-elemen tertentu.

**2. Jelaskan tag HTML5 yang kamu ketahui.**

>Berikut tag HTML5 yang saya ketahui:
>* `<audio>` untuk meng-embed suara atau audio stream ke dokumen HTML
>* `<dialog>` untuk mendefinisikan dialog box atau subwindow
>* `<embed>` untuk meng-embed aplikasi eksternal, biasanya berupa konten multimedia ke dokumen HTML
>* `<footer>` menggambarkan bagian footer dari dokumen atau section
>* `<header>` menggambarkan bagian header dari dokumen atau section
>* `<main>` menggambarkan konten main atau dominant dari dokumen
>* `<nav>` untuk mendefinisikan bagian dari link navigasi
>* `<picture>` untuk mendefinisikan section untuk beberapa sumber gambar
>* `<section>` untuk mendefinisikan section dari dokumen, seperti header, footer, dll.
>* `<source>` untuk menentukan sumber media alternatif pada elemen media seperti `<audio>` atau `<video>`.
>* `<video>` untuk mendefinisikan konten video pada dokumen HTML

**3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.**

>Berikut tipe-tipe CSS selector, yaitu:
>
>1. **Universal selector** (`*`) akan men-*select* semua elemen HTML pada satu halaman
>2. **Element selector** menggunakan tag HTML sebagai *selector* untuk mengubah properti yang terdapat dalam tag tersebut.
>3. **id Selector** menggunakan id pada tag sebagai *selector*. Untuk men-*select* pada id tertentu, bubuhi karakter pagar/*hash* (#), diikuti dengan id elemen
>4. **Class selector** men-*select* elemen HTML pada atribut class yang spesifik. Untuk men-*select* elemen dengan class tertentu, bubuhi karakter titik (.), diikuti dengan nama class.

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

>1. Pada checklist pertama, kustomisasi menggunakan bootstrap dan beberapa penyesuaian dengan CSS, dan kustomisasi dilakukan pada tampilan login, register, dan create-task. Pada halaman utama todo list, menggunakan card dengan template dari bootstrap.
>2. Pada checklist kedua, membuat semua halamannya menjadi responsive dengan:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```
>3. Pada bagian checklist bonus, melakukan hover dengan `selector:hover`, transformasi `scale(1.1)`, dan mengganti background color dengan warna violet untuk melakukan zoom serta pergantian warna saat di-*hover*