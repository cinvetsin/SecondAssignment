### **Nama:**

Sasha Nabila Fortuna

### **NPM:**

2106632226

### **Link Heroku:**
[https://second-assignment.herokuapp.com/mywatchlist](https://second-assignment.herokuapp.com/mywatchlist)


**1. Jelaskan perbedaan antara JSON, XML, dan HTML!**

>HTML (Hyper Text Markup Language) adalah markup language standar untuk dokumen yang dirancang untuk ditampilkan ke browser web. HTML sendiri menggambarkan struktur halaman web secara semantik. Elemen dari HTML sendiri adalah building block pada halaman HTML.

>XML (eXtensible Markup Language) juga merupakan markup language. Namun, XML dirancang untuk mendeskripsikan data dan berfokus pada definisi dari data itu sendiri. Pada XML, kita harus mendefinisikan sendiri tag yang kita pakai, sedangkan pada HTML, kita harus menggunakan predefined tag. Lalu, jika menggunakan XML, data akan disimpan di luar HTML. Sedangkan jika kita ingin menampilkan data dalam bentuk HTML, data akan disimpan di dalam HTML.

>JSON (JavaScript Object Notation) adalah format pertukaran data yang ringan dan sepenuhnya tidak bergantung pada bahasa apapun. Format JSON sendiri identik dengan kode untuk membuat objek JavaScript. Oleh karena itu, program JavaScript mudah untuk melakukan konversi dari data JSON ke objek native JavaScript.

>Ada beberapa hal yang membedakan JSON dengan yang lainnya, yaitu JSON menggunakan array, jika dibandingkan dengan XML, file-nya lebih mudah untuk dibaca. Namun, XML, jauh lebih aman daripada JSON. Selain itu, JSON tidak menggunakan end tag dan hanya menerima encoding UTF-8.

**2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

>Pada dasarnya, proses data delivery pada platform terjadi saat client mengirimkan request berupa HTTP Request ke Web Server. Di web server, request akan di-forward ke view yang nantinya akan dibaca/ditulis oleh model. Setelah proses request sudah terjadi di server, hasil/responsenya akan dikembalikan ke client berupa HTTP Response dan browser memberikan tampilan sesuai dengan permintaan client.

**3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

- Pada checklist pertama, kita membuat `django-app` bernama `mywatchlist` dengan perintah `python manage.py startapp mywatchlist`.

- Pada checklist kedua, kita membuat path   `mywatchlist` pada file `urls.py` baik di folder `project_django` dan folder `mywatchlist`.

- Pada checklist ketiga, kita membuat model dari `mywatchlist` dengan atribut `watched`, `title`, `rating`, `release_date`, dan `review`. Lalu, atur juga untuk tampilan template-nya menyesuaikan dengan atribut yang sudah disusun.

- Pada checklist keempat, buat minimal 10 data untuk objek `MyWatchList` dengan atribut yang sudah ditentukan. Lalu, simpan datanya di file JSON

- Pada checklist kelima, lakukan pengaturan agar data dapat dikembalikan dalam bentuk HTML, XML, dan JSON pada file `views.py`

- Pada checklist keenam, lakukan routing agar data dapat dikembalikan dan bentuk HTML, XML, dan JSON pada file `urls.py` di folder `mywatchlist`

- Pada checklist ketujuh, lakukan deploy ke link heroku yang sudah pernah dibuat pada tugas sebelumnya. Perlu diperhatikan ketika melakukan deploy, pastikan kita sudah melakukan loaddata JSON ke `Procfile`.

### **Screenshot Akses Tiga URL di Postman**

**1. HTML**
![mywatchlist/html/](https://drive.google.com/uc?id=1JkH9-ahkoIxSwLsy5PWoUfuoJDMqbDIv)

**2. XML**
![mywatchlist/xml/](https://drive.google.com/uc?id=1avFs3j_LglIURWr_P-kVbS5kzCxyvuRX)

**3. JSON**
![mywatchlist/json/](https://drive.google.com/uc?id=1hzioSPnsmmMgC-s6MazfK-SwLqQ8Rz-Q)