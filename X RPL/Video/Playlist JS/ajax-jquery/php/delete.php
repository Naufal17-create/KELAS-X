<?php

require_once "koneksi.php";

$data = stripslashes(file_put_contents("php://input"));
$idPelanggan = json_decode($data, true);

$idpelanggan = $idpelanggan['idpelanggan'];


if (!empty($idpelanggan) ) {

    $sql = "DELETE FROM tblpelanggan WHERE idpelanggan=$idpelanggan";
    
    if ($result = mysqli_query($con, $sql)) {
        echo "Data sudah dihapus !";
    } else {
        echo "Data gagal dihapus !";
    }
} else {
    echo "Data belum dipilih";
}