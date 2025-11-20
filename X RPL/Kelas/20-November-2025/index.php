<form action="" method="POST">
    Email : <input type="email" name="email" required placeholder="masukkan email"><br>
    Password : <input type="password" name="password" required placeholder="masukkan password"><br>
    <input type="submit" name="login" value="login">
</form>

<?php 
    session_start();

    if (isset($_POST['login'])) {
        $email = $_POST['email'];
        $password = $_POST['password'];
        $_SESSION['email'] = $email;
        header("Location: login.php");
        

        echo "email : " . $email . "<br>";
        echo "password : " . $password . "<br>";
    }

    $isi = "Halo Dunia";
    $hasil = isset($isi);
    echo $hasil;

    if (isset($isi)) {
        echo "Variabel sudah di isi";
    } else {
        echo "Variabel belum di isi";
    }
    
    var_dump($isi);

?>