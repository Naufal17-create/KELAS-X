<!-- (eps 13 [bagian 2]) -->

<nav>
    <ul>
        <li><a href="?menu=kontak">Kontak</a></li>
        <li><a href="?menu=sejarah">Sejarah</a></li>
        <li><a href="?menu=jurusan">Jurusan</a></li>
    </ul>
</nav>

<?php
    if (isset($_GET['menu'])){
        $menu = $_GET['menu'];
        require_once $menu.'.php';
    }
?>


<!-- (eps 11 [bagian 2]) -->

<!-- <nav>
    <ul>
        <li>Kontak</li>
        <li>Sejarah</li>
        <li>Jurusan</li>
    </ul>
</nav> -->