import React from 'react';

// ==========================================
// SEKSI 5: PROYEK KECIL (PORTFOLIO PROJECTS)
// ==========================================

const ProjectsSection = () => {
    return (
        <section id="projects" className="section reveal">
            
            {/* Kepala Bagian */}
            <div className="section-header">
                <h2 className="section-title">Proyek Kecil</h2>
            </div>

            {/* Grid 3 Kolom */}
            <div className="grid-3">
                
                {/* [PROYEK 1] Landing Page Profil Diri */}
                <div className="glass-panel project-card">
                    <div className="project-icon">
                        {/* Ikon Kertas Dokumen */}
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                    </div>
                    <h3 className="project-title">Landing Page Profil Diri</h3>
                    <p className="project-desc">Sebuah website portofolio simpel yang dibuat dari awal menggunakan HTML dan CSS murni untuk melatih pemahaman dasar layouting.</p>
                    {/* Tag Teknologi */}
                    <div className="project-tech"><span>#HTML</span><span>#CSS</span></div>
                </div>

                {/* [PROYEK 2] Desain Feed Instagram */}
                <div className="glass-panel project-card">
                    <div className="project-icon">
                        {/* Ikon Kamera */}
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                    </div>
                    <h3 className="project-title">Desain Feed Instagram</h3>
                    <p className="project-desc">Kumpulan desain visual estetis untuk feed Instagram teman, dibuat menggunakan Canva dengan fokus pada komposisi dan warna.</p>
                    {/* Tag Teknologi */}
                    <div className="project-tech"><span>#Canva</span><span>#Design</span></div>
                </div>

                {/* [PROYEK 3] Ocean Theme Profile (Situs Ini) */}
                <div className="glass-panel project-card">
                    <div className="project-icon">
                        {/* Ikon Tetesan Air */}
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"></path></svg>
                    </div>
                    <h3 className="project-title">Ocean Theme Profile</h3>
                    <p className="project-desc">Website profil modern ini! Dibangun dengan Laravel, React JS, dan tema desain Ocean dengan glassmorphism UI.</p>
                    {/* Tag Teknologi */}
                    <div className="project-tech"><span>#React</span><span>#Laravel</span></div>
                </div>

            </div>
        </section>
    );
};

export default ProjectsSection;
