<?php

// ==========================================
// BACKEND CONTROLLER: RIWAYAT PENDIDIKAN
// ==========================================

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\JsonResponse;

class EducationController extends Controller
{
    /**
     * [PENGAMBILAN DATA] Mengembalikan data riwayat sekolah untuk Frontend React
     */
    public function index(): JsonResponse
    {
        // [DATA UTAMA] Daftar riwayat pendidikan dari SD sampai SMK
        $education = [
            [
                'id' => 1,
                'level' => 'SD',
                'school' => 'MINU KH Mukmin Sidoarjo',
                'year' => '2013 - 2019',
                'description' => 'Pendidikan dasar yang membentuk fondasi belajar dan karakter.',
                'icon' => 'book', // Ikon buku untuk SD
            ],
            [
                'id' => 2,
                'level' => 'SMP',
                'school' => 'MTsN 1 Sidoarjo',
                'year' => '2019 - 2022',
                'description' => 'Mendalami ilmu pengetahuan, ilmu agama dan mulai mengenali dunia teknologi.',
                'icon' => 'compass', // Ikon kompas untuk SMP
            ],
            [
                'id' => 3,
                'level' => 'SMK',
                'school' => 'SMKN 2 Buduran Sidoarjo',
                'year' => '2022 - Sekarang',
                'description' => 'Fokus di bidang kejuruan, mendalami skill teknis dan siap memasuki dunia kerja.',
                'icon' => 'code', // Ikon kode pemrograman untuk SMK
            ],
        ];

        // [KIRIM RESPON] Mengirim data sukses dan array pendidikan ke frontend
        return response()->json([
            'success' => true,
            'data' => $education,
        ]);
    }
}
