# SteamNLP Project - Proje Raporu

**Tarih:** 2026-06-02
**Hazırlayan:** Proje otomasyonu (yardımcı)

## 1. Proje Özeti
Bu proje, Steam oyun incelemeleri verisi üzerinde doğal dil işleme ve makine öğrenmesi uygulamalarıyla kullanıcı öneri / duygu sınıflandırması yapmak amacıyla oluşturulmuştur. Veri temizleme, özellik mühendisliği (TF-IDF + sayısal özellikler), modellerin eğitimi ve Streamlit tabanlı bir uygulama arayüzü geliştirilmiştir.

## 2. Yapılanlar (Tamamlanan işler)
- Proje klasör yapısı düzenlendi ve temel script/notebook konfigürasyonu sağlandı.
- Veri yükleme ve ön işleme adımları uygulandı (raw -> processed). İşlem sonuçları `data/processed/` içinde saklanıyor.
- TF-IDF vektörleştirme uygulandı ve `tfidf_vectorizer.joblib` kaydedildi.
- Sayısal ve kategorik özellikler çıkarıldı ve `X_combined` oluşturuldu.
- Çeşitli modeller denendi; en iyi model `models/champion_model.joblib` olarak saklandı.
- Streamlit uygulaması (`app.py` ve `pages/`) için başlangıç temasal ve UI düzenlemeleri yapıldı, başlatma talimatı verildi (örn. `python -m streamlit run app.py`).
- Notebook (`SteamNLP.ipynb`) içinde BERT sentence-transformer embedding çıkarımı için bir kod bloğu eklendi; embeddingler SVD ile indirgenip ölçeklenerek `bert_features` DataFrame'i oluşturuldu ve `X_combined`'a eklendi.

## 3. Yapılmayanlar / Kısıtlar
- Tam otomatize eğitim-cevap (CI) pipeline'ı yok; model eğitimi elle tetikleniyor.
- Hyperparametre araması sınırlı; geniş çaplı Grid/Random search ve ensemble optimizasyonu tamamlanmadı.
- Model açıklanabilirliği (SHAP/LIME) kısmi; tam rapor/etki analizi eksik.
- Özellikle BERT tabanlı embeddinglerin etkisi üzerinde kapsamlı model karşılaştırması ve düzenli cross-validation çalışmaları kısıtlı süre nedeniyle sınırlı uygulanmıştır.
- Streamlit uygulaması yerel olarak test edildi; dağıtım (Heroku/Cloud) adımları ve Dockerfile yok.

## 4. Teknik Notlar
- Notebook: `SteamNLP.ipynb` (özellikle ADIM 10 civarında feature birleşimi ve BERT hücresi).
- Modeller: `models/champion_model.joblib`, `models/features_champion.joblib`.
- Önemli yardımcı scriptler: `app.py`, `utils/feature_engineering.py`, `utils/loader.py`.

## 5. Öneriler / Sonraki Adımlar
- BERT gömme özelliklerinin (bert_features) modele katkısını nicel olarak test edin (ablasyon çalışması).
- ROC-AUC gibi sınıflandırma metriklerine odaklanarak dengesiz sınıf problemi için ağırlıklı kayıp veya yeniden örnekleme yöntemleri uygulayın.
- Hyperparameter aramalarını genişletin (Optuna/Hyperopt kullanımı önerilir).
- Model açıklanabilirliği için SHAP entegrasyonu ekleyin ve Streamlit içinde interaktif görselleştirmeler oluşturun.
- Projeyi kapsayan küçük bir Dockerfile ve kolay deploy adımları hazırlayın.

## 6. Dosya Listesi (Öne çıkanlar)
- `SteamNLP.ipynb` - Analiz ve preprocessing notebook
- `app.py` - Streamlit giriş noktası
- `pages/` - Streamlit sayfaları
- `data/processed/` - Ön işlenmiş veri ve joblib artefaktları
- `models/` - Eğitilmiş model ve metadata


---

Bu raporu PDF'e dönüştürmek için aynı klasörde `generate_report_pdf.py` betiğini oluşturdum; betik Markdown dosyasını okuyup `report.pdf` üretecektir.
