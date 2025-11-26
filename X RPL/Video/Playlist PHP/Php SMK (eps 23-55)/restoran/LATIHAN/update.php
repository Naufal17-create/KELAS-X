<!-- (eps 22) -->

<?php 
    $id = $_GET['id'];

    require_once "../function.php";

    $sql = "SELECT * FROM tblkategori WHERE idkategori = $id";
    $result = mysqli_query($koneksi, $sql);

    $row = mysqli_fetch_assoc($result);

    // $kategori = '';
    // $id = 21;
    // $sql = "UPDATE tblkategori SET kategori='$kategori' WHERE idkategori= $id ";
    
    // $result = mysqli_query($koneksi, $sql);
    
    // echo $sql;
?>

<form action="" method="post">
    kategori :
    <input type="text" name="kategori" value="<?php echo $row['kategori'] ?>">
    <br>
    <input type="submit" name="simpan" value="simpan">
</form>

<?php 
    if (isset($_POST['simpan'])) {
        $kategori = $_POST['kategori'];
        $sql = "UPDATE tblkategori SET kategori='$kategori' WHERE idkategori= $id ";

        $result = mysqli_query($koneksi, $sql);

        header("location:http://localhost/Playlist%20PHP/Php%20SMK%20(eps%201-55)/restoran/kategori/select.php");
    }
?>