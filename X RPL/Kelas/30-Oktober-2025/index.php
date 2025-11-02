<form action="" method="post">
    Tanggal:
    <input type="number" name="tanggal" placeholder="Maukkan Tanggal"> <br>
    Bulan:
    <input type="number" name="bulan" placeholder="Masukkan Bulan"> <br>

    <input type="submit" name="kirim" value="Zodiak anda ...">
</form>

<form action="" method="post">
    a:
    <input type="number" name="a" placeholder="Bilangan a"> <br>
    b:
    <input type="number" name="b" placeholder="Bilangan b"> <br>

    <input type="submit" name="hitung" value="jumlahkan">
    <input type="submit" name="hitung" value="kurangi">
    <input type="submit" name="hitung" value="kalikan">
    <input type="submit" name="hitung" value="bagikan">
</form>

<?php
    if (isset($_POST['hitung'])) {
        $hitung = $_POST['hitung'];
        $a = $_POST['a'];
        $b = $_POST['b'];

        if ($hitung == 'jumlahkan') {
            echo "Penjumlahan dari $a + $b adalah: <br>";
            echo $a + $b;
        }
        if ($hitung == 'kurangi') {
            echo "Pengurangan dari $a - $b adalah: <br>";
            echo $a - $b;
        }
        if ($hitung == 'kalikan') {
            echo "Perkalian dari $a * $b adalah: <br>";
            echo $a * $b;
        }
        if ($hitung == 'bagikan') {
            echo "Pemagian dari $a / $b adalah: <br>";
            echo $a / $b;
        }

    }

    if (isset($_POST['kirim'])) {
        $tanggal = $_POST['tanggal'];
        $bulan = $_POST['bulan'];

        Zodiak($bulan, $tanggal);
    }

    
    function belajar() {
        echo "Hari ini, saya belajar function";
    }

    function cekTanggal($tanggal) {
        if ($tanggal > 0 && $tanggal < 32) {
            // echo "tanggal benar !";
        } else {
            //  echo "tanggal salah !";
            return false;
        }
    }

    // >> Memanggil function <<
    // cekTanggal(1);
    // cekTanggal(0);
    // cekTanggal(100);

    // $tanggal = 22;
    // $bulan = 6;


    function zodiak($bulan, $tanggal) {
        if ($tanggal > 0 && $tanggal < 32 && $bulan > 0 && $bulan < 13) {
            // echo "= = = = = = = = = = = = = = = = = = = = = =<br>";
            if ($bulan == 1) {
                if ($tanggal > 0 && $tanggal < 20) {
                    echo "Zodiak anda: Capicorn";
                } else {
                    echo "Zodiak anda: Aquarius";
                }
            }
            
            if ($bulan == 2) {
                if ($tanggal > 0 && $tanggal < 20) {
                    echo "Zodiak anda: Aquarius";
                } else if ($tanggal > 28) {
                    echo "Bulan Februari tidak memiliki tanggal $tanggal !";
                }
                else {
                    echo "Zodiak anda: Pisces";
                }
            }
            
            if ($bulan == 3) {
                if ($tanggal > 0 && $tanggal < 21) {
                    echo "Zodiak anda: Pisces";
                } else {
                    echo "Zodiak anda: Aries";
                }
            }
            
            if ($bulan == 4) {
                if ($tanggal > 0 && $tanggal < 20) {
                    echo "Zodiak anda: Aries";
                } else {
                    echo "Zodiak anda: Taurus";
                }
            }
            
            if ($bulan == 5) {
                if ($tanggal > 0 && $tanggal < 21) {
                    echo "Zodiak anda: Taurus";
                } else {
                    echo "Zodiak anda: Gemini";
                }
            }
            
            if ($bulan == 6) {
                if ($tanggal > 0 && $tanggal < 21) {
                    echo "Zodiak anda: Gemini";
                } else {
                    echo "Zodiak anda: Cancer";
                }
            }
            
            if ($bulan == 7) {
                if ($tanggal > 0 && $tanggal < 23) {
                    echo "Zodiak anda: Cancer";
                } else {
                    echo "Zodiak anda: Leo";
                }
            }
            
            if ($bulan == 8) {
                if ($tanggal > 0 && $tanggal < 23) {
                    echo "Zodiak anda: Leo";
                } else {
                    echo "Zodiak anda: Virgo";
                }
            }
            
            if ($bulan == 9) {
                if ($tanggal > 0 && $tanggal < 23) {
                    echo "Zodiak anda: Virgo";
                } else {
                    echo "Zodiak anda: Libra";
                }
            }
            
            if ($bulan == 10) {
                if ($tanggal > 0 && $tanggal < 23) {
                    echo "Zodiak anda: Libra";
                } else {
                    echo "Zodiak anda: Scorpio";
                }
            }
            
            if ($bulan == 11) {
                if ($tanggal > 0 && $tanggal < 22) {
                    echo "Zodiak anda: Scorpio";
                } else {
                    echo "Zodiak anda: Sagittarius";
                }
            }
            
            if ($bulan == 12) {
                if ($tanggal > 0 && $tanggal < 22) {
                    echo "Zodiak anda: Sagittarius";
                } else {
                    echo "Zodiak anda: Capicorn";
                }
            }
            // echo "<br>= = = = = = = = = = = = = = = = = = = = = =";
        } else {
            echo "tanggal atau bulan salah !";
        }
    }

    // zodiak(100, 1);
    // zodiak(12, 30);
    // zodiak(5, 20);

    function cekBulan($bulan) {
        if ($bulan > 0 && $bulan < 13) {
            return true;
        } else {
            return false;
        }
    }

    $p = 55;
    $I = 33;
    $t = 155;

    // echo "Volume balok dengan panjang $p, lebar $I, dan tinggi $t adalah: <br>";

    // echo luasPersegiPanjang($p, $I) * $t;

    function tambah($a, $b) {
        return $a = $b;
    }

    function kurang($a, $b) {
        return $a - $b;
    }

    function kali($a, $b) {
        return $a * $b;
    }

    function bagi($a, $b) {
        return $a / $b;
    }

    $a = 15;
    $b = 5;

    // echo 'penjumlahan dari'. $a . 'dan' . $b . 'adalah:' . tambah($a, $b) . '<br>';
    // echo 'penjumlahan dari'. $a . 'dan' . $b . 'adalah:' . tambah($a, $b) . '<br>';
    // echo 'penjumlahan dari'. $a . 'dan' . $b . 'adalah:' . tambah($a, $b) . '<br>';
    // echo 'penjumlahan dari'. $a . 'dan' . $b . 'adalah:' . tambah($a, $b) . '<br>';
?>