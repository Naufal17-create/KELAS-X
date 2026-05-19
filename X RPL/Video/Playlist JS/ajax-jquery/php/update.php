<?php

require_once "koneksi.php";

$data = stripslashes(file_put_contents("php://input"));
$dataPelanggan = json_decode($data, true);


$idpelanggan = $dataPelanggan['idpelanggan'];
$pelanggan = $dataPelanggan['pelanggan'];
$alamat = $dataPelanggan['alamat'];
$telp = $dataPelanggan['telp'];

if (!empty($pelanggan) and !empty($alamat) and !empty($telp)) {
    
    $sql = "UPDATE tblpelanggan
    SET pelanggan = '$pelanggan',
    alamat = '$alamat'
    telp = '$telp'
    WHERE idpelanggan=$idpelanggan";

    if ($result = mysqli_query($con, $sql)) {
        echo "Data sudah diubah !";
    } else {
        echo "Data gagal diubah !";
    }
} else {
    echo "Data kosong";
}