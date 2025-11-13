<form action="" method="POST">
    <label for="nis">NIS :</label>
    <input type="number" name="nis" id="nis" required placeholder="Masukkan NIS"><br>

    <label for="nama">Nama :</label>
    <input type="text" name="nama" id="nama" required placeholder="Masukkan Nama"><br>
    
    <label for="alamat">Alamat :</label>
    <input type="text" name="alamat" id="alamat" placeholder="Masukkan Alamat"><br>
    
    <label for="telp">Telepon :</label>
    <input type="text" name="telp" id="telp" placeholder="Masukkan Telepon"><br>
    
    <input type="submit" name="simpan" value="simpan">
</form>

<?php 
    $db = 'dbsekolah';
    $host = 'localhost';
    $user = 'root';
    $password = '';

    $koneksi = mysqli_connect($host, $user, $password, $db);

    if (isset($_POST['simpan'])) {
        $nis = $_POST['nis'];
        $nama = $_POST['nama'];
        $alamat = $_POST['alamat'];
        $telp = $_POST['telp'];

        // echo $nis, "-" , $nama, "-", $alamat, "-", $telp;

        $sql = "INSERT INTO tblsiswa (nis, nama, alamat, telp) VALUES ($nis, '$nama', '$alamat', '$telp')";
        echo $sql;
        $query = mysqli_query($koneksi, $sql);

        
    }

        $sql = "SELECT * FROM tblsiswa";
        $query = mysqli_query($koneksi, $sql);

        
            ?>

            <table border="2px">
                <thead>
                    <tr>
                        <th>NIS</th>
                        <th>Nama</th>
                        <th>Alamat</th>
                        <th>Telepon</th>
                    </tr>
                </thead>
                <tbody>

            <!-- (while) -->
            <?php 
                while ($siswa = mysqli_fetch_array($query)) {
            ?>
                    <tr>
                        <td><?php echo $siswa['nis']; ?></td>
                        <td><?php echo $siswa['nama']; ?></td>
                        <td><?php echo $siswa['alamat']; ?></td>
                        <td><?php echo $siswa['telp']; ?></td>
                    </tr>
                

            <?php
            // echo $siswa['nis'] , " - " , $siswa['nama'] , " - " , $siswa['alamat'] , " - " , $siswa['telp'];
            // echo "<br>";
        } ?>
                </tbody>
            </table>
<?php ?>