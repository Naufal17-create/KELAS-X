import React from 'react';

// ==========================================
// SEKSI 2: TENTANG SAYA (ABOUT ME)
// ==========================================

const AboutSection = () => {
    return (
        <section id="about" className="section reveal">
            
            {/* Kepala Bagian */}
            <div className="section-header">
                <h2 className="section-title">Tentang Saya</h2>
            </div>

            {/* Kotak Konten Bermotif Kaca (Glassmorphism) */}
            <div className="glass-panel">
                
                {/* [METADATA] Baris Informasi Tempat & Tanggal Lahir */}
                <div className="about-meta">
                    {/* Tempat Lahir */}
                    <div className="about-meta-item">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                            <circle cx="12" cy="10" r="3"></circle>
                        </svg>
                        <span>Lahir di <strong>Surabaya</strong></span>
                    </div>
                    {/* Tanggal Lahir */}
                    <div className="about-meta-item">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="16" y1="2" x2="16" y2="6"></line>
                            <line x1="8" y1="2" x2="8" y2="6"></line>
                            <line x1="3" y1="10" x2="21" y2="10"></line>
                        </svg>
                        <span><strong>10 Agustus 2009</strong></span>
                    </div>
                </div>

                {/* [BIOGRAFI PARAGRAF] */}
                <div style={{ fontSize: '1.2rem', lineHeight: '1.8', color: 'var(--text-main)', display: 'flex', flexDirection: 'column', gap: '1.2rem' }}>
                    
                    {/* Paragraf 1: Perkenalan Diri */}
                    <p>
                        Selamat datang di profil saya! Nama saya <strong>Maulana Naufal Fatihus Sururi</strong>, 
                        lahir di Surabaya pada tanggal 10 Agustus 2009. 
                        Saya sangat antusias dengan dunia teknologi, khususnya pengembangan web dan desain.
                    </p>
                    
                    {/* Paragraf 2: Perjalanan Belajar Coding */}
                    <p>
                        Dalam perjalanan 9 bulan terakhir ini, saya banyak menghabiskan waktu mempelajari dasar-dasar 
                        bagaimana sebuah website dibuat agar tidak hanya berfungsi dengan baik, tetapi juga terlihat indah.
                    </p>
                    
                    {/* Paragraf 3: Kreativitas Lainnya */}
                    <p>
                        Selain coding, saya juga gemar menulis cerita pendek yang membantu saya mengembangkan 
                        kreativitas dan imajinasi yang kemudian saya tuangkan ke dalam desain saya.
                    </p>

                </div>

            </div>
        </section>
    );
};

export default AboutSection;
