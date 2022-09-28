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
>1. Pengguna mengirimkan request berupa mengakses browser dan browser akan men-generate HTTP ke http://host/path. Selanjutnya, server akan menerima HTTP Request dari pengguna.
>2. 

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

>xxx