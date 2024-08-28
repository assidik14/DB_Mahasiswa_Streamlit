import streamlit as st
from streamlit_option_menu import option_menu
from CRUD import Operations
import pandas as pd
import datetime as dt

main_menu = ["Create", "Read", "Update", "Delete"]

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # required
        options=main_menu,  # required
        icons=['pencil','book','recycle','eraser'],  # optional
        menu_icon="menu-down",  # optional
        default_index=0,  # optional
        )

# Homepage
if __name__ == "__main__":
    st.title("CRUD Database Mahasiswa")
    st.text("Menggunakan MySQL dan Streamlit Python")
    
    try:
        Operations.readData()
    except Exception:
        st.error("Database is not connected!!")

# Create
if selected == "Create":
    st.header("Create Data")

    nama = st.text_input("Nama")
    lahir = st.date_input("Tanggal Lahir", max_value=dt.date.today(), min_value=dt.date(1990, 1, 1))

    fakultas = st.selectbox(
        "Fakultas",
        ("FASILKOM", "FIKOM", "FD"),
        index=None,
        placeholder="Pilih Fakultas...",
    )
    st.write("You selected:", fakultas)

    if fakultas == "FASILKOM":
        jurusan = st.selectbox(
            "Jurusan",
            ("Teknik Informatika", "Sistem Informasi"),
            index=None,
            placeholder="Pilih Jurusan...",
        )
        st.write("You selected:", jurusan)
    elif fakultas == "FIKOM":
        jurusan = st.selectbox(
            "Jurusan",
            ("Broadcasting", "Jurnalistik", "Psikologi"),
            index=None,
            placeholder="Pilih Jurusan...",
        )
        st.write("You selected:", jurusan)
    elif fakultas == "FD":
        jurusan = st.selectbox(
            "Jurusan",
            ("Desain Grafis", "Desain Komunikasi Visual", "Desain Interior"),
            index=None,
            placeholder="Pilih Jurusan...",
        )
        st.write("You selected:", jurusan)

    create_btn = st.button("Create Data")

    if create_btn:
        try:
            Operations.createData(nama, lahir, fakultas, jurusan)
            st.success("Data berhasil ditambahkan")
        except Exception:
            st.error("Data gagal ditambahkan")


# Read
if selected == "Read":
    st.header("Read Data")
    
    try:
        data = Operations.readData()
        df = pd.DataFrame(data)
        st.dataframe(df.set_index(df.columns[0]))

    except Exception:
        st.error("Database error!!")

# Update
if selected == "Update":
    st.header("Update Data")

    nama = ""
    lahir = dt.date.today()
    fakultas = ""
    jurusan = ""
    data_fakultas = ("FASILKOM", "FIKOM", "FD")
    data_jurusan = ("Teknik Informatika", "Sistem Informasi", "Broadcasting", "Jurnalistik", "Psikologi", "Desain Grafis", "Desain Komunikasi Visual", "Desain Interior")
    data = Operations.rowData()
    id_status = 0

    id = st.text_input("Masukan ID Mahasiswa")

    if id == "":
        st.warning("ID Mahasiswa harus diisi!!")

    else :
        for all_id in data:
            if id == all_id[0]:
                id_status = 1
                break

        if id_status != 1:
            st.error("ID Mahasiswa tidak ditemukan!!")
        
        else:
            nama, lahir, fakultas, jurusan = Operations.searchData(id)

            nama_baru = st.text_input("Nama", nama)
            lahir_baru = st.date_input("Tanggal Lahir", max_value=dt.date.today(), min_value=dt.date(1990, 1, 1), value=lahir)

            if fakultas == "FASILKOM":
                fakultas_baru = st.selectbox("Fakultas",data_fakultas,index=0)
            elif fakultas == "FIKOM":
                fakultas_baru = st.selectbox("Fakultas",data_fakultas,index=1)
            elif fakultas == "FD":
                fakultas_baru = st.selectbox("Fakultas",data_fakultas,index=2)

            if jurusan == "Teknik Informatika":
                jurusan_baru = st.selectbox("Jurusan",data_jurusan,index=0)
            elif jurusan == "Sistem Informasi":
                jurusan_baru = st.selectbox("Jurusan",data_jurusan,index=1)
            elif jurusan == "Broadcasting":
                jurusan_baru = st.selectbox("Jurusan",data_jurusan,index=2)
            elif jurusan == "Jurnalistik":
                jurusan_baru = st.selectbox("Jurusan",data_jurusan,index=3)
            elif jurusan == "Psikologi":
                jurusan_baru = st.selectbox("Jurusan",data_jurusan,index=4)
            elif jurusan == "Desain Grafis":
                jurusan_baru = st.selectbox("Jurusan",data_jurusan,index=5)
            elif jurusan == "Desain Komunikasi Visual":
                jurusan_baru = st.selectbox("Jurusan",data_jurusan,index=6)
            elif jurusan == "Desain Interior":
                jurusan_baru = st.selectbox("Jurusan",data_jurusan,index=7)

            update_btn = st.button("Update Data")

            if update_btn:
                try:
                    Operations.updateData(id, nama_baru, lahir_baru, fakultas_baru, jurusan_baru)
                    st.success("Data Berhasil diupdate")
                except Exception:
                    st.error("Data Gagal diupdate")

if selected == "Delete":
    st.header("Delete Data")

    # nama = ""
    # lahir = dt.date.today()
    # fakultas = ""
    # jurusan = ""

    data_fakultas = ("FASILKOM", "FIKOM", "FD")
    data_jurusan = ("Teknik Informatika", "Sistem Informasi", "Broadcasting", "Jurnalistik", "Psikologi", "Desain Grafis", "Desain Komunikasi Visual", "Desain Interior")
    data = Operations.rowData()
    id_status = 0

    id = st.text_input("Masukan ID Mahasiswa")

    if id == "":
        st.warning("ID Mahasiswa harus diisi!!")

    else :
        for all_id in data:
            if id == all_id[0]:
                id_status = 1
                break

        if id_status != 1:
            st.error("ID Mahasiswa tidak ditemukan!!")
        
        else:
            st.text("Data ini akan dihapus")
            del_data = Operations.displayData(id)
            df = pd.DataFrame(del_data)
            st.dataframe(df.set_index(df.columns[0]))

            delete_btn = st.button("Delete Data")

            if delete_btn:
                try:
                    Operations.deleteData(id)
                    st.success("Data Berhasil dihapus")
                except Exception:
                    st.error("Data Gagal dihapus")
