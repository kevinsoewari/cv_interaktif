import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Curriculum Vitae- Kevin Alifviansyah", layout="centered")
    
    # Sidebar
    with st.sidebar:
        st.image("pas_kevin.jpg", width=200)
        st.write("### Kontak")
        st.write("📧 Email: kevinalifviansyah@gmail.com")
        st.write("📞 Telepon: +62 81214282172")
        st.write("🌍 LinkedIn: linkedin.com/kevinalifviansyah")
        st.write("📊 GitHub: github.com/kevinsoewari")
        
    # Header
    st.title("Curriculum Vitae")
    st.header("Kevin Alifviansyah - Data Analyst")
    st.write("Seorang Data Analyst yang memiliki dasar yang kuat dalam statistik, dengan pengalaman akademik dan profesional dalam analisis data.")
    
    # Tentang Saya
    st.subheader("Tentang Saya")
    st.write(
        "Seorang analis data yang bersemangat dan berwawasan luas dengan dasar yang kuat dalam statistik, diasah melalui proyek akademik. Lulus dengan gelar Sarjana Matematika dari Universitas Negeri Surabaya dan saat ini sedang duduk di semester akhir program Magister Statistika dan Data Science di IPB University. Memiliki semangat untuk penyelesaian masalah dengan pendekatan statistik pada data kompleks menjadi wawasan yang dapat ditindaklanjuti dan mengoptimalkan proses untuk mendorong solusi inovatif. Dilengkapi dengan keahlian canggih dalam metode statistik dan analisis data, dan berkomitmen untuk memecahkan masalah yang kompleks dan mendukung pengambilan keputusan berbasis data."
    )
    
    # Keahlian
    st.subheader("Keahlian")
    skills = ["Python", "R","Excel", "SQL", "SAS", "Tableau", "Machine Learning", "Data Visualization", "Data Mining", "Natural Language Process"]
    st.write(", ".join(skills))
    
    # Pengalaman Kerja
    st.subheader("Pengalaman Kerja")
    st.write("**Assistant Lecturer - IPB University** (Jan 2024 - Jul 2024)")
    st.write("- Mengajarkan dasar-dasar SAS dan Pengantar Pemrograman R.")
    st.write("- Berhasil menyampaikan 14+ kuliah interaktif yang berfokus pada analisis statistik dan dasar-dasar pemrograman, dengan tingkat kepuasan siswa rata-rata 90% berdasarkan umpan balik akhir semester.")
    st.write("- Membimbing 50 mahasiswa sarjana dalam proyek langsung, membimbing mereka melalui analisis data dunia nyata menggunakan R, yang meningkatkan kemahiran teknis dan keterampilan berpikir kritis pada tugas akhir kursus")


    st.write("**Staff Data Analysis Project - Dokter Data IPB** (Mar 2024 - Aug 2024)")
    st.write("- Mengembangkan laporan strategis untuk program alumni 2024-2025.")
    st.write("- Berkolaborasi dengan tim lintas fungsi untuk mengidentifikasi metrik keterlibatan alumni utama, berkontribusi pada laporan strategis yang secara resmi diadopsi untuk program penjangkauan alumni 2024-2025")
    st.write("- Melakukan pembersihan dan prapemrosesan data yang komprehensif, memastikan integritas data 100% untuk lebih dari 5.000 catatan alumni, yang secara signifikan mengurangi kesalahan pelaporan.")


    st.write("**Project Leader - Dokter Data IPB** (Apr 2023 - Jun 2023)")
    st.write("- Melakukan analisis survival left-censored menggunakan Tobit Regression untuk HIV/AIDS.")
    st.write("- Berhasil mengidentifikasi variabel signifikan yang memengaruhi tingkat kelangsungan hidup individu dengan HIV/AIDS, meningkatkan akurasi model sebesar 15%.")
    st.write("- Menerapkan validasi lintas model untuk memastikan kekokohan hasil, meningkatkan keandalan model prediktif. Berkontribusi pada penyusunan laporan analisis yang digunakan sebagai dasar pengambilan keputusan.")

    # Pendidikan
    st.subheader("Pendidikan")
    st.write("**Institut Pertanian Bogor** (S2 Statistik dan Data Science, 2023 - Sekarang)")
    st.write("**Universitas Negeri Surabaya** (S1 Matematika, 2018 - 2022, IPK: 3.40/4.00)")
 
    

    st.subheader("Portofolio")
    projects = {
        "Visualisasi Data Scraping IBL": {
            "desc": "Menggunakan R, mengumpulkan data dari situs resmi Liga Basket Indonesia (IBL) untuk mengumpulkan data terkait statistik pemain, hasil pertandingan, dan kinerja tim. Setelah data berhasil diekstraksi, saya membersihkan dan menganalisis data untuk mengidentifikasi pola kinerja, tren kemenangan pada 3 tim teratas dalam klasemen serta kontribusi pemain kunci di setiap pertandingan. Hasil analisis ini kemudian divisualisasikan menggunakan berbagai teknik grafik interaktif untuk memberikan wawasan yang lebih dalam terkait dinamika kompetisi IBL.",
            "link": "https://shorturl.at/BDqG8"
        },
        "Multi-kelas Klasifikasi dengan Ulasan Starbucks": {
            "desc": "Menggunakan R, mengumpulkan data dari situs resmi Liga Basket Indonesia (IBL) untuk mengumpulkan data terkait statistik pemain, hasil pertandingan, dan kinerja tim. Setelah data berhasil diekstraksi, saya membersihkan dan menganalisis data untuk mengidentifikasi pola kinerja, tren kemenangan pada 3 tim teratas dalam klasemen serta kontribusi pemain kunci di setiap pertandingan. Hasil analisis ini kemudian divisualisasikan menggunakan berbagai teknik grafik interaktif untuk memberikan wawasan yang lebih dalam terkait dinamika kompetisi IBL.",
            "link": "https://shorturl.at/TFvhj"
        }
    }
    for title, info in projects.items():
        with st.expander(title):
            st.write(info["desc"])
            st.markdown(f"[Lihat Proyek]({info['link']})")

    # Unduh CV

    st.subheader("Unduh CV")
    with open("Kevin Alifviansyah-ats-r.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button("Unduh CV", data=pdf_bytes, file_name="Kevin Alifviansyah_CV.pdf", mime="application/pdf")

if __name__ == "__main__":
    main()
