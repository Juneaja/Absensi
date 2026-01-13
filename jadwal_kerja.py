import sqlite3
from datetime import datetime

# Fungsi untuk membuat koneksi database
def create_connection():
    conn = sqlite3.connect('jadwal_kerja.db')
    return conn

# Fungsi untuk membuat tabel jika belum ada
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jadwal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_karyawan TEXT NOT NULL,
            tanggal TEXT NOT NULL,
            jam_masuk TEXT NOT NULL,
            jam_pulang TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Fungsi CREATE: Tambah jadwal baru
def create_jadwal(nama, tanggal, jam_masuk, jam_pulang):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO jadwal (nama_karyawan, tanggal, jam_masuk, jam_pulang) VALUES (?, ?, ?, ?)',
                   (nama, tanggal, jam_masuk, jam_pulang))
    conn.commit()
    conn.close()
    print("Jadwal berhasil ditambahkan!")

# Fungsi READ: Lihat semua jadwal
def read_jadwal():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM jadwal')
    rows = cursor.fetchall()
    conn.close()
    if rows:
        print("Daftar Jadwal Kerja:")
        for row in rows:
            print(f"ID: {row[0]}, Nama: {row[1]}, Tanggal: {row[2]}, Masuk: {row[3]}, Pulang: {row[4]}")
    else:
        print("Tidak ada jadwal.")

# Fungsi UPDATE: Edit jadwal berdasarkan ID
def update_jadwal(id_jadwal, nama, tanggal, jam_masuk, jam_pulang):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE jadwal SET nama_karyawan=?, tanggal=?, jam_masuk=?, jam_pulang=? WHERE id=?',
                   (nama, tanggal, jam_masuk, jam_pulang, id_jadwal))
    conn.commit()
    conn.close()
    print("Jadwal berhasil diperbarui!")

# Fungsi DELETE: Hapus jadwal berdasarkan ID
def delete_jadwal(id_jadwal):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM jadwal WHERE id=?', (id_jadwal,))
    conn.commit()
    conn.close()
    print("Jadwal berhasil dihapus!")

# Menu utama
def main():
    create_table()
    while True:
        print("\n=== Sistem Jadwal Masuk dan Pulang Kerja ===")
        print("1. Tambah Jadwal (Create)")
        print("2. Lihat Jadwal (Read)")
        print("3. Edit Jadwal (Update)")
        print("4. Hapus Jadwal (Delete)")
        print("5. Keluar")
        pilihan = input("Pilih opsi: ")
        
        if pilihan == '1':
            nama = input("Nama Karyawan: ")
            tanggal = input("Tanggal (YYYY-MM-DD): ")
            jam_masuk = input("Jam Masuk (HH:MM): ")
            jam_pulang = input("Jam Pulang (HH:MM): ")
            create_jadwal(nama, tanggal, jam_masuk, jam_pulang)
        elif pilihan == '2':
            read_jadwal()
        elif pilihan == '3':
            id_jadwal = int(input("ID Jadwal yang akan diedit: "))
            nama = input("Nama Karyawan baru: ")
            tanggal = input("Tanggal baru (YYYY-MM-DD): ")
            jam_masuk = input("Jam Masuk baru (HH:MM): ")
            jam_pulang = input("Jam Pulang baru (HH:MM): ")
            update_jadwal(id_jadwal, nama, tanggal, jam_masuk, jam_pulang)
        elif pilihan == '4':
            id_jadwal = int(input("ID Jadwal yang akan dihapus: "))
            delete_jadwal(id_jadwal)
        elif pilihan == '5':
            print("Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
