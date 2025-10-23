<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentdiv</title>
    <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
    <script src="bootstrap/js/bootstrap.bundle.min.js" defer></script>
</head>
<body>
    <div class="container">

        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container-fluid">
            <a class="navbar-brand" href="?menu=Profile">Profile</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" 
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            
            <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="?menu=Sejarah">Sejarah</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" aria-current="page" href="?menu=Jurusan">Jurusan</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" aria-current="page" href="?menu=Prestasi">Prestasi</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" aria-current="page" href="?menu=Kegiatan">Kegiatan</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" aria-current="page" href="?menu=Kontak">Kontak</a>
                </li>               
            </ul>
            </div>
        </div>
        </nav>

    
        <!-- <nav class="mt-3">
            <ol>
                <li><a href="?menu=Profile">Profile</a></li>
                <li><a href="?menu=Sejarah">Sejarah</a></li>
                <li><a href="?menu=Jurusan">Jurusan</a></li>
                <li><a href="?menu=Prestasi">Prestasi</a></li>
                <li><a href="?menu=Kegiatan">Kegiatan</a></li>
                <li><a href="?menu=Kontak">Kontak</a></li>      
            </ol>
        </nav> -->

        <section class="mt-3">
            <!-- <form action="" method="GET"> 
                <input type="submit" name="kirim" value="click">
            </form> -->
            <?php
            if (isset($_GET['menu'])) {
                $isi = $_GET['menu'];
                // echo $isi;
                
                if ($isi == "Profile") {
                    require_once "pages/profile.php";
                }

                if ($isi == "Sejarah") {
                    require_once "pages/sejarah.php";
                }
                
                if ($isi == "Jurusan") {
                    require_once "pages/jurusan.php";
                }
                
                if ($isi == "Prestasi") {
                    require_once "pages/prestasi.php";
                }
                
                if ($isi == "Kegiatan") {
                    require_once "pages/kegiatan.php";
                }
                
                if ($isi == "Kontak") {
                    require_once "pages/kontak.php";
                }
            }else {
                require_once "pages/profile.php";
            }

            if (isset($_POST['tombol'])) {
                $nama = $_POST['nama'];
                $email = $_POST['email'];
                $pesan = $_POST['pesan'];

                echo "Nama : $nama <br>";
                echo "Email : $email <br>";
                echo "Pesan : $pesan <br>";
            }
            ?>
        </section>
        <footer class="bg-dark text-white text-center py-3 mt-5">
            <div class="container">
                <p class="mb-0">&copy; 2025 SMK Negeri 2 Buduran . All rights reserved.</p>
            </div>
        </footer>

    </div>
</body>
</html>
