<!-- (eps 15) -->

<?php
    $cookie_name = 'user';
    $cookie_value = 'joni';

    setcookie($cookie_name, $cookie_value);

    $cookie_value = 'tejo';

    setcookie($cookie_name, $cookie_value);

    echo isset($_COOKIE[$cookie_name]) ? $_COOKIE[$cookie_name] : 'Cookie belum diset';
    // echo $_COOKIE[$cookie_name];

    setcookie("user", "", time() - 3600);

    echo '<br>';

    var_dump($_COOKIE);
?>