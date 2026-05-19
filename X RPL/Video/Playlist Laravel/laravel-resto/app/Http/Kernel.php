<?php

namespace App\Http;

use Illuminate\Foundation\Http\Kernel as HttpKernel;

class Kernel extends HttpKernel
{
    /** 
        The application's global HTTP middlewere stack.

        These middlewere are run during every request to your application.

        @var array<int, class-string|string>
    */
    protected $middleware = [
        // \App\Http\Middlewere\TrustHosts::class,
        // \App\Http\Middleware\TrustProxies::class,
        // \Illuminate\Http\Middleware\HandleCors::class,
        // \App\Http\Middleware\PreventRequestsDuringMaintenance::class,
        // \Illuminate\Foundation\Http\Middleware\ValidatePostSize::class,
        // \App\Http\Middleware\TrimStrings::class,
        // \Illuminate\Foundation\Http\Middleware\ConvertEmptySrtingsToNull::class,
    ];

    protected $routeMiddleware = [
        'CekLogin' => \App\Http\Middleware\CekLogin::class
    ];
}

?>