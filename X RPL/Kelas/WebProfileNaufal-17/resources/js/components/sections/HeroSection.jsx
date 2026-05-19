import React from 'react';

// ==========================================
// SEKSI 1: HERO SECTION (SAMBUTAN UTAMA)
// ==========================================

const HeroSection = ({ scrollTo }) => {
    return (
        <section className="hero">
            
            {/* [SECTOR KIRI] Teks Sambutan dan Panggilan Aksi */}
            <div className="hero-content">
                
                {/* Badge Lokasi */}
                <div className="location-badge">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                        <circle cx="12" cy="10" r="3"></circle>
                    </svg>
                    Surabaya, Indonesia
                </div>
                
                {/* Judul Besar & Subtitle */}
                <h1 className="hero-title">Halo! Saya Naufal.</h1>
                <h2 className="hero-subtitle">Belajar Web Development &amp; Desain</h2>
                
                {/* Deskripsi Singkat */}
                <p className="hero-description">
                    Saya baru mulai belajar coding dan desain web sejak 9 bulan lalu. Saya suka membuat tampilan website yang simpel, rapi, dan estetis.
                </p>
                
                {/* Tombol Interaktif */}
                <a href="#projects" onClick={(e) => { e.preventDefault(); scrollTo('projects'); }} className="btn-primary">
                    Lihat Karya Saya
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                        <polyline points="12 5 19 12 12 19"></polyline>
                    </svg>
                </a>

            </div>

            {/* [SECTOR KANAN] Foto Profil Estetis dengan Bingkai Cahaya */}
            <div className="hero-photo">
                <div className="photo-frame">
                    <div className="photo-glow"></div> {/* Cahaya neon melingkar di belakang foto */}
                    <img src="/images/profile.jpg" alt="Naufal" />
                    <div className="photo-border"></div> {/* Garis putus-putus berputar */}
                </div>
            </div>

        </section>
    );
};

export default HeroSection;
