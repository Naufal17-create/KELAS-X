import React from 'react';

// ==========================================
// SEKSI 4: SKILL & KEAHLIAN (SKILLS)
// ==========================================

const SkillsSection = () => {
    return (
        <section id="skills" className="section reveal">
            
            {/* Kepala Bagian */}
            <div className="section-header">
                <h2 className="section-title">Skill & Keahlian</h2>
            </div>

            {/* Kisi Grid 2 Kolom */}
            <div className="grid-2">
                
                {/* [KATEGORI 1] Technical Skills (Keahlian Teknis / Coding) */}
                <div className="glass-panel">
                    <h3>Technical Skills</h3>
                    <div className="skill-category">
                        <h4>Web Development</h4>
                        {/* Kumpulan Tag Skill */}
                        <div className="skills-wrapper">
                            <span className="skill-tag">HTML</span>
                            <span className="skill-tag">CSS</span>
                            <span className="skill-tag">Dasar JavaScript</span>
                            <span className="skill-tag">React JS (Learning)</span>
                            <span className="skill-tag">Laravel (Learning)</span>
                        </div>
                    </div>
                </div>

                {/* [KATEGORI 2] Creative Skills (Keahlian Kreatif & Desain) */}
                <div className="glass-panel">
                    <h3>Creative Skills</h3>
                    <div className="skill-category">
                        <h4>Design & Content</h4>
                        {/* Kumpulan Tag Skill */}
                        <div className="skills-wrapper">
                            <span className="skill-tag">Canva Design</span>
                            <span className="skill-tag">UI/UX Basic</span>
                            <span className="skill-tag">Menulis Cerita Pendek</span>
                            <span className="skill-tag">Content Creation</span>
                        </div>
                    </div>
                </div>

            </div>
        </section>
    );
};

export default SkillsSection;
