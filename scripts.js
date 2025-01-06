document.addEventListener("DOMContentLoaded", () => {
    // Menangani formulir Mahasiswa
    const formMahasiswa = document.getElementById("formMahasiswa");
    const listMahasiswa = document.getElementById("listMahasiswa");

    formMahasiswa.addEventListener("submit", (e) => {
        e.preventDefault();
        const nama = document.getElementById("nama").value;
        const nim = document.getElementById("nim").value;

        if (nama && nim) {
            const mahasiswaItem = document.createElement("div");
            mahasiswaItem.textContent = `Nama: ${nama}, NIM: ${nim}`;
            listMahasiswa.appendChild(mahasiswaItem);

            formMahasiswa.reset();
        }
    });

    // Menangani formulir Mata Kuliah
    const formMataKuliah = document.getElementById("formMataKuliah");
    const listMataKuliah = document.getElementById("listMataKuliah");

    formMataKuliah.addEventListener("submit", (e) => {
        e.preventDefault();
        const kodeMk = document.getElementById("kode_mk").value;
        const namaMk = document.getElementById("nama_mk").value;

        if (kodeMk && namaMk) {
            const mkItem = document.createElement("div");
            mkItem.textContent = `Kode: ${kodeMk}, Nama: ${namaMk}`;
            listMataKuliah.appendChild(mkItem);

            formMataKuliah.reset();
        }
    });

    // Menangani formulir Riwayat Studi
    const formRiwayat = document.getElementById("formRiwayat");
    const listRiwayat = document.getElementById("listRiwayat");

    formRiwayat.addEventListener("submit", (e) => {
        e.preventDefault();
        const nimRiwayat = document.getElementById("nim_riwayat").value;
        const kodeMkRiwayat = document.getElementById("kode_mk_riwayat").value;
        const nilai = document.getElementById("nilai").value;

        if (nimRiwayat && kodeMkRiwayat && nilai) {
            const riwayatItem = document.createElement("div");
            riwayatItem.textContent = `NIM: ${nimRiwayat}, Kode MK: ${kodeMkRiwayat}, Nilai: ${nilai}`;
            listRiwayat.appendChild(riwayatItem);

            formRiwayat.reset();
        }
    });

    // Menangani formulir Dosen
    const formDosen = document.getElementById("formDosen");
    const listDosen = document.getElementById("listDosen");

    formDosen.addEventListener("submit", (e) => {
        e.preventDefault();
        const nidn = document.getElementById("nidn").value;
        const namaDosen = document.getElementById("nama_dosen").value;

        if (nidn && namaDosen) {
            const dosenItem = document.createElement("div");
            dosenItem.textContent = `NIDN: ${nidn}, Nama: ${namaDosen}`;
            listDosen.appendChild(dosenItem);

            formDosen.reset();
        }
    });
});
