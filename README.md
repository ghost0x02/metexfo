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
**METEXFO v5.0**, sızma testi uzmanları ve güvenlik araştırmacıları için geliştirilmiş bir **"GENEL ZAFİYET"** aracıdır. Klasik araçların aksine, sadece tarama yapmaz; hedefleri çoklu iş parçacığı (Multi-threading) ile analiz eder ve bulunan servislere en uygun Metasploit saldırı senaryosunu hazırlar.

### 🛡️ Neden METEXFO?

| Özellik | Açıklama |
| :--- | :--- |
| **Senaryo** | Hedefin portlarına göre saldırı senaryosunu anlık değiştirir. |
| **Metasploit** | Versiyon bilgilerini Metasploit DB ile otomatik eşleştirir. |
| **Sızma** | Sızma sonrası sistem bilgilerini otomatik çeker. |
| **Sorunsuz** | Firewall takılmalarını minimize eden tarama teknikleri. |

---

## 🛠️ Kurulum & Hazırlık

```bash
git clone https://github.com
cd METEXFO
pip3 install python-nmap colorama
python3 mme5.py -t <HEDEF İP VEYA LİSTESİ> -l <KENDİ İP ADRESİMİZ>
```

---

## 🔰 Örnek işlem

```text
    ██████╗  ██████╗ ███╗   ██╗██╗  ██╗██████╗ 
    ██╔══██╗██╔═══██╗████╗  ██║██║  ██║██╔══██╗
    ██████╔╝██║   ██║██╔██╗ ██║███████║██████╔╝
    ██╔═══╝ ██║   ██║██║╚██╗██║██╔══██║██╔═══╝ 
    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     

[*] Taranıyor...
[📡 TARAMA BAŞLADI] ➔ 192.168.1.50
    ├─ [PORT BULUNDU] 192.168.1.50:8080 (http Apache Tomcat/9.0)
    ├─ [ANALİZ] 192.168.1.50 ➔ PORT: 8080 [http apache tomcat/9.0]
    │  ├─ ➔ [ŞABLON EŞLEŞTİ] Apache Tomcat Yönetim Paneli Tespiti

[GHOST0X02] RC dosyası >  metexfo_final_agent.rc
>> KOMUT: msfconsole -q -r metexfo_final_agent.rc
```

---

## ⚖️ Yasal Uyarı
Bu araç yalnızca yasal sızma testleri ve eğitim amaçlı geliştirilmiştir. 
