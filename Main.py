""" 
Saya Muhammad Zakaria Saputra 2007993 mengerjakan Latihan 4 C1 dalam
mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin 
"""
from Job import Job
from Driver import Driver
from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane
from Person import Person

#Create Array for Airplane Class
#5 Dummy Data
airplane = [Airplane(79.8, 2005, "In Service"), Airplane(90, 1969, "In Service"), Airplane(59.6, 1988, "In Service"), Airplane(64.8, 1994, "In Service"), Airplane(60.3, 1991, "In Production")] 

#Set Airplane Derived Attribute from Vehicle Class
airplane[0].setModelName("Airbus A380")
airplane[0].setAge(17)
airplane[0].setMaxPassengers(525)
airplane[0].setType("Airbus")
airplane[0].setFuelType("Jet Kerosene")

airplane[1].setModelName("Boeing 747")
airplane[1].setAge(52)
airplane[1].setMaxPassengers(366)
airplane[1].setType("Boeing")
airplane[1].setFuelType("Jet Kerosene")

airplane[2].setModelName("Boeing 747-400")
airplane[2].setAge(34)
airplane[2].setMaxPassengers(416)
airplane[2].setType("Boeing")
airplane[2].setFuelType("Kerosene")

airplane[3].setModelName("Boeing 777")
airplane[3].setAge(27)
airplane[3].setMaxPassengers(368)
airplane[3].setType("Boeng")
airplane[3].setFuelType("Jet Fuel")

airplane[4].setModelName("Airbus A340")
airplane[4].setAge(28)
airplane[4].setMaxPassengers(370)
airplane[4].setType("Airbus")
airplane[4].setFuelType("Aviation Fuel")

#Print All of Attribute
print("AIRPLANE CLASS :")
print("/////////////////////")
for i in range(0,5):
    airplane[i].printAirplaneClass()
print("/////////////////////")

#Create Array for Ship Class
#5 Dummy Data
ship = [Ship("Bahamas", 361.011, 47.448), Ship("Bahamas", 362.12, 47.42), Ship("Bahamas", 362, 47), Ship("Italy", 337, 42), Ship("Italy", 337, 42)]

#Set Airplane Derived Attribute from Vehicle Class
ship[0].setModelName("Symphony of the Seas")
ship[0].setAge(5)
ship[0].setFuelType("Solar")
ship[0].setMaxPassengers(6680)
ship[0].setType("Cruise Ship")

ship[1].setModelName("Harmony of the Seas")
ship[1].setAge(7)
ship[1].setFuelType("Liquefied Natural Gas (LNG)")
ship[1].setMaxPassengers(6780)
ship[1].setType("Cruise Ship")

ship[2].setModelName("Allure of the Seas")
ship[2].setAge(13)
ship[2].setFuelType("Liquefied Natural Gas (LNG)")
ship[2].setMaxPassengers(6780)
ship[2].setType("Cruise Ship")

ship[3].setModelName("Costa Smeralda")
ship[3].setAge(3)
ship[3].setFuelType("Liquefied Natural Gas (LNG)")
ship[3].setMaxPassengers(6554)
ship[3].setType("Cruise Ship")

ship[4].setModelName("AIDAnova")
ship[4].setAge(4)
ship[4].setFuelType("Liquefied Natural Gas (LNG)")
ship[4].setMaxPassengers(6654)
ship[4].setType("Cruise Ship")

#Print All of Attribute
print("SHIP CLASS :")
print("/////////////////////")
for i in range(0,5):
    ship[i].printShipClass()
print("/////////////////////")

#Create Array for Person Class
#5 Dummy Data
person = [Person("3001313112", "Mang Asep", "Male", Driver("A0001", 2026, "Motorcycle")), Person("3001313112", "Mang Jajang", "Male", Driver("D001", 2025, "Car")), Person("1237771191", "Mang Ujang", "Male", Driver("D002", 2023, "Car")), Person("1931777711", "Neng Ida", "Female", Driver("B001", 2025, "Motorcycle")), Person("1269199121", "Mang Cecep", "Male", Driver("A002", 2023, "Motorcycle"))]

#Set Driver Derived Attribute from Job Class
person[0].getDriver().setNip("99001")
person[0].getDriver().setCompanyName("Grab")
person[0].getDriver().setPosition("Employee")

person[1].getDriver().setNip("88001")
person[1].getDriver().setCompanyName("Gojek")
person[1].getDriver().setPosition("Employee")

person[2].getDriver().setNip("77001")
person[2].getDriver().setCompanyName("Bluebird")
person[2].getDriver().setPosition("Driver")

person[3].getDriver().setNip("66001")
person[3].getDriver().setCompanyName("Shopee")
person[3].getDriver().setPosition("Courier")

person[4].getDriver().setNip("88002")
person[4].getDriver().setCompanyName("Gojek")
person[4].getDriver().setPosition("Employee")

#Print All of Attribute
print("PERSON CLASS :")
print("/////////////////////")
for i in range(0,5):
    person[i].printtPersonClass()
print("/////////////////////")