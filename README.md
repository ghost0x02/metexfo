
# 💀 METEXFO v5.0 | Multi-Language Edition

<p align="center">
<img src="https://shields.io">
<img src="https://shields.io">
<img src="https://shields.io">
<img src="https://shields.io">
</p>
<p align="center">
  <img src="https://hizliresim.com" width="600" alt="METEXFO Banner">
</p>

<p align="center">
<i>VERSION 5.0 METEXFO - GHOST0X02</i>
</p>

<p align="center">
  <a href="#-türkçe-dökümantasyon"><b>🇹🇷 Türkçe Dökümantasyon</b></a> | 
  <a href="#-english-documentation"><b>🇺🇸 English Documentation</b></a>
</p>

---

## 🇹🇷 Türkçe Dökümantasyon

### 🌌 Genel Bakış
**METEXFO v5.0**, sızma testi uzmanları ve güvenlik araştırmacıları için geliştirilmiş çoklu iş parçacığı (Multi-threading) destekli modern bir **"YAPILANDIRMA HATASI VE PANEL AVCISI"** otomasyon aracıdır. Sadece klasik port taraması yapmaz; bulduğu servislerin durumunu ve SSL yapılandırmalarını analiz ederek **Metasploit Framework** için tetiklenmeye hazır `.rc` saldırı senaryoları inşa eder. Görev sonu log analiz motoruyla sızma sonuçlarını süzebilir.

### 🛠️ Kurulum & Hazırlık
```bash
git clone https://github.com
cd METEXFO
pip3 install python-nmap colorama
```

### 🚀 Kullanım Parametreleri
Programı başlatırken `--lang tr` parametresi vererek tamamen Türkçe terminal arayüzü ile çalıştırabilirsiniz:

```bash
# Mod 1: Türkçe Arayüz ile Keşif ve Reçete Üretimi (Çoklu Hedef)
python3 mme5.py -t 192.168.1.50,192.168.1.60 -l 192.168.1.10 --lang tr

# Mod 2: Metasploit Üzerinden Otomatik Operasyonu Başlatma
msfconsole -q -r metexfo_final_agent.rc

# Mod 3: Türkçe Görev Sonu Derin Log Analiz Motoru
python3 mme5.py -t 192.168.1.50 -l 192.168.1.10 --lang tr --analyze
```

### 🔰 Örnek İşlem Çıktısı (TR)
```text
[📡 TARAMA BAŞLADI] ➔  192.168.1.50 
    ├─ [PORT BULUNDU] 192.168.1.50:8080 (http Apache Tomcat/9.0)
    ├─ [ANALİZ] 192.168.1.50 ➔ PORT: 8080 [http apache tomcat/9.0]
    │  ├─ ➔ [ŞABLON EŞLEŞTİ] Apache Tomcat Yönetim Paneli Tespiti
```

---

## 🇺🇸 English Documentation

### 🌌 Overview
**METEXFO v5.0** is a multi-threaded, modern **"MISCONFIGURATION & PANEL HUNTER"** automation orchestrator built for penetration testers and security researchers. Instead of plain banner grabbing, it deeply analyzes target ports, matches them against a modern template database, and automatically compiles production-ready `.rc` attack deployment scripts for **Metasploit Framework**. It features an integrated post-mission log parser to filter critical breaches.

### 🛠️ Installation & Setup
```bash
git clone https://github.com
cd METEXFO
pip3 install python-nmap colorama
```

### 🚀 Usage Parameters
You can launch the program with the `--lang en` flag to run the completely localized English terminal interface:

```bash
# Mode 1: Recon & RC Generation via English Interface (Multi-Target)
python3 mme5.py -t 192.168.1.50,192.168.1.60 -l 192.168.1.10 --lang en

# Mode 2: Launching Automated Operation via Metasploit
msfconsole -q -r metexfo_final_agent.rc

# Mode 3: Post-Mission Deep Log Parser (English)
python3 mme5.py -t 192.168.1.50 -l 192.168.1.10 --lang en --analyze
```

### 🔰 Execution Sample (EN)
```text
[📡 SCAN STARTED] ➔  192.168.1.50 
    ├─ [PORT FOUND] 192.168.1.50:8080 (http Apache Tomcat/9.0)
    ├─ [ANALYSIS] 192.168.1.50 ➔ PORT: 8080 [http apache tomcat/9.0]
    │  ├─ ➔ [TEMPLATE MATCHED] Apache Tomcat Manager Login Detection
```

---

## ⚖️ Yasal Uyarı / Disclaimer
**TR:** Bu araç yalnızca yasal sızma testleri ve eğitim amaçlı geliştirilmiştir. Yetkisiz sistemlerde kullanılması yasal sorumluluk doğurur.
**EN:** This tool is strictly developed for authorized penetration testing and educational purposes. Unauthorized deployment is illegal.

**Developer:** `GHOST0X02` | **Version:** `5.0-MultiLang`
