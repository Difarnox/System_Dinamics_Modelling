import numpy as np  # Mengimpor library numpy untuk perhitungan numerik dan array
import matplotlib.pyplot as plt  # Mengimpor matplotlib.pyplot untuk membuat grafik

# Data peralatan listrik
peralatan = {
    "Kulkas": {"daya": 150, "jam": [24, 20, 24, 22, 24]},  # Daya kulkas dalam watt dan jam penggunaan bulanan
    "Komputer": {"daya": 300, "jam": [5, 8, 6, 9, 7]},  # Daya komputer dan jam penggunaan bulanan
    "Televisi": {"daya": 100, "jam": [2, 3, 1, 4, 2]},  # Daya televisi dan jam penggunaan bulanan
    "AC": {"daya": 800, "jam": [3, 6, 4, 7, 5]},  # Daya AC dan jam penggunaan bulanan
}  # Atribut = Daya dan Jam

# Fungsi untuk menghitung konsumsi energi bulanan dalam kWh
def hitung_konsumsi_bulanan(peralatan):
    konsumsi = {}  # Inisialisasi dictionary kosong untuk menyimpan hasil konsumsi energi

    for nama, data in peralatan.items():  # Iterasi setiap peralatan dalam dictionary
        # Hitung energi dalam kWh untuk 30 hari berdasarkan jam penggunaan
        konsumsi[nama] = [(data["daya"] / 1000) * jam * 30 for jam in data["jam"]]  # Menghitung konsumsi energi

    return konsumsi  # Mengembalikan hasil perhitungan konsumsi energi

# Menghitung konsumsi energi untuk setiap bulan
konsumsi_energi = hitung_konsumsi_bulanan(peralatan)  # Memanggil fungsi untuk menghitung konsumsi energi

# Menghitung total konsumsi energi bulanan
total_konsumsi = np.sum(list(konsumsi_energi.values()), axis=0)  # Menjumlahkan total konsumsi per bulan

# Output hasil
print("Konsumsi Energi (kWh) per Bulan dari Januari hingga Mei:")
for bulan in range(5):  # Iterasi melalui setiap bulan
    print(f"Bulan {bulan + 1}:")  # Menampilkan bulan
    for nama, energi in konsumsi_energi.items():  # Iterasi setiap peralatan
        print(f"{nama}: {energi[bulan]:.2f} kWh")  # Menampilkan konsumsi energi per peralatan
    print(f"Total: {total_konsumsi[bulan]:.2f} kWh\n")  # Menampilkan total konsumsi bulanan

# Grafik konsumsi energi
bulan_label = ['Januari', 'Februari', 'Maret', 'April', 'Mei']  # Label bulan untuk sumbu X
bar_width = 0.15  # Lebar batang grafik

plt.figure(figsize=(12, 6))  # Mengatur ukuran figure grafik

# Menambahkan batang untuk setiap peralatan
for i, (nama, energi) in enumerate(konsumsi_energi.items()):  # Iterasi setiap peralatan
    bar_positions = np.arange(len(bulan_label)) + i * bar_width  # Menghitung posisi batang
    bars = plt.bar(bar_positions, energi, width=bar_width, label=nama)  # Membuat batang untuk grafik

    # Menambahkan nilai konsumsi di atas setiap batang peralatan
    for bar in bars:  # Iterasi melalui setiap batang
        yval = bar.get_height()  # Mengambil tinggi batang (nilai konsumsi)
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f"{yval:.2f}", ha='center', va='bottom')  # Menampilkan nilai di atas batang

# Menambahkan garis untuk total konsumsi
plt.plot(bulan_label, total_konsumsi, marker='o', color='black', linewidth=2, label='Total Konsumsi', linestyle='--')  # Menambahkan garis total konsumsi

# Menambahkan label dan judul
plt.ylabel('Konsumsi Energi (kWh)')  # Menambahkan label untuk sumbu Y
plt.title('Model Konsumsi Energi Listrik Bulanan per Peralatan')  # Menambahkan judul grafik
plt.xticks(np.arange(len(bulan_label)) + bar_width * 1.5, bulan_label)  # Menyesuaikan posisi label bulan
plt.grid(axis='y')  # Mengaktifkan grid pada sumbu Y
plt.legend(frameon=False)  # Menambahkan legenda tanpa bingkai

# Menampilkan total konsumsi di grafik
for i, v in enumerate(total_konsumsi):  # Iterasi melalui total konsumsi
    plt.text(i + bar_width * len(peralatan) / 2 - bar_width / 2, v + 1, f"{v:.2f}", ha='center')  # Menampilkan total konsumsi di atas garis

plt.tight_layout()  # Memastikan layout grafik tidak tumpang tindih
plt.show()  # Menampilkan grafik yang telah dibuat
