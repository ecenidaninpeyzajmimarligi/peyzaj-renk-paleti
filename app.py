import streamlit as st
from colour import Color
import colorsys
import math

# 1. BİTKİ VERİ TABANI (Tüm bitkileriniz entegre edilmiştir)
BITKI_KUTUPHANESI = {
    "Acacia cyaneophylla (A. saligna)": "#5E7F6B", "Acer negundo": "#6FA66A", 
    "Acer negundo 'Variegatum'": "#A7CFA3", "Acer negundo 'Aureavariegatum'": "#D8E68A", 
    "Ailanthus altissima": "#5FA350", "Albizia julibrissin": "#8DBB7A", 
    "Alnus glutinosa": "#2F5A34", "Araucaria heterophylla": "#3D5F52", 
    "Bauhinia variegata": "#6FAF62", "Brachychiton populneus": "#7E9A7A", 
    "Caesalpinia gilliesii": "#9EB59C", "Casuarina equisetifolia": "#6D8F82", 
    "Catalpa bignonioides": "#A5CF5E", "Cedrus libani": "#4F7470", 
    "Celtis australis": "#4E7A43", "Ceratonia siliqua": "#5D7A4A", 
    "Cercis siliquastrum": "#7BA86A", "Chamaerops humilis": "#6D8C5A", 
    "Chorisia speciosa (Ceiba speciosa)": "#78A46C", "Cinnamomum camphora": "#5F8A55", 
    "Citrus aurantium": "#6EA857", "Cryptomeria japonica": "#3E5F46", 
    "Cupressus arizonica": "#5F7F77", "Cupressus macrocarpa": "#5E7F78", 
    "Cupressus sempervirens var. horizontalis": "#55786F", 
    "Cupressus sempervirens var. pyramidalis": "#4D6E67", 
    "× Cuprocyparis leylandii (Leylandi)": "#5C7D72", "Cycas revoluta": "#3F6A3A", 
    "Dalbergia sissoo": "#6FA066", "Elaeagnus angustifolia": "#A7B89A", 
    "Eriobotrya japonica": "#587A45", "Erythrina lysistemon": "#6A8E58", 
    "Erythrina crista-galli": "#6C8C59", "Eucalyptus camaldulensis": "#7E998A", 
    "Ficus australis (F. rubiginosa)": "#4F6F45", "Ficus benjamina": "#4A7442", 
    "Ficus elastica": "#2E4C34", "Ficus nitida (F. microcarpa ‘Nitida’)": "#4B7241", 
    "Firmiana simplex": "#78A564", "Fraxinus excelsior": "#5E8A54", 
    "Fraxinus ornus": "#6C9A62", "Ginkgo biloba": "#A8C654", 
    "Grevillea robusta": "#6E8F63", "Jacaranda mimosifolia": "#7FA96A", 
    "Koelreuteria paniculata": "#8DB05C", "Leucaena leucocephala": "#7FAF68", 
    "Liquidambar orientalis": "#4E6E45", "Liriodendron tulipifera": "#6FAF62", 
    "Livistona australis": "#4F6F4A", "Livistona chinensis": "#567A52", 
    "Magnolia grandiflora": "#4A6A3F", "Malus floribunda": "#6FA868", 
    "Melia azedarach": "#7BAF66", "Morus alba": "#6F9F5A", 
    "Morus alba f. pendula": "#6C9C58", "Morus kagayamae (Morus bombycis)": "#6A9554", 
    "Olea europaea": "#8A9B6D", "Parkinsonia aculeata": "#90B473", 
    "Paulownia tomentosa": "#80A86B", "Phoenix canariensis": "#4E6D45", 
    "Phoenix dactylifera": "#4A6942", "Phoenix theophrasti": "#486741", 
    "Phoenix roebelenii": "#3F5F3A", "Phytolacca dioica": "#6C8E57", 
    "Pinus brutia": "#3D5E48", "Pinus pinea": "#3F624A", 
    "Platanus orientalis": "#6F9A5E", "Populus alba": "#A1B79A", 
    "Populus nigra": "#5F8A54", "Prunus cerasifera ‘Nigra’": "#4A5A40", 
    "Robinia pseudoacacia": "#6D9C59", "Robinia pseudoacacia ‘Umbraculifera’": "#76A463", 
    "Salix babylonica": "#7FAF6A", "Salix caprea ‘Pendula’": "#789F64", 
    "Schinus molle": "#6E9A62", "Sophora japonica": "#6FA665", 
    "Syagrus romanzoffiana": "#4E6F45", "Taxodium distichum": "#567A55", 
    "Thuja orientalis (Platycladus orientalis)": "#5D7F6A", 
    "Viburnum lucidum (V. tinus var.)": "#4F6C45", "Washingtonia filifera": "#5B7A52", 
    "Washingtonia robusta": "#5F7F55", "Ficus carica": "#6F8D54", 
    "Lagunaria patersonia": "#7B9C67", "Prunus persica ‘Versicolor’": "#7AA566", 
    "Abelia × grandiflora": "#6E8F58", "Agave americana": "#6E8A72", 
    "Aloe arborescens": "#6F8F65", "Berberis thunbergii": "#7B8E55", 
    "Berberis thunbergii var. atropurpurea": "#5A4A52", "Brugmansia × candida": "#799C6A", 
    "Buxus sempervirens": "#4F6A3F", "Callistemon citrinus": "#6F9C60", 
    "Callistemon viminalis": "#6C9A5D", "Cassia artemisioides": "#A3B88A", 
    "Cestrum elegans": "#6C8F58", "Cestrum nocturnum": "#6A8E54", 
    "Chaenomeles japonica": "#759A62", "Cortaderia selloana": "#A7B89A", 
    "Cotoneaster franchetii": "#7C9B78", "Cotoneaster horizontalis": "#6F8A62", 
    "Duranta repens": "#6FA867", "Dodonaea viscosa ‘Purpurea’": "#5A3E4A", 
    "Dracaena indivisa ‘Purpurea’": "#4B2F38", "Eugenia myrtifolia": "#4F6D44", 
    "Euonymus fortunei": "#89A875", "Euonymus japonicus": "#6F8F62", 
    "Euphorbia pulcherrima (Atatürk çiçeği)": "#7A8F64", 
    "Euphorbia tirucalli": "#A7C27A", "Forsythia × intermedia": "#8DAF6A", 
    "Hibiscus mutabilis": "#7AA565", "Hibiscus rosa-sinensis": "#6D9C59", 
    "Hibiscus syriacus": "#789F62", "Grevillea juniperina": "#5A7A55", 
    "Grevillea rosmarinifolia": "#4F6D4A", "Juniperus horizontalis": "#5A7F78", 
    "Lantana camara": "#7F9A60", "Laurus nobilis": "#4F6F45", 
    "Ligustrum japonicum": "#4E6A3F", "Ligustrum japonicum ‘Texanum’": "#506C41", 
    "Ligustrum ovalifolium": "#5B7A48", "Mahonia fortunei": "#4D6A3E", 
    "Malvaviscus penduliflorus": "#6F8C58", "Metrosideros excelsa": "#5D7A52", 
    "Myrtus communis": "#4A6A3F", "Nandina domestica": "#6F8754", 
    "Nerium oleander": "#6C8F58", "Photinia × fraseri": "#5A7A48", 
    "Phormium tenax": "#4F5A3F", "Pittosporum tobira": "#4E6D45", 
    "Pittosporum tobira ‘Nana’": "#4F6E46", "Plumeria alba": "#6FAF6C", 
    "Polygala myrtifolia": "#6F8C5A", "Punica granatum": "#6A8A50", 
    "Pyracantha coccinea": "#6D8F55", "Ricinus communis": "#597A48", 
    "Rosmarinus officinalis": "#5A7F72", "Russelia equisetiformis": "#6E8F64", 
    "Sambucus nigra": "#4F6A42", "Sambucus nigra ‘Purpurea’": "#4A3A45", 
    "Solanum rantonnetii (Lycianthes rantonnetii)": "#6F8A58", 
    "Spiraea × vanhouttei": "#6FA76A", "Strelitzia reginae": "#6C8F5A", 
    "Syringa vulgaris": "#7BA86A", "Tamarix tetrandra": "#A7B8A2", 
    "Teucrium fruticans": "#7C9A8A", "Thevetia peruviana": "#6D8A54", 
    "Viburnum opulus": "#6D8F55", "Viburnum tinus": "#4F6C44", 
    "Weigela florida": "#6F9960", "Yucca elephantipes": "#5A7A48", 
    "Murraya paniculata": "#6FA866", "Strelitzia nicolai": "#5C7F5A", 
    "Carissa macrocarpa": "#58784A", "Bougainvillea glabra": "#6A8F58", 
    "Bougainvillea spectabilis": "#6F965C", "Campsis radicans": "#6FA766", 
    "Hedera helix": "#4A6A3F", "Ipomoea purpurea": "#6F8C58", 
    "Jasminum fruticans": "#6DA65C", "Jasminum nudiflorum": "#7FAF6A", 
    "Jasminum officinale": "#6FA966", "Lonicera japonica": "#6D8F59", 
    "Parthenocissus quinquefolia": "#5A7A4A", "Plumbago capensis (Plumbago auriculata)": "#7FAF82",
    "Trachelospermum jasminoides": "#587A4A", "Wisteria sinensis": "#7FA96C",
    "Caesalpinia gilliesii": "#9EB59C"
}

