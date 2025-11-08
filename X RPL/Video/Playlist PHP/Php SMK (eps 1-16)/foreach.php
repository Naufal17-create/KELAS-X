<!-- (eps 10) -->

<?php
    // $nama = array('tejo','budi','siti', 100);
    // var_dump($nama);
    // echo '<br>';

    // foreach ($nama as $key){
    //     echo $key.'<br>';
    // }

    $nama = array(
        "tejo" => "surabaya",
        "budi" => "malang",
        "siti" => "sidoarjo"
    );

    var_dump($nama);
    echo '<br>';
    foreach ($nama as $a => $b){
        echo $a.'-'.$b;
        echo '<br>';
    }
?>