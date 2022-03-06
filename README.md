# Design Pemrograman Berorientasi Objek
Repositori ini dibuat untuk memenuhi tugas latihan dari Mata Kuliah Desain Pemrograman Berorientasi Objek di Semester 4 pada Program Studi Ilmu Komputer Universitas Pendidikan Indonesia. Di dalamnya terdapat beberapa implementasi kelas dalam bahasa Python.
> Muhammad Zakaria Saputra; 2007993; Ilmu Komputer-C1-2020; Universitas Pendidikan Indoneisa

### Project Description
Pada latihan kali ini terdapat penerapan dari materi "Inheritance dan Composition" di mana pada project kali ini terdapat 6 kelas yaitu kelas Vehicle, Ship, Airplane, Person, Job, dan Driver. Vehicle merupakan parent dari Ship dan Airplane, kemudian Job adalah parent dari Driver, dan Driver meng-composite Person. Berikut atribut dari masing-masing kelas:
* Vehicle 
  * modelName 
  * fuelType 
  * maxPassengers 
  * Move() 
  * type 
  * age
* Ship 
  * countryOfManufacture
  * Length
  * Beam	
* Airplane
  * wingsLength 
  * firstFlight
  * status

* Person
  * NIK 
  * Name 
  * Gender 
  * sleep()
* Job 
  * NIP 
  * companyName
  * position
* Driver 
  * lisenceID
  * activeUntil
  * vehicleType

### Design and Details
#### Design Class
![Design](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/c6099d748c13a62b32197949c14adef9624db427/Desain/Design.png)

#### Details
* Desain untuk kelas Vehicle, Ship, dan Airplane merupakan **Hierarchical Inheritance**, di mana Vehicle merupakan parent dari kelas Airplane dan Ship. Alasan digunakannya desain ini adalah karena penulis memandang bahwa kelas Airplane dan Ship merupakan turunan dari kelas Vehicle, di mana baik Airplane maupun Ship, keduanya merupakan jenis Vehicle.
* Dilakukan pemindahan atribut ‘age’ dan ‘type’ dari kelas Airplane dan Ship ke kelas Vehicle. Pemindahan ini dikarenakan baik pada kelas Airplane maupun Ship sama-sama terdapat 2 atribut tersebut, dan seperti yang kita ketahui kelas Airplane dan Ship merupakan child dari kelas Vehicle, maka pemindahan atribut ini dapat dilakukan. Nantinya, kedua kelas child (Airplane dan Ship) cukup menggunakan derived attribute dari kelas Vehicle.
* Dilakukan penambahan atribut untuk kelas Airplane (wingsLength, firstFlight, status) dan untuk kelas Ship (Length, Beam), penambahan ini dikarenakan kelas Airplane dan Ship kini hanya memiliki 1 atribut (kelas dengan 1 atribut tidak disarankan). 
* Desain untuk kelas Job dan Driver merupakan **Simple Inheritance**, di mana Job merupakan parent dari kelas Driver. Alasan digunakannya desain ini adalah karena penulis memandang bahwa kelas Driver merupakan turunan dari kelas Job, di mana Driver merupakan jenis Job.
* Pada dasarnya kelas Person berdiri sendiri karena kenyataannya kelas Person bukanlah parent ataupun child dari kelas lain sehingga tidak digunakan inheritance untuk kelas ini. Kemudian sebenarnya bisa saja kelas Person meng-composite kelas Job, tetapi bukan itu desain yang diinginkan case kali ini melainkan di sini kelas Person dapat meng - **composite** kelas Driver yang menunjukkan bahwa Person itu memiliki pekerjaan sebagai Driver.

### Tools
- [Python](https://www.python.org/)
- Text Editor

### Usage
* Masuk ke directory project dalam CMD
* Eksekusi Perintah berikut:
```
py [name].py
```
### Results
1. Airplane Class</br>
![SS A1](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/00e35143faa68e5cfe6506e8cf7926de8067e7db/Screenshot%20Hasil/Airplane%20Class_1.png)</br>
![SS A2](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/00e35143faa68e5cfe6506e8cf7926de8067e7db/Screenshot%20Hasil/Airplane%20Class_2.png)
2. Ship Class</br>
![SS S1](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/00e35143faa68e5cfe6506e8cf7926de8067e7db/Screenshot%20Hasil/Ship%20Class_1.png)</br>
![SS S2](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/caaaf6e3508510ffaed910812e34f3980c95f207/Screenshot%20Hasil/Ship%20Class_2.png)
3. Person Class</br>
![SS P1](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/00e35143faa68e5cfe6506e8cf7926de8067e7db/Screenshot%20Hasil/Person%20Class_1.png)</br>
![SS P2](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/caaaf6e3508510ffaed910812e34f3980c95f207/Screenshot%20Hasil/Person%20Class_2.png)