# 2. ALAN KATEGORİLERİ VE TASARIM KURALLARI
ALAN_KURALLARI = {
    "Otel Bahçesi": {"sema": "analogous", "etki": "Huzur, Lüks (Yumuşak Geçiş)"},
    "Villa Bahçesi": {"sema": "analogous", "etki": "Estetik, Kişisel Uyum (Yumuşak Geçiş)"},
    "Mahalle Parkı": {"sema": "triadic", "etki": "Canlılık, Kolay Algılanma (Dengeli Canlılık)"},
    "Kent Meydanı": {"sema": "complementary", "etki": "Kontrast, Odak Noktası (Güçlü Zıtlık)"},
    "Otoparklar": {"sema": "analogous", "etki": "İşlevsel, Göz Yormayan (Yumuşak Geçiş)"},
    "Spor Alanları": {"sema": "complementary", "etki": "Enerji, Yüksek Kontrast (Güçlü Zıtlık)"},
}

# 3. RENK HESAPLAMA FONKSİYONLARI
def hex_to_hls(hex_code):
    r, g, b = Color(hex_code).rgb
    # Color kütüphanesinden gelen RGB'yi colorsys ile HLS'ye çevir
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h, l, s

def hls_to_hex(h, l, s):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    # 0-1 aralığındaki RGB'yi Color nesnesi ile HEX'e çevir
    return Color(rgb=(r, g, b)).hex

