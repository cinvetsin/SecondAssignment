### **Nama:**

Sasha Nabila Fortuna

### **NPM:**

2106632226

### **Link Heroku:**
[https://second-assignment.herokuapp.com/todolist](https://second-assignment.herokuapp.com/todolist)

**1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**

>Pada asynchronus programming, beberapa operasi yang terkait dapat dijalankan tanpa menunggu task lain selesai (atau tanpa harus menunggu response dari server). Pada synchronus programming, satu task baru bisa dijalankan jika task sebelumnya sudah selesai dijalankan atau dengan kata lain, harus menunggu respon dari server.

**2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

>Penerapan event-driven programming yaitu dengan user men-trigger suatu event sehingga membuat event tersebut terjadi. Selanjutnya, dijalankan function yang meng-handle event tersebut. Setelah menjalankan function-nya, tampilan halaman akan termodifikasi sebagai akibat dari mentrigger suatu event.
>
>Contoh pada tugas ini yaitu ketika kita ingin menambahkan tugas, kita memunculkan form modal untuk menambahkan task. Lalu ketik men-submit task yang dibuat, secara asinkronus menambahkan task di halaman utama todolist (tanpa harus melakukan reload).

**3. Jelaskan penerapan asynchronous programming pada AJAX.**

>Berikut proses AJAX bekerja secara asinkronus:
>1. Ketika halaman HTML di-load, data dibaca dari web server
>2. Tanpa harus melakukan reload pada halaman web, data sudah ter-update
>3. Transfer data terjadi ke web server di balik layar
>
>Dengan asynchronous programming, membantu dalam menciptakan konten web HTML yang responsif dengan performa yang lebih cepat. 

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

>1. Pada checklist pertama, membuat views baru pada `get_todolist_json` untuk mengembalikan seluruh data ke dalam bentuk JSON
>2. Pada checklist kedua, membuat routing views `get_todolist_json` ke `todolist/json`
>3. Pada checklist ketiga, mengimplementasikan AJAX GET pada `function getTask()`
>4. Pada checklist keempat, menerapkan modal bootstrap untuk menampilkan form untuk menambahkan task baru dengan tombol `Add Task` sebagai event trigger-nya.
>5. Pada checklist kelima, membuat views untuk form buat task baru pada `add_todolist`
>6. Pada checklist keenam, membuat routing views `add_todolist` ke `todolist/add`
>7. Pada checklist ketujuh dan kedelapan, ketika kita sudah melakukan submit untuk task baru yang baru kita masukkan, modal langsung tertutup dan list task ter-update secara asinkronus.
