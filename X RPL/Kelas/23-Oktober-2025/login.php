<h1>Login</h1>

<form action="" method="post">
    <input type="email" name="email" placeholder="Masukkan Email" required> <br>
    <input type="password" name="password" placeholder="Masukkan Password"> <br>
    <input type="submit" value="login" name="login">
</form>

<?php
if (isset($_POST['login'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];

    if ($email == "kaa@gmail.com" && $password == "090809") {
        $_SESSION['email'] = $email;
        header("Location: index.php");
    } else {
        echo "EMAIL ATAU PASSWORD SALAH";
    }
}
?>