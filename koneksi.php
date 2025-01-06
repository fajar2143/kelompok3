<?php
// Konfigurasi database
$host = 'localhost'; // Host database
$dbname = 'nama_database'; // Nama database
$username = 'root'; // Username database
$password = ''; // Password database

// Koneksi ke database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Koneksi gagal: " . $e->getMessage());
}

// Proses data dari form
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nama = $_POST['nama'] ?? '';
    $nim = $_POST['nim'] ?? '';

    if (!empty($nama) && !empty($nim)) {
        try {
            // Query untuk menyimpan data ke database
            $query = "INSERT INTO mahasiswa (nama, nim) VALUES (:nama, :nim)";
            $stmt = $pdo->prepare($query);

            // Bind parameter dan eksekusi query
            $stmt->bindParam(':nama', $nama);
            $stmt->bindParam(':nim', $nim);
            $stmt->execute();

            echo "Data mahasiswa berhasil disimpan.";
        } catch (PDOException $e) {
            echo "Error: " . $e->getMessage();
        }
    } else {
        echo "Harap isi semua field.";
    }
}
?>
