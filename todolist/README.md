### **Nama:**

Sasha Nabila Fortuna

### **NPM:**

2106632226

### **Link Heroku:**
[https://second-assignment.herokuapp.com/todolist](https://second-assignment.herokuapp.com/todolist)

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