def palet_olustur(hex_color, sema_tipi):
    h, l, s = hex_to_hls(hex_color)
    palet = [hex_color]
    
    # Renk tekerleği üzerinde açılara göre renkleri hesapla
    if sema_tipi == "complementary": 
        new_h = (h + 0.5) % 1.0 # 180 derece
        palet.append(hls_to_hex(new_h, l, s))
        
    elif sema_tipi == "analogous": 
        for angle in [0.083, -0.083]: # +/- 30 derece
            new_h = (h + angle) % 1.0
            palet.append(hls_to_hex(new_h, l, s))
            
    elif sema_tipi == "triadic": 
        for angle in [0.333, 0.666]: # 120 derece aralıklar
            new_h = (h + angle) % 1.0
            palet.append(hls_to_hex(new_h, l, s))

    return palet

# 4. STREAMLIT ARAYÜZÜNÜN BAŞLATILMASI
st.set_page_config(page_title="Peyzaj Renk Paleti Jeneratörü (AI Destekli)", layout="wide")

st.title("🌳 AI Destekli Peyzaj Renk Paleti Jeneratörü")
st.markdown("Proje alanına ve seçilen bitkiye göre otomatik renk uyumu (Adobe/Photoshop için HEX kodları) oluşturur.")

# Girişler için iki sütun oluşturma
col1, col2 = st.columns(2)

with col1:
    # 💥 Hata kaynağı olan eski kod kaldırıldı. Yeni temiz kod!
    alan_tipi = st.selectbox(
        "1. Proje Uygulama Alanını Seçin:",
        options=list(ALAN_KURALLARI.keys())
    )
    
with col2:
    bitki_adi = st.selectbox(
        "2. Odak Bitkinizi/Ağacınızı Seçin (Renk Kaynağı):",
        options=list(BITKI_KUTUPHANESI.keys())
    )

if bitki_adi and alan_tipi:
    
    ana_renk_hex = BITKI_KUTUPHANESI[bitki_adi]
    sema_tipi = ALAN_KURALLARI[alan_tipi]["sema"]
    sema_etki = ALAN_KURALLARI[alan_tipi]["etki"]

    sonuc_paleti = palet_olustur(ana_renk_hex, sema_tipi)

    # 5. ÇIKTI VE GÖRSELLEŞTİRME
    st.markdown("---")
    st.subheader("📊 Analiz Sonucu ve Önerilen Palet")

    st.info(f"**AI Kararı:** '{alan_tipi}' alanı için genellikle **{sema_tipi.capitalize()} Şeması** kullanılır. (Etki: {sema_etki})")

    st.markdown("#### 🎨 Önerilen Renk Paleti (Görsel)")
    
    cols_palet = st.columns(len(sonuc_paleti))
    
    for i, hex_code in enumerate(sonuc_paleti):
        label = "ODAK BİTKİ RENGİ" if i == 0 else "UYUMLU RENK"
        
        # HTML ile renk kutusu oluşturma (Yazı rengi kontrastını otomatik ayarlama)
        try:
            luminance = Color(hex_code).luminance
        except ValueError:
            luminance = 0.5 # Hata durumunda varsayılan
            
        text_color = '#000000' if luminance > 0.6 else '#FFFFFF' # Parlak renkse siyah yazı, koyu renkse beyaz yazı
        
        html_code = f"""
        <div style="background-color: {hex_code}; padding: 10px; border-radius: 5px; height: 100px; text-align: center; color: {text_color};">
            <p style="font-size: 14px; margin-top: 10px;">{label}</p>
            <p style="font-weight: bold; font-size: 18px;">{hex_code}</p>
        </div>
        """
        cols_palet[i].markdown(html_code, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("#### 📝 Detaylı Kod Çıktısı")
    st.code(f"Seçilen Bitki: {bitki_adi}\nRenk Şeması: {sema_tipi.capitalize()}\nÖnerilen Palet (HEX Kodları): {sonuc_paleti}")