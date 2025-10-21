
# Credential Information
Username = "rhomairama"
Password = "223344"

# Customer Data Profile
customers = [
    {"ID": "G0001", "Name": "Ayu Tingting",   "Email": "ayu.tingting@gmail.com", "Phone": "081122334455"},
    {"ID": "G0002", "Name": "Vincent Rompis", "Email": "vincent@gmail.com",      "Phone": "082233223322"},
    {"ID": "G0003", "Name": "Surya Insomnia", "Email": "surya.in@gmail.com",        "Phone": "088122331122"},
    {"ID": "G0004", "Name": "Wendy Cagur",    "Email": "wendycags@yahoo.com",    "Phone": "085622331876"},
]

# Tabel Customer Data Profile
def show_data():
    print("\nKum-Bank Customer Data Profile")
    print("Index\tID\tName\t\tEmail\t\t\tPhone")
    print("-------------------------------------------------------------------")

    i = 0
    for c in customers:
        print(f"{i}\t{c['ID']}\t{c['Name']}\t{c['Email']}\t{c['Phone']}")
        i += 1

# Masuk Ke Menu Utama
def show_menu():
        print("===============================")
        print("Kum-Bank Customer Data Profile")
        print("===============================")
        print("1. Tampilkan Semua Data Customer")
        print("2. Menambah Data Customer Baru")
        print("3. Perbarui Data Customer")
        print("4. Hapus Data Customer")
        print("5. Keluar Menu")

# Masuk ke Menu 2 -> menambahkan Data Customer Baru
def add_customer():
    print("Menambahkan Customer Baru")
    Cust_ID = input("ID     : ").strip()
    Name    = input("Name   : ").strip()
    Email   = input("Email  : ").strip()
    Phone   = input("Phone  : ").strip()

    if Cust_ID and Name:
        customers.append({"ID": Cust_ID, "Name": Name, "Email": Email, "Phone": Phone})
        print("Data Customer Berhasil Ditambahkan.")
    else:
        print("ID Dan Name Tidak Boleh Kosong.")

# Masuk ke Menu 3 -> Memperbarui Data Customer
def update_customer():
    if not customers:
        print("Belum ada data.")
        return

    show_data()
    idx_str = input("\nMasukkan index yang akan diupdate: ").strip()
    if not idx_str.isdigit():
        print("Index harus angka.")
        return

    idx = int(idx_str)
    if not (0 <= idx < len(customers)):
        print("Index tidak valid.")
        return

    c = customers[idx]
    print("Kosongkan jika tidak ingin mengubah field.")
    Name  = input(f"Name  ({c['Name']}) : ").strip() or c['Name']
    Email = input(f"Email ({c['Email']}): ").strip() or c['Email']
    Phone = input(f"Phone ({c['Phone']}): ").strip() or c['Phone']

    customers[idx] = {"ID": c["ID"], "Name": Name, "Email": Email, "Phone": Phone}
    print("Data Customer Berhasil Diperbaharui.")

# Masuk ke Menu 4 -> Menghapus Data Customer
def delete_customer():
    if not customers:
        print("Data Customer Tidak Ada.")
        return

    show_data()
    idx_str = input("\nMasukkan index yang akan dihapus: ").strip()
    if not idx_str.isdigit():
        print("Index harus angka.")
        return

    idx = int(idx_str)
    if not (0 <= idx < len(customers)):
        print("Index tidak valid.")
        return

    removed = customers[idx]
    del customers[idx]
    print(f"Customer {removed['ID']} dihapus.")

# Masuk ke menu Looping
def main_menu():
    while True:
        show_menu()
        choose = input("Pilih menu 1 - 5: ").strip()
        if choose == "1":
            show_data()
        elif choose == "2":
            add_customer()
        elif choose == "3":
            update_customer()
        elif choose == "4":
            delete_customer()
        elif choose == "5":
            print("Berhasil Keluar Menu.")
            break
        else:
            print("Pilihan Tidak Valid.")
            
# Masuk ke menu login
LoginSuccess = False
# Count Percobaan Login
Login = 0
MaxLogin = 3

while Login < MaxLogin: # bikin looping untuk beberapa possibility dg IF jika percobaan masih di bawah 3. Pake While dulu karena biar tiap loop jalan, selalu diminta untuk masukin Uname & pass kalo tidak memenuhi salah satu kondisi.
    input_username = input("Username: ").strip() #using trim for eleminating xtra space
    input_password = input("Password: ").strip()

# Validasi Agar Usename & Password tidak kosong
    if input_username == "" or input_password == "":
        print("Input tidak boleh kosong. Coba lagi.\n") #kasih enter untuk print hasil sebelah + masukin uname
        Login += 1
        if Login >= MaxLogin:
            print("Gagal Login sudah 3 kali percobaan")
            break #keluar dari loop
        continue #masuk ke command setelahnya

# Validasi Agar Username Yang Dimasukkan Hanya Huruf
    if not input_username.isalpha():
        print("Username tidak valid! Harus huruf semua\n")
        Login += 1
        if Login >= MaxLogin:
            print("Gagal Login sudah 3 kali percobaan")
            break
        continue

# Validasi Agar Password Yang Dimasukkan Hanya Angka
    if not input_password.isdigit() or len(input_password) != 6:
        print("Password tidak valid! Harus angka semua dan 6 karakter\n")
        Login += 1
        if Login >= MaxLogin:
            print("Gagal Login sudah 3 kali percobaan")
            break #jika sudah 3x percobaan atau sukses login
        continue #balik ke loop input

# Kalo Login Berhasil
    if input_username == Username and input_password == Password:
        print("Login berhasil.\n")
        LoginSuccess = True
        break
    else:
        print("Username atau Password salah.")
        Login += 1
        if Login >= MaxLogin:
            print("Gagal login sudah 3 kali percobaan")
            break


# Jika login berhasil
if LoginSuccess:
    main_menu()
   