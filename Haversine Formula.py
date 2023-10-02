import math

# Masukkan koordinat dalam derajat
lat1 = math.radians(float(input("Masukan lattitude kota pertama: ")))
long1 = math.radians(float(input("Masukan longitude kota pertama: ")))
lat2 = math.radians(float(input("Masukan lattitude kota kedua: ")))
long2 = math.radians(float(input("Masukan longitude kota kedua: ")))

# Haversine formula
Δlat = lat2 - lat1
Δlong = long2 - long1

a = math.sin(Δlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(Δlong / 2) ** 2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# Radius Bumi dalam kilometer
radius = 6371

# Hitung jarak dalam kilometer
distance = radius * c

print("Jarak antara dua titik adalah:", distance, "kilometer")


