<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;

class OtpController extends Controller
{
    public function index()
    {
        return view('auth.verify-otp');
    }

    public function verify(Request $request)
    {
        $request->validate([
            'email' => 'required',
            'otp' => 'required'
        ]);

        $user = User::where('email', $request->email)
            ->where('otp', $request->otp)
            ->first();

        if (!$user) {
            return back()->with('error', 'OTP salah');
        }

        $user->email_verified_at = now();
        $user->otp = null;
        $user->save();

        return redirect('/login')->with('success', 'Email berhasil diverifikasi');
    }
}