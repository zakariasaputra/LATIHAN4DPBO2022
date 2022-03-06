# Design Pemrograman Berorientasi Objek
Repositori ini dibuat untuk memenuhi tugas latihan dari Mata Kuliah Desain Pemrograman Berorientasi Objek di Semester 4 pada Program Studi Ilmu Komputer Universitas Pendidikan Indonesia. Di dalamnya terdapat beberapa implementasi kelas dalam bahasa PHP, C++, Python, dan Java.
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

### Design and Detail
Design Class</br>
![Design](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/00e35143faa68e5cfe6506e8cf7926de8067e7db/Desain/Desain.png)

### Tools
- [Python](https://www.python.org/) : Python
- Text Editor

### Usage
* Masuk ke directory project dalam CMD
* Eksekusi Perintah berikut:
```
py [name].py
```
### Results
1. Airplane Class</br>
![SS A1](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/00e35143faa68e5cfe6506e8cf7926de8067e7db/Screenshot%20Hasil/Airplane%20Class_1.png)
![SS A2](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/00e35143faa68e5cfe6506e8cf7926de8067e7db/Screenshot%20Hasil/Airplane%20Class_2.png)
2. Ship Class</br>
![SS S1](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/00e35143faa68e5cfe6506e8cf7926de8067e7db/Screenshot%20Hasil/Ship%20Class_1.png)
![SS S2](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/00e35143faa68e5cfe6506e8cf7926de8067e7db/Screenshot%20Hasil/Ship%20Class_2png)
3. Person Class</br>
![SS P1](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/00e35143faa68e5cfe6506e8cf7926de8067e7db/Screenshot%20Hasil/Person%20Class_1.png)
![SS P2](https://github.com/zakariasaputra/LATIHAN4DPBO2022/blob/00e35143faa68e5cfe6506e8cf7926de8067e7db/Screenshot%20Hasil/Person%20Class_2png)

