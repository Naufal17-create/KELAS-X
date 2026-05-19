import React from 'react';

// ==========================================
// LAYOUT: EFEK LATAR BELAKANG TEMA LAUT
// ==========================================

const BackgroundEffects = () => {
    return (
        <>
            {/* [EFEK 1] Gelembung Air yang Melayang Naik */}
            <ul className="bg-bubbles">
                <li></li><li></li><li></li><li></li><li></li>
                <li></li><li></li><li></li><li></li><li></li>
            </ul>

            {/* [EFEK 2] Cipratan Air Rintik */}
            <div className="water-splashes">
                <span className="droplet"></span>
                <span className="droplet"></span>
                <span className="droplet"></span>
                <span className="droplet"></span>
                <span className="droplet"></span>
                <span className="droplet"></span>
                <span className="droplet"></span>
                <span className="droplet"></span>
            </div>

            {/* [EFEK 3] Riak Air Melingkar */}
            <div className="water-ripples">
                <div className="ripple"></div>
                <div className="ripple"></div>
                <div className="ripple"></div>
                <div className="ripple"></div>
                <div className="ripple"></div>
            </div>

            {/* [EFEK 4] Partikel Air Kecil yang Hanyut */}
            <div className="water-particles">
                <span></span><span></span><span></span><span></span><span></span>
                <span></span><span></span><span></span><span></span><span></span>
                <span></span><span></span><span></span><span></span><span></span>
            </div>

            {/* [EFEK 5] Sorot Cahaya Matahari Menembus Air (God Rays) */}
            <div className="god-rays">
                <div className="ray"></div>
                <div className="ray"></div>
                <div className="ray"></div>
                <div className="ray"></div>
                <div className="ray"></div>
            </div>

            {/* [EFEK 6] Ubur-ubur Buatan yang Mengapung Lambat */}
            <div className="jellyfish-container">
                {/* Ubur-ubur 1 */}
                <div className="jellyfish jf-1">
                    <div className="jf-head"></div>
                    <div className="jf-tentacles">
                        <span></span><span></span><span></span><span></span>
                    </div>
                </div>
                {/* Ubur-ubur 2 */}
                <div className="jellyfish jf-2">
                    <div className="jf-head"></div>
                    <div className="jf-tentacles">
                        <span></span><span></span><span></span><span></span>
                    </div>
                </div>
                {/* Ubur-ubur 3 */}
                <div className="jellyfish jf-3">
                    <div className="jf-head"></div>
                    <div className="jf-tentacles">
                        <span></span><span></span><span></span>
                    </div>
                </div>
            </div>

            {/* [EFEK 7] Ombak Laut Bergerak di Paling Bawah Layar */}
            <div className="ocean-waves">
                <svg className="wave wave-1" viewBox="0 0 1440 100" preserveAspectRatio="none">
                    <path d="M0,40 C360,100 1080,0 1440,60 L1440,100 L0,100 Z" />
                </svg>
                <svg className="wave wave-2" viewBox="0 0 1440 100" preserveAspectRatio="none">
                    <path d="M0,60 C320,10 720,90 1440,30 L1440,100 L0,100 Z" />
                </svg>
            </div>

            {/* [EFEK 8] Sinar Glow yang Mengikuti Gerak Kursor Mouse */}
            <div id="cursor-glow" className="cursor-glow"></div>
        </>
    );
};

export default BackgroundEffects;
