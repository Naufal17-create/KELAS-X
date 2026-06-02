<x-guest-layout>
    <div class="mb-4 text-sm text-gray-600">
        {{ __('Masukkan kode OTP yang telah dikirimkan ke email Anda.') }}
    </div>

    <!-- Session Status -->
    <x-auth-session-status class="mb-4" :status="session('status')" />

    <form method="POST" action="/verify-otp">
        @csrf

        <!-- Email Address -->
        <div>
            <x-input-label for="email" :value="__('Email')" />
            <x-text-input id="email" class="block mt-1 w-full" type="email" name="email" :value="old('email')" required autofocus />
            <x-input-error :messages="$errors->get('email')" class="mt-2" />
        </div>

        <!-- OTP Code -->
        <div class="mt-4">
            <x-input-label for="otp" :value="__('Kode OTP')" />
            <x-text-input id="otp" class="block mt-1 w-full" type="text" name="otp" required />
            <x-input-error :messages="$errors->get('otp')" class="mt-2" />
        </div>

        <div class="flex items-center justify-end mt-4">
            <x-primary-button>
                {{ __('Kirim') }}
            </x-primary-button>
        </div>
    </form>
</x-guest-layout>