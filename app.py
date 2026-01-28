import streamlit as st
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
import datetime

# --- CONFIG ---
API_KEY = "AIzaSyCYpxVSiwIwPmkt0Wi_Wc33C6FqG7VKJTc"
genai.configure(api_key=API_KEY)

# --- 1. OTONOM VERİ TOPLAMA SİSTEMİ ---
def get_autonomous_intel():
    # Google News ve Sektörel RSS'lerden en sıcak 3 gelişme
    url = "https://news.google.com/rss/search?q=Germany+work+visa+news&hl=en-US&gl=US&ceid=US:en"
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features="xml")
        titles = [item.title.text for item in soup.findAll('item')[:3]]
        return " | ".join(titles)
    except:
        return "Mavi Kart güncellemeleri ve konut piyasası trendleri."

# --- 2. TASARIM ---
st.set_page_config(page_title="DeutschInsider", page_icon="🇩🇪", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=Playfair+Display:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .logo-box { background: #000; color: #fff; padding: 5px 15px; font-family: 'Playfair Display', serif; font-size: 30px; font-weight: 700; }
    .brand-container { display: flex; align-items: center; gap: 15px; border-bottom: 2px solid #000; padding-bottom: 15px; margin-bottom: 30px; }
    .premium-lock { background: linear-gradient(180deg, rgba(255,255,255,0) 0%, #f9f9f9 100%); padding: 60px; text-align: center; border: 1px dashed #ccc; margin-top: -100px; }
    .footer { font-size: 11px; color: #888; text-align: center; margin-top: 100px; padding: 40px; border-top: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

# HEADER
st.markdown("<div class='brand-container'><div class='logo-box'>DI</div><div style='font-size: 24px; letter-spacing: 4px;'>DEUTSCHINSIDER</div></div>", unsafe_allow_html=True)

tabs = st.tabs(["📊 GÜNLÜK ANALİZ", "📁 ARŞİV", "💎 ÜYELİK", "⚖️ YASAL"])

with tabs[0]:
    intel = get_autonomous_intel()
    st.write(f"**Son Güncelleme:** {datetime.date.today().strftime('%d.%m.%Y')} | **Sinyaller:** {intel}")
    st.markdown("## Stratejik İstihbarat Raporu #2026-112")
    st.write("""
    Almanya'da nitelikli göçmenlik yasasında yapılan son revizyonlar, özellikle IT ve mühendislik alanındaki 
    yabancı profesyoneller için vize bekleme sürelerini eyalet bazlı olarak %30 oranında azaltmayı hedefliyor. 
    Ancak, Berlin ve Münih'teki konut kayıt (Anmeldung) krizleri, bu süreci operasyonel olarak zorlaştırıyor.
    
    Profesyonel ekibimizin yaptığı analizlere göre, bu ay öne çıkan 3 kritik risk faktörü şunlardır:
    1. Eyalet bazlı vergi avantajlarının değişimi.
    2. Sigorta primlerindeki yeni kesinti oranları.
    """)
    
    st.markdown("""
        <div style='height: 100px;'></div>
        <div class='premium-lock'>
            <h3>🔒 Analizin Devamı ve Aksiyon Planı Kilitli</h3>
            <p>2026 maaş pazarlığı stratejileri ve yasal koruma rehberine erişmek için Premium üyeliğe geçin.</p>
            <br>
        </div>
    """, unsafe_allow_html=True)
    st.button("TÜM RAPORLARI AÇ (199 TL / AY)")

# --- 3. HUKUKİ METİNLER (Footers) ---
with tabs[3]:
    st.markdown("### Yasal Bilgilendirmeler")
    with st.expander("Mesafeli Satış Sözleşmesi"):
        st.write("""
        **1. TARAFLAR:** İşbu sözleşme DeutschInsider (SATICI) ile hizmetten faydalanan (ALICI) arasındadır.
        **2. KONU:** Dijital içerik ve stratejik analiz bülten aboneliği hizmetidir.
        **3. İPTAL:** 6502 sayılı Kanun gereği dijital ortamda anında ifa edilen hizmetlerde cayma hakkı bulunmamaktadır.
        """)
    with st.expander("Gizlilik ve Veri Politikası"):
        st.write("Kişisel verileriniz KVKK kapsamında sadece hizmet sunumu ve ödeme doğrulama amacıyla işlenmektedir.")

st.markdown("<div class='footer'>© 2026 DeutschInsider | iyzico Güvenli Ödeme Altyapısı | <a href='#'>Destek</a></div>", unsafe_allow_html=True)