import streamlit as st
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
import datetime

# --- 1. CONFIG & SECRETS ---
API_KEY = "AIzaSyCYpxVSiwIwPmkt0Wi_Wc33C6FqG7VKJTc"
genai.configure(api_key=API_KEY)

# --- 2. NYT STYLE CUSTOM CSS (Arayüzü kusursuzlaştıran kısım) ---
st.set_page_config(page_title="DeutschInsider", page_icon="🇩🇪", layout="wide")

st.markdown("""
    <style>
    /* Google Fonts Entegrasyonu */
    @import url('https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@300;400;700&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');
    
    /* Genel Arkaplan ve Fontlar */
    html, body, [class*="css"] { 
        font-family: 'Libre Franklin', sans-serif; 
        color: #121212;
        background-color: #ffffff;
    }
    
    /* GEREKSİZ STREAMLIT ELEMENTLERİNİ GİZLEME (GitHub, Rerun, Footer vb.) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* New York Times Header Stili */
    .nyt-header {
        text-align: center;
        border-bottom: 2px solid #121212;
        margin-bottom: 10px;
        padding-bottom: 10px;
    }
    .nyt-logo {
        font-family: 'Playfair Display', serif;
        font-size: 65px;
        font-weight: 700;
        letter-spacing: -2px;
        color: #000;
        margin-bottom: 0px;
    }
    .nyt-sub {
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 400;
        margin-top: -10px;
    }
    
    /* Yazı Boyutlarını Büyütme */
    h1, h2, h3 { font-family: 'Playfair Display', serif; }
    p, li { font-size: 20px !important; line-height: 1.6; color: #333; }
    
    /* Rapor Kartı ve Premium Kilit */
    .report-container {
        max-width: 850px;
        margin: auto;
        padding: 20px;
    }
    .premium-overlay {
        background: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,1) 80%);
        padding: 60px;
        text-align: center;
        border-top: 1px solid #eee;
        margin-top: -150px;
        position: relative;
    }
    
    /* Şık Buton */
    .stButton>button {
        background-color: #000;
        color: #fff;
        border: 1px solid #000;
        padding: 12px 40px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER (NYT LOGO & DATE) ---
current_date = datetime.date.today().strftime("%A, %B %d, %Y")
st.markdown(f"""
    <div class='nyt-header'>
        <div class='nyt-logo'>DeutschInsider</div>
        <div class='nyt-sub'>STRATEGIC CAREER INTELLIGENCE FOR PROFESSIONALS</div>
        <div style='font-size: 13px; margin-top: 10px; border-top: 1px solid #eee; padding-top: 5px;'>
            {current_date.upper()} | LATEST MARKET UPDATES
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 4. ANA İÇERİK (MANŞET) ---
st.markdown("<div class='report-container'>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["LATEST REPORT", "THE ARCHIVE", "MEMBERSHIP"])

with tab1:
    st.markdown("## 2026 Salary Benchmarks: The Quiet Shift in German IT Hubs")
    st.markdown("*Analysis by DI Strategic Unit*")
    
    # Rapor Metni
    st.write("""
    As the new fiscal quarter begins, the German Ministry of Labor has quietly adjusted the threshold for high-demand 
    professional sectors. While public focus remains on general immigration numbers, the real movement is happening 
    within the 'Opportunity Card' (Chancenkarte) selection criteria, where linguistic versatility is now weighted 
    more heavily than pure academic credentials.
    """)

    # --- PROFESYONEL LİNK VE PAYWALL ---
    st.markdown("""
        <div style='height: 150px; background: linear-gradient(transparent, white);'></div>
        <div class='premium-overlay'>
            <h3 style='font-size: 26px; font-family: "Playfair Display", serif;'>Unlock the Full Intelligence Report</h3>
            <p style='font-size: 18px !important; color: #666;'>
                To continue reading this analysis and access our 2026 salary database, 
                <a href='#membership-tab' style='color: #000; font-weight: 700; text-decoration: underline;'>become a Professional Member</a>.
            </p>
            <div style='margin-top: 20px;'>
                <a href='https://iyzi.link/SİZİN_IYZICO_LİNKİNİZ' target='_blank' 
                   style='background-color: #000; color: #fff; padding: 12px 35px; text-decoration: none; font-weight: 700; font-size: 14px; letter-spacing: 1px; display: inline-block;'>
                   SUBSCRIBE NOW — $19/MO
                </a>
            </div>
            <p style='font-size: 13px !important; margin-top: 15px; color: #999;'>
                Already a member? <a href='#' style='color: #666;'>Sign in here.</a>
            </p>
        </div>
    """, unsafe_allow_html=True)
with tab2:
    st.markdown("### The Intelligence Archive")
    st.write("Browse previous strategic reports and deep-dives.")
    st.info("Archive access is limited to Professional members.")

with tab3:
    st.markdown("### Professional Membership")
    st.write("Get daily market signals and legal navigation directly to your dashboard.")
    st.write("**$19 / month**")

st.markdown("</div>", unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("""
    <div style='text-align: center; padding: 50px; border-top: 1px solid #eee; margin-top: 50px; font-size: 12px; color: #999;'>
        © 2026 DEUTSCHINSIDER STRATEGIC INTELLIGENCE. ALL RIGHTS RESERVED.<br>
        <a href='#' style='color: #999;'>Terms of Service</a> | <a href='#' style='color: #999;'>Privacy Policy</a>
    </div>
    """, unsafe_allow_html=True)


