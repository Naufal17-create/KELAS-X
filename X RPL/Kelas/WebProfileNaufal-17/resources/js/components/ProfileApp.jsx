import React, { useEffect, useState } from 'react';

// ==========================================
// ORCHESTRATOR UTAMA: INDUK APLIKASI (PROFILE APP)
// ==========================================

// [IMPORT 1] Layout Pendukung Website
import Navbar from './layout/Navbar';
import BackgroundEffects from './layout/BackgroundEffects';

// [IMPORT 2] Bagian Seksi Halaman Utama
import HeroSection from './sections/HeroSection';
import AboutSection from './sections/AboutSection';
import EducationSection from './sections/EducationSection';
import SkillsSection from './sections/SkillsSection';
import ProjectsSection from './sections/ProjectsSection';
import ContactFooter from './sections/ContactFooter';

const ProfileApp = () => {
    // [STATE 1] Status scroll navigasi (true jika scroll melebihi 80px)
    const [scrolled, setScrolled] = useState(false);
    
    // [STATE 2] Data riwayat sekolah (diambil dari Laravel API)
    const [education, setEducation] = useState([]);
    
    // [STATE 3] ID kartu pendidikan yang sedang disentuh mouse (hover)
    const [activeEdu, setActiveEdu] = useState(null);

    useEffect(() => {
        // [FUNGSI 1] Memantau scroll layar
        const handleScroll = () => {
            setScrolled(window.scrollY > 80);

            // Efek reveal konten melayang muncul saat di-scroll
            const reveals = document.querySelectorAll('.reveal');
            for (let i = 0; i < reveals.length; i++) {
                const windowHeight = window.innerHeight;
                const elementTop = reveals[i].getBoundingClientRect().top;
                const elementVisible = 100;
                
                if (elementTop < windowHeight - elementVisible) {
                    reveals[i].classList.add('active');
                }
            }
        };

        // [FUNGSI 2] Efek cahaya biru mengikuti gerakan kursor mouse
        const cursorGlow = document.getElementById('cursor-glow');
        const handleMouseMove = (e) => {
            if (cursorGlow) {
                cursorGlow.style.left = e.clientX + 'px';
                cursorGlow.style.top = e.clientY + 'px';
            }
        };

        // Pasang pendengar scroll & mouse
        window.addEventListener('scroll', handleScroll);
        window.addEventListener('mousemove', handleMouseMove);
        handleScroll();

        // [FUNGSI 3] Fetching: Mengambil data riwayat sekolah dari API Backend Laravel
        fetch('/api/education')
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    setEducation(data.data);
                }
            })
            .catch(err => console.error('Failed to fetch education:', err));
        
        // Hapus pendengar event saat komponen dihancurkan
        return () => {
            window.removeEventListener('scroll', handleScroll);
            window.removeEventListener('mousemove', handleMouseMove);
        };
    }, []);

    // [FUNGSI TAUTAN NAVIGASI] Scroll transisi halus ke element tujuan
    const scrollTo = (id) => {
        const element = document.getElementById(id);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
    };

    return (
        <>
            {/* 1. Komponen Latar Belakang (Gelembung, Ombak, Sinar Matahari) */}
            <BackgroundEffects />

            {/* 2. Menu Navigasi Sticky */}
            <Navbar scrolled={scrolled} scrollTo={scrollTo} />

            {/* 3. Kontainer Utama Seksi Halaman */}
            <div className="app-container">
                <main>
                    <HeroSection scrollTo={scrollTo} />
                    <AboutSection />
                    <EducationSection education={education} activeEdu={activeEdu} setActiveEdu={setActiveEdu} />
                    <SkillsSection />
                    <ProjectsSection />
                </main>
                
                {/* 4. Footer & Sosial Media */}
                <ContactFooter />
            </div>
        </>
    );
};

export default ProfileApp;
