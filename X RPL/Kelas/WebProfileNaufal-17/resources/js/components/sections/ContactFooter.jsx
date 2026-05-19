import React from 'react';

// ==========================================
// SEKSI 6: KONTAK & HAK CIPTA (FOOTER)
// ==========================================

const ContactFooter = () => {
    return (
        <footer id="contact" className="reveal">
            
            {/* Judul Bagian */}
            <h2 className="section-title" style={{ fontSize: '2rem', marginBottom: '2rem' }}>Mari Terhubung</h2>
            
            {/* [SOSIAL MEDIA LINKS] Kumpulan Tombol Jejaring Sosial */}
            <div className="social-links">
                {/* 1. Email */}
                <a href="mailto:naufalsururi10@gmail.com" className="social-btn" title="Email">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                </a>
                
                {/* 2. Instagram */}
                <a href="https://instagram.com/maulanuuu_1" target="_blank" rel="noopener noreferrer" className="social-btn" title="Instagram">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                </a>
                
                {/* 3. TikTok */}
                <a href="https://tiktok.com/@nauu_106" target="_blank" rel="noopener noreferrer" className="social-btn" title="TikTok">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5"></path></svg>
                </a>
                
                {/* 4. GitHub */}
                <a href="https://github.com/Naufal17-create" target="_blank" rel="noopener noreferrer" className="social-btn" title="GitHub">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                </a>
            </div>

            {/* [HAK CIPTA] Informasi Nama & Tahun Dinamis */}
            <p className="footer-text">
                © {new Date().getFullYear()} Maulana Naufal Fatihus Sururi. Dibuat dengan 🩵 dan tema lautan.
            </p>

        </footer>
    );
};

export default ContactFooter;
