import React from 'react';

// ==========================================
// LAYOUT: MENU NAVIGASI (NAVBAR)
// ==========================================

const Navbar = ({ scrolled, scrollTo }) => {
    return (
        // [NAVBAR UTAMA] Kelas 'scrolled' akan ditambahkan jika user men-scroll ke bawah > 80px
        <header className={`navbar${scrolled ? ' scrolled' : ''}`}>
            <div className="navbar-inner">
                
                {/* [LOGO] Di sebelah kiri, klik untuk scroll kembali ke paling atas */}
                <a href="#" onClick={(e) => { e.preventDefault(); window.scrollTo({ top: 0, behavior: 'smooth' }); }} className="navbar-logo">Naufal.</a>
                
                {/* [MENU LINK] Navigasi cepat untuk berpindah bagian halaman */}
                <nav>
                    <a href="#about" onClick={(e) => { e.preventDefault(); scrollTo('about'); }} className="nav-link">Tentang</a>
                    <a href="#education" onClick={(e) => { e.preventDefault(); scrollTo('education'); }} className="nav-link">Pendidikan</a>
                    <a href="#skills" onClick={(e) => { e.preventDefault(); scrollTo('skills'); }} className="nav-link">Skill</a>
                    <a href="#projects" onClick={(e) => { e.preventDefault(); scrollTo('projects'); }} className="nav-link">Proyek</a>
                    <a href="#contact" onClick={(e) => { e.preventDefault(); scrollTo('contact'); }} className="nav-link">Kontak</a>
                </nav>

            </div>
        </header>
    );
};

export default Navbar;
