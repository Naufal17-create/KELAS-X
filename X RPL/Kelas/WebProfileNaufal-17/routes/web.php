<?php

// ==========================================
// KUMPULAN RUTE BACKEND APLIKASI (ROUTES)
// ==========================================

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Api\EducationController;

// [RUTE 1] Halaman Utama: Merender tampilan website profil utama (welcome.blade.php)
Route::get('/', function () {
    return view('welcome');
});

// [RUTE 2] API Pendidikan: Mengirim data riwayat sekolah (SD, SMP, SMK) dalam format JSON
Route::get('/api/education', [EducationController::class, 'index']);
