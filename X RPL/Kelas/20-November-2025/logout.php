<h1>anda sudah logout</h1>

<?php 
    session_start();
    session_destroy();
    // echo "<a href='login.php'>login</a>";
    header("Location: login.php");
?>