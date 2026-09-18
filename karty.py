import streamlit as st
import random
st.title("KARTA POSTACI")
początek = [
  "Boży",
  "Dar",
  "Sła",
  "Gra",
  "Lina",
  "Bogu",
  "Mir"
]
koniec_damski = [
  "bora",
  "mora",
  "sława",
  "bola",
  "woja",
  "oka"
]
koniec_męski = [
  "bór",
  "dar",
  "mór",
  "sław",
  "knur",
  "ból",
  "sławój"
]

wylosowany_początek = random.choice(początek)
wylosowany_koniec_męski = random.choice(koniec_męski)
wylosowany_koniec_damski = random.choice(koniec_damski)
płeć = st.selectbox("Wybierz płeć:", ["Kobieta", "Mężczyzna"], key="plec")
if płeć == "Kobieta":
 st.write("Imię:", wylosowany_początek + wylosowany_koniec_damski)
 st.write("Płeć: Kobieta")
elif płeć == "Mężczyzna":
 st.write("Imię:", wylosowany_początek + wylosowany_koniec_męski)
 st.write("Płeć: Mężczyzna")
  
siła = random.randint(1,100)
szybkość = random.randint(1,100)
inteligencja = random.randint(1,100)
charyzma = random.randint(1,100)
szczęście = random.randint(1,100)
zręczność = random.randint(1,100)
klasy = [
  "Paladyn Kapitalista", 
  "Pół Majster - Pół Grafik", # łotrzyk,
  "Przeklęty Bard", 
  "Mnich Alkoholik" 
]
wylosowana_klasa = random.choice(klasy)
if wylosowana_klasa == "Paladyn Kapitalista":
  siła = random.randint(81,100)
  inteligencja = random.randint(61,100)
  print("Klasa:", "Paladyn Kapitalista")
elif wylosowana_klasa == "Pół Majster - Pół Grafik":
  zręczność = random.randint(61,100)
  charyzma = random.randint(61,100)
  print("Klasa:", "Pół Majster - Pół Grafik")
elif wylosowana_klasa == "Przeklęty Bard":
  szczęście = random.randint(1,30)
  charyzma = random.randint(61,100)
  print("Klasa:", "Przeklęty Bard")
elif wylosowana_klasa == "Mnich Alkoholik":
  zręczność = random.randint(1,30)
  szybkość = random.randint(1,30)
  print("Klasa:", "Mnich Alkoholik")
print("")
print("STATYSTYKI:")
print("Siła:", siła)
print("Szybkość:", szybkość)
print("Zręczność:", zręczność)
print("Inteligencja:", inteligencja)
print("Charyzma:", charyzma)
print("Szczęście:", szczęście)
