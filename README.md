# 💀 METEXFO v5.0

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

---

## 🌌 Genel Bakış
**METEXFO v5.0**, sızma testi uzmanları ve güvenlik araştırmacıları için geliştirilmiş modern bir **"YAPILANDIRMA HATASI VE PANEL AVCISI"** otomasyon aracıdır. Klasik araçların aksine, sadece port taraması yapmaz; hedef ağları eşzamanlı (Multi-threading) olarak analiz eder, bulduğu açık yönetim panellerini ve zayıf şifreli servisleri yakalayarak hedefe en uygun **Metasploit** saldırı senaryosunu (`.rc` dosyasını) otomatik inşa eder.

### 🛡️ Neden METEXFO v5.0?

| Özellik | Açıklama |
| :--- | :--- |
| **Eşzamanlı Kuyruk** | Çoklu hedef taramalarında Thread-safe mimariyle ultra hızlı sonuç üretir. |
| **Panel Odaklı Mantık** | Karmaşık zafiyetler yerine doğrudan Apache Tomcat, Jenkins, MySQL gibi kritik servislerdeki insan kaynaklı zayıf yapılandırmaları hedefler. |
| **Otomatik Cephane** | Hedef servislerin SSL/TLS durumlarına kadar analiz ederek Metasploit için tetiğe basmaya hazır `.rc` dosyası derler. |
| **Derin Raporlama** | Barındırdığı log analiz motoru sayesinde Metasploit operasyonu bittikten sonra sızma başarı durumlarını süzerek önünüze serer. |

---

## 🛠️ Kurulum & Hazırlık

Sisteminizde `Nmap` kurulu olduğundan ve gerekli bağımlılıkların yüklendiğinden emin olun:

```bash
sudo apt update && sudo apt install nmap -y
git clone https://github.com
cd METEXFO
pip3 install python-nmap colorama
```

---

## 🚀 Kullanım Protokolü

### 1. Keşif ve Otomatik RC Operasyon Planı Üretimi
Tek bir hedefi veya virgülle ayrılmış çoklu IP adreslerini eşzamanlı tarayıp saldırı reçetesini hazırlamak için:
```bash
python3 mme5.py -t <HEDEF İP VEYA LİSTESİ> -l <KENDİ İP ADRESİMİZ>

# Örnek:
python3 mme5.py -t 192.168.1.50,192.168.1.60 -l 192.168.1.10
```

### 2. Metasploit Üzerinden Otomatik Saldırıyı Tetikleme
Oluşturulan reçeteyi tek komutla Metasploit üzerinde başlatın:
```bash
msfconsole -q -r metexfo_final_agent.rc
```

### 3. Görev Sonu Derin Log Analizi
Saldırı oturumu kapandıktan sonra logları tarayıp düşen panelleri raporlamak için:
```bash
python3 mme5.py -t 192.168.1.50 -l 192.168.1.10 --analyze
```

---

## 🔰 Örnek İşlem Çıktıları

### Keşif ve Eşleşme Aşaması
```text
    ██████╗  ██████╗ ███╗   ██╗██╗  ██╗██████╗ 
    ██╔══██╗██╔═══██╗████╗  ██║██║  ██║██╔══██╗
    ██████╔╝██║   ██║██╔██╗ ██║███████║██████╔╝
    ██╔═══╝ ██║   ██║██║╚██╗██║██╔══██║██╔═══╝ 
    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     

⚡ AGENT STATUS : MODERN LOGIC AGENT | VERSION : 5.0-VIVID
🎯 TOTAL TARGETS: 2 | MY LHOST: 192.168.1.10
🛡️ ENGINE MODE  : MODERN-MISCONFIG-SCAN
───────────────────────────────────────────────────────────────

[📡 TARAMA BAŞLADI] ➔ 192.168.1.50
    ├─ [PORT BULUNDU] 192.168.1.50:8080 (http Apache Tomcat/9.0)
    ├─ [ANALİZ] 192.168.1.50 ➔ PORT: 8080 [http apache tomcat/9.0]
    │  ├─ ➔ [ŞABLON EŞLEŞTİ] Apache Tomcat Yönetim Paneli Tespiti

[+] MODERN OPERASYON PLANI HAZIR: metexfo_final_agent.rc
[*] Metasploit ile çalıştırmak için: msfconsole -q -r metexfo_final_agent.rc
```

### Başarılı Sızma Sonrası Log Analiz Raporu (`--analyze`)
```text
[*] Modern Log Analiz Motoru Çalıştırılıyor...

╔═════════════════════════════════════════════════════════════════╗
║                 GÖREV SONU KRİTİK ANALİZ RAPORU                 ║
╠═════════════════════════════════════════════════════════════════╣
║ 💀 [CRITICAL] BAŞARI: Tomcat Paneli Zayıf Kimlik Bilgisiyle Düştü! 
║ 💀 [CRITICAL] BAŞARI: MySQL root Yetkisi Şifresiz Ele Geçirildi!  
╚═════════════════════════════════════════════════════════════════╝
```

---

## ⚖️ Yasal Uyarı
Bu araç yalnızca yasal sızma testleri, siber defans araştırmaları ve eğitim faaliyetleri amacıyla geliştirilmiştir. İzin alınmamış hedef sistemler üzerinde kullanılması yasal sorumluluk doğurabilir. Kullanıcı, aracın kullanımından doğabilecek tüm hukuki sonuçlardan kendisi sorumludur.

**Developer:** `GHOST0X02` | **Version:** `5.0-Elite`
