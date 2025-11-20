<?php 
    session_start();

    if (isset($_SESSION['email'])) {
        echo $_SESSION['email'];
        echo '<br>';
        echo "<a href='logout.php'>logout</a>";
    } else {
        echo "<h1>Register dulu ya!</h1>";
        echo '<br>';
        echo "<a href='index.php'>register</a>";
    }
?>