<!-- (eps 5) -->

<?php
    // OPERATOR MATEMATIKA
    $a = 7;
    $b = 2;

    $c = $a + $b;
    echo "Penjumlahan: $c<br>";

    $c = $a - $b;
    echo "Pengurangan: $c<br>";

    $c = $a * $b;
    echo "Perkalian: $c<br>";

    $c = $a / $b;
    echo "Pembagian (dibulatkan ke bawah): " . floor($c) . "<br>";

    $c = $a % $b;
    echo "Sisa bagi: $c<br><br>";

    // OPERATOR LOGIKA
    echo 'a < b : '.($a < $b ? 'true' : 'false').'<br>';
    echo 'a > b : '.($a > $b ? 'true' : 'false').'<br>';
    echo 'a == b : '.($a == $b ? 'true' : 'false').'<br>';
    echo 'a != b : '.($a != $b ? 'true' : 'false').'<br><br>';

    // INCREMENT
    $a++;
    echo "Nilai a setelah increment: $a<br><br>";

    // OPERATOR STRING
    $kata = 'Sura';
    $kota = 'Baya';

    $hasil = $kata . $kota . ' ';
    $hasil .= 'KOTA PAHLAWAN';

    echo "Hasil string: $hasil";
?>
