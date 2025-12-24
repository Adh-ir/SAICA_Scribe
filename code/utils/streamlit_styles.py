
SETUP_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

/* Force Streamlit to use the font */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

/* Glass Panel for Setup */
.setup-card {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.6);
    border-radius: 24px;
    padding: 2rem;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.gradient-bg {
    background: linear-gradient(135deg, #e0e7ff 0%, #f3e8ff 50%, #fce7f3 100%);
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
}

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Custom Button Styling */
.stButton button {
    width: 100%;
    background-color: #0f172a;
    color: white;
    padding: 1rem;
    border-radius: 0.75rem;
    font-weight: 700;
    font-size: 1.125rem;
    border: none;
    transition: all 0.3s ease;
}
.stButton button:hover {
    background-color: #000;
    transform: scale(1.02);
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
