import React from 'react';

// ==========================================
// SEKSI 3: RIWAYAT PENDIDIKAN (TIMELINE)
// ==========================================

const EducationSection = ({ education, activeEdu, setActiveEdu }) => {
    return (
        <section id="education" className="section reveal">
            
            {/* Kepala Bagian */}
            <div className="section-header">
                <h2 className="section-title">Riwayat Pendidikan</h2>
            </div>

            {/* Kontainer Garis Waktu */}
            <div className="edu-timeline">
                
                {/* [LOOPING DATA] Memetakan array sekolah dari API Backend */}
                {education.map((edu, index) => (
                    <div
                        key={edu.id}
                        // Kelas aktif menyala jika sedang disentuh mouse (hover)
                        className={`edu-card ${activeEdu === edu.id ? 'edu-card-active' : ''}`}
                        onMouseEnter={() => setActiveEdu(edu.id)}
                        onMouseLeave={() => setActiveEdu(null)}
                        style={{ animationDelay: `${index * 0.2}s` }} // Animasi memantul beruntun
                    >
                        
                        {/* [KONEKTOR KIRI] Bagian Garis dan Titik Hubung Timeline */}
                        <div className="edu-connector">
                            <div className="edu-dot">
                                <div className="edu-dot-inner"></div>
                            </div>
                            {/* Garis vertikal menyambung antar kartu (kecuali kartu terakhir) */}
                            {index < education.length - 1 && <div className="edu-line"></div>}
                        </div>

                        {/* [KARTU UTAMA] Berisi Detail Sekolah */}
                        <div className="edu-content glass-panel">
                            
                            {/* [SEKTOR IKON] Ikon Dinamis Berdasarkan Tag Database */}
                            <div className="edu-icon">
                                {/* Ikon SD (Buku) */}
                                {edu.icon === 'book' && (
                                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                                        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                                    </svg>
                                )}
                                {/* Ikon SMP (Kompas) */}
                                {edu.icon === 'compass' && (
                                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                        <circle cx="12" cy="12" r="10"></circle>
                                        <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon>
                                    </svg>
                                )}
                                {/* Ikon SMK (Kode pemrograman) */}
                                {edu.icon === 'code' && (
                                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                        <polyline points="16 18 22 12 16 6"></polyline>
                                        <polyline points="8 6 2 12 8 18"></polyline>
                                    </svg>
                                )}
                            </div>

                            {/* [SEKTOR TEKS] Nama Sekolah, Jenjang, Tahun, dan Deskripsi */}
                            <div className="edu-info">
                                <span className="edu-level">{edu.level}</span>
                                <h3 className="edu-school">{edu.school}</h3>
                                <span className="edu-year">{edu.year}</span>
                                <p className="edu-desc">{edu.description}</p>
                            </div>

                        </div>

                    </div>
                ))}

            </div>
        </section>
    );
};

export default EducationSection;
