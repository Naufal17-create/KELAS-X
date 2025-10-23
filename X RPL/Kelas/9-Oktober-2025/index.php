
<h1>Saya Belajar Php</h1>
<?php
    
    $nama = "Maulana Naufal Fatihus Sururi";
    $kelas = "X-Rpl";
    $absen = 18;
    $hobi = "Bermain Badminton";
    $alamat = "Oma Pesona Buduran, Blok I1/17";
    $cita_cita = "Seorang Pengusaha/Guru";
    $enter = "<br>";

    /*
    echo $nama.$enter;
    echo $kelas.$enter;
    echo $absen.$enter;
    echo $hobi.$enter;
    echo $alamat.$enter;
    echo $cita_cita.$enter;
    */

    /*
    
    echo "<h1>Saya Belajar Php</h1>";
    echo "Saya Kelas: ";
    echo 10;

    echo "<h2>Maulana Naufal Fatihus Sururi</h2>";
    echo "<br>";
    echo "Kelas:X-Rpl";
    echo "<br>";
    echo "Absen: 18";
    echo "<br>";
    echo "Hobi: Bermain Badminton";
    echo "<br>";
    echo "Alamat: Oma Pesona Buduran, Blok I1/17";
    echo "<br>";
    echo "Cita-cita: Seorang Pengusaha/Guru";
    
    */

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Naufal</title>
</head>
<body>
    <h1>Identitas Diri</h1>
    <table>
        <tbody>
            <tr>
                <td>
                    Nama :
                </td>
                <td>
                    <?= $nama ?>
                </td>
            </tr>
            <tr>
                <td>
                    Kelas :
                </td>
                <td>
                    <?= $kelas ?>
                </td>
            </tr>
            <tr>
                <td>
                    Absen :
                </td>
                <td>
                    <?= $absen ?>
                </td>
            </tr>
            <tr>
                <td>
                    Hobi :
                </td>
                <td>
                    <?= $hobi ?>
                </td>
            </tr>
            <tr>
                <td>
                    Alamat :
                </td>
                <td>
                    <?= $alamat ?>
                </td>
            </tr>
            <tr>
                <td>
                    Cita-cita :
                </td>
                <td>
                    <?= $cita_cita ?>
                </td>
            </tr>
        </tbody>
    </table>
</body>
</html>