<?php 
    $host = "localhost";
    $user = "root";
    $pass = "";
    $db   = "dbsekolah";
    $koneksi = mysqli_connect($host, $user, $pass, $db);
    $sql = "SELECT * FROM tblsiswa";
    $query = mysqli_query($koneksi, $sql);
    $siswa = mysqli_fetch_array($query);
    var_dump($siswa);
    echo "<br>";
    echo $siswa[1];
?>