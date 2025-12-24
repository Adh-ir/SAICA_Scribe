
SETUP_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@1,600&family=JetBrains+Mono:wght@400;500&display=swap');

/* Force Font globally */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Base Dark Theme for Setup */
.stApp {
    background-color: #02040a; /* Deepest blue-black */
    color: white;
}

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* --- RAYCAST-LIKE AURORA --- */
.aurora-container {
    position: fixed;
    top: -50%;
    left: 50%;
    transform: translateX(-50%);
    width: 250vw;
    height: 250vh;
    z-index: 0;
    pointer-events: none;
    background: 
        radial-gradient(circle at 60% 60%, rgba(56, 189, 248, 0.4), transparent 40%),
        conic-gradient(from 0deg at 50% 50%, rgba(14, 165, 233, 0.1), rgba(6, 182, 212, 0.3), rgba(37, 99, 235, 0.2), rgba(14, 165, 233, 0.1));
    filter: blur(60px);
    animation: rotateAurora 40s linear infinite;
    mix-blend-mode: screen;
}

.aurora-secondary {
    position: fixed;
    top: -30%;
    left: 40%;
    width: 200vw;
    height: 200vh;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.2), transparent 60%);
    filter: blur(80px);
    animation: pulseGlow 10s ease-in-out infinite alternate;
    mix-blend-mode: screen;
}

.beam {
    position: absolute;
    top: -20%;
    left: 50%;
    width: 150px;
    height: 150vh;
    background: linear-gradient(180deg, rgba(56, 189, 248, 0.6), transparent);
    filter: blur(50px);
    transform-origin: top center;
    animation: swingBeam 8s ease-in-out infinite alternate;
    mix-blend-mode: overlay;
}

.beam-2 {
    animation-duration: 12s;
    background: linear-gradient(180deg, rgba(168, 85, 247, 0.4), transparent); /* Subtle purple hint */
    height: 180vh;
    width: 200px;
    animation-delay: -5s;
}

@keyframes rotateAurora {
    from { transform: translateX(-50%) rotate(0deg); }
    to { transform: translateX(-50%) rotate(360deg); }
}

@keyframes swingBeam {
    from { transform: translateX(-50%) rotate(-25deg); }
    to { transform: translateX(-50%) rotate(25deg); }
}

@keyframes pulseGlow {
    0% { opacity: 0.3; transform: scale(1); }
    100% { opacity: 0.7; transform: scale(1.1); }
}

/* --- STARS --- */
.stars {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background-image: 
        radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 3px),
        radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 2px);
    background-size: 550px 550px, 350px 350px;
    background-position: 0 0, 40px 60px;
    opacity: 0.4;
    z-index: 0;
    animation: twinkle 5s infinite alternate;
}

@keyframes twinkle {
    0% { opacity: 0.3; }
    100% { opacity: 0.5; }
}

/* --- GLASS CARD (Applied to Streamlit Form) --- */
[data-testid="stForm"] {
    position: relative;
    z-index: 10;
    background: rgba(10, 10, 15, 0.75); /* Darker, more contrast */
    backdrop-filter: blur(40px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: 
        0 0 0 1px rgba(0,0,0,0.5),
        0 20px 40px -10px rgba(0,0,0,0.8),
        0 0 120px rgba(56, 189, 248, 0.25); /* Stronger blue glow */
    border-radius: 20px;
    padding: 3rem;
    animation: cardFloat 6s ease-in-out infinite alternate;
}

@keyframes cardFloat {
    0% { transform: translateY(0); }
    100% { transform: translateY(-10px); }
}

/* --- TEXT STYLES --- */
h1 {
    font-weight: 700;
}

/* Inputs */
.stTextInput input {
    background: rgba(0,0,0,0.4) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: white !important;
    border-radius: 12px !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.stTextInput input:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.15) !important;
}

/* Labels */
label {
    color: #94a3b8 !important;
    font-size: 0.8rem !important;
    text-transform: uppercase !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
}

/* Button */
.stButton button {
    background: white !important;
    color: black !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
    border: none !important;
    padding: 1rem !important;
    transition: all 0.2s !important;
}

.stButton button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 30px rgba(255, 255, 255, 0.3) !important;
}

</style>
"""

MAIN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@1,600&family=JetBrains+Mono:wght@400;500&display=swap');

/* Base Font */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #1e3a8a;
}

/* Fluid Background */
.fluid-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
    background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
}

.glass-card {
    background: rgba(255, 255, 255, 0.60);
    backdrop-filter: blur(30px);
    border: 3px solid #93c5fd;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 20px 40px -12px rgba(14, 165, 233, 0.1);
    border-radius: 20px;
    padding: 2rem;
}

/* Branding */
.logo-main {
    font-family: 'Inter', sans-serif;
    font-weight: 800;
    color: #003B5C;
    font-size: 2.5rem;
}

.logo-scribe {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-weight: 600;
    color: #005F88;
    font-size: 2.5rem;
}

/* Input Areas */
.stTextArea textarea {
    border: 1px solid #cbd5e1;
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 1rem;
    padding: 1.25rem;
}

.stTextArea textarea:focus {
    border-color: #38bdf8;
    box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.2);
}

/* Primary Button */
.stButton button {
    background: linear-gradient(to right, #0ea5e9, #2563eb);
    color: white;
    border: none;
    border-radius: 0.75rem;
    font-weight: 700;
    transition: transform 0.1s;
}
.stButton button:hover {
    transform: translateY(-2px);
}
</style>
"""
