<!-- (eps 21) -->

<?php
    require_once "../function.php";

    $sql = "DELETE FROM tblkategori WHERE idkategori = $id";
    
    $result = mysqli_query($koneksi, $sql);

    header("location:http://localhost/Playlist%20PHP/Php%20SMK%20(eps%201-55)/restoran/kategori/select.php");

?>