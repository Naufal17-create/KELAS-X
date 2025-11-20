<?php 
    class Calculator {
        function penjumlahan() {
            echo "penjumlahan";
            echo "<br>";
        }
        function pengurangan() {
            echo "pengurangan";
            echo "<br>";
        }
        function perkalian() {
            echo "perkalian";
            echo "<br>";
        }
        function pembagian() {
            echo "pembagian";
            echo "<br>";
        }

    }

    $kalkulator = new Calculator();
    $kalkulator->penjumlahan(); 
    $kalkulator->perkalian();
?>