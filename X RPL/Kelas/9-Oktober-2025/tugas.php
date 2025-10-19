<?php
$menu = ["Profil", "Program", "Berita", "Kontak"];
$nama_sekolah = "MTsN 1 Sidoarjo";
$tagline = "Santun dan Berprestasi";
$logo = "img/logoMTsN1sda.jpg"; 
$berita = "MTsN 1 Sidoarjo meraih Juara Umum Lomba Cerdas Cermat Islami Tingkat Kabupaten tahun 2025.";
$program = [
  "Tahfidzul Qur'an Terprogram",
  "Kelas Tahsin & Tilawah",
  "Pembinaan Olimpiade Sains Terpadu",
  "Kegiatan Pramuka & Ekstrakurikuler Wajib"
];
?>

<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title><?= $nama_sekolah ?></title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-success shadow-sm">
  <div class="container">
    <a class="navbar-brand fw-bold" href="#">
      <img src="<?= $logo ?>" alt="Logo" width="30" height="30" class="d-inline-block align-text-top me-2">
      <?= $nama_sekolah ?>
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    
    <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
      <ul class="navbar-nav">
        <?php foreach ($menu as $item): ?>
          <li class="nav-item">
            <a class="nav-link text-white" href="#"><?= $item ?></a>
          </li>
        <?php endforeach; ?>
      </ul>
    </div>
  </div>
</nav>

<!-- Hero Section -->
<section class="bg-light text-center py-5">
  <div class="container">
    <h1 class="display-5 fw-bold"><?= $nama_sekolah ?></h1>
    <p class="lead"><?= $tagline ?></p>
  </div>
</section>

<!-- Berita -->
<section class="container my-4">
  <h2 class="mb-3">Berita Terbaru</h2>
  <div class="alert alert-info" role="alert">
    <?= $berita ?>
  </div>
</section>

<!-- Program Unggulan -->
<section class="container mb-5">
  <h2 class="mb-4">Program Unggulan</h2>
  <div class="row">
    <?php foreach ($program as $prog): ?>
      <div class="col-md-6 mb-3">
        <div class="card shadow-sm">
          <div class="card-body">
            <h5 class="card-title"><?= $prog ?></h5>
            <p class="card-text">Program ini bertujuan untuk meningkatkan kompetensi dan karakter siswa secara holistik.</p>
          </div>
        </div>
      </div>
    <?php endforeach; ?>
  </div>
</section>

<!-- Footer -->
<footer class="bg-dark text-white text-center py-3">
  <p class="mb-0">&copy; <?= date("Y") ?> <?= $nama_sekolah ?> | All Rights Reserved.</p>
</footer>

<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
