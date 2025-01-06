import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Konfigurasi koneksi MySQL
config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'keberlangsungan_studi'
}

def create_connection():
    return mysql.connector.connect(**config)

# Endpoint untuk menambahkan mahasiswa
@app.route('/mahasiswa', methods=['POST'])
def add_mahasiswa():
    data = request.json
    nama = data.get('nama')
    nim = data.get('nim')

    if not nama or not nim:
        return jsonify({'error': 'Nama dan NIM harus diisi'}), 400

    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO mahasiswa (nama, nim) VALUES (%s, %s)", (nama, nim))
        conn.commit()
        return jsonify({'message': 'Mahasiswa berhasil ditambahkan'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint untuk menambahkan mata kuliah
@app.route('/mata_kuliah', methods=['POST'])
def add_mata_kuliah():
    data = request.json
    kode_mk = data.get('kode_mk')
    nama_mk = data.get('nama_mk')

    if not kode_mk or not nama_mk:
        return jsonify({'error': 'Kode dan Nama Mata Kuliah harus diisi'}), 400

    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO mata_kuliah (kode_mk, nama_mk) VALUES (%s, %s)", (kode_mk, nama_mk))
        conn.commit()
        return jsonify({'message': 'Mata Kuliah berhasil ditambahkan'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint untuk menambahkan riwayat studi
@app.route('/riwayat', methods=['POST'])
def add_riwayat():
    data = request.json
    nim = data.get('nim')
    kode_mk = data.get('kode_mk')
    nilai = data.get('nilai')

    if not nim or not kode_mk or not nilai:
        return jsonify({'error': 'NIM, Kode Mata Kuliah, dan Nilai harus diisi'}), 400

    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO riwayat (nim, kode_mk, nilai) VALUES (%s, %s, %s)", (nim, kode_mk, nilai))
        conn.commit()
        return jsonify({'message': 'Riwayat Studi berhasil ditambahkan'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint untuk menambahkan dosen
@app.route('/dosen', methods=['POST'])
def add_dosen():
    data = request.json
    nidn = data.get('nidn')
    nama = data.get('nama')

    if not nidn or not nama:
        return jsonify({'error': 'NIDN dan Nama Dosen harus diisi'}), 400

    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO dosen (nidn, nama) VALUES (%s, %s)", (nidn, nama))
        conn.commit()
        return jsonify({'message': 'Dosen berhasil ditambahkan'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
