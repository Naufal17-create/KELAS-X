<!-- (eps 20) -->

<form action="" method="post">
    <input type="text" name="kategori">
    <br>
    <input type="submit" name="simpan" value="simpan">
</form>

<?php
    require_once "../function.php";

    if (isset($_POST['simpan'])) {
        $kategori = $_POST['kategori'];

        $sql = "INSERT INTO tblkategori VALUES ('','$kategori') ";

        $result = mysqli_query($koneksi, $sql);

        header("location:http://localhost/Playlist%20PHP/Php%20SMK%20(eps%201-55)/restoran/kategori/select.php");
    }
?>