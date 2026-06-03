import argparse
import os
import threading
import re
from queue import Queue, Empty
from colorama import Fore, Back, Style, init
import nmap

init(autoreset=True)

LOCALES = {
    "tr": {
        "status": "DURUM",
        "targets": "HEDEFLER",
        "scan_start": "[TARAMA BAŞLADI] ➔",
        "port_found": "├─ [PORT BULUNDU]",
        "analysis": "├─ [ANALİZ]",
        "template_match": "│  ├─ ➔ [SONUÇ]",
        "inactive": "└─ [SONUÇ] {} aktif değil veya portları kapalı.\n",
        "error": "└─ [!] HATA ({}): {}\n",
        "compile_success": "[+] RC DOSYASI HAZIRLANDI",
        "path": "Dosya Yolu",
        "run_cmd": "Metasploit üzerinde çalıştırmak için bu komutu kullanın"
    },
    "en": {
        "status": "AGENT STATUS",
        "version": "VERSION",
        "targets": "TOTAL TARGETS",
        "engine_mode": "ENGINE MODE",
        "scan_start": "[SCAN STARTED] ➔",
        "port_found": "├─ [PORT FOUND]",
        "analysis": "├─ [ANALYSIS]",
        "template_match": "│  ├─ ➔ [TEMPLATE MATCHED]",
        "inactive": "└─ [SILENT] {} is inactive or ports are closed.\n",
        "error": "└─ [!] ERROR ({}): {}\n",
        "compile_success": "[+] RC FILE GENERATED SUCCESSFULLY",
        "path": "File Path",
        "run_cmd": "Use this command to execute on Metasploit"
    }
}

class MetexfoModernAgent:
    def __init__(self, target_list, lhost, lang="en"):
        self.targets = target_list
        self.lhost = lhost
        self.lang = lang if lang in ["tr", "en"] else "en"
        self.txt = LOCALES[self.lang]

        self.rc_file = "metexfo.rc"
        self.log_file = "agent_deep_log.txt"
        self.queue = Queue()
        self.lock = threading.Lock()
        self.nm = nmap.PortScanner()
        self.processed_targets = {}

        self.msf_commands = [
            f"spool {self.log_file}",
            "setg ExitOnSession false",
            "setg LHOST " + self.lhost
        ]

        self.modern_vulnerability_db = {
            "http": [
                {
                    "name": "Apache Tomcat Yönetim Paneli" if self.lang=="tr" else "Apache Tomcat Manager",
                    "module": "auxiliary/scanner/http/tomcat_mgr_login",
                    "setup_commands": ["set BLANK_PASSWORDS true", "set STOP_ON_SUCCESS true"]
                },
                { 
                    "name": "Jenkins Otomasyon Sunucusu" if self.lang=="tr" else "Jenkins Automation Server",
                    "module": "auxiliary/scanner/http/jenkins_enum",
                    "setup_commands": []
                }
            ],
            "mysql": [
                {
                    "name": "MySQL Boş Şifre Kontrolü" if self.lang=="tr" else "MySQL Blank Password Check",
                    "module": "auxiliary/scanner/mysql/mysql_login",
                    "setup_commands": ["set USERNAME root", "set BLANK_PASSWORDS true", "set STOP_ON_SUCCESS true"]
                }
            ]
        }

        for target in self.targets:
            self.queue.put(target)

    def banner(self):
        os.system("clear")
        print(f"{Fore.RED}{Style.BRIGHT}                CODED BY GHOST0X02")
        print(f"{Fore.WHITE}{Style.BRIGHT}                     .--------.")
        print(f"{Fore.WHITE}{Style.BRIGHT}                    /          \\")
        print(f"{Fore.WHITE}{Style.BRIGHT}                   |   __  __   |")
        print(f"{Fore.WHITE}{Style.BRIGHT}                   |  /  \\/  \\  |")
        print(f"{Fore.WHITE}{Style.BRIGHT}                   |  |()||()|  |")
        print(f"{Fore.RED}{Style.BRIGHT}                   |  \\__/\\__/  |")
        print(f"{Fore.RED}{Style.BRIGHT}                   |     ||     |")
        print(f"{Fore.RED}{Style.BRIGHT}                   |  \\_`=='_/  |")
        print(f"{Fore.RED}{Style.BRIGHT}                    \\  `----'  /")
        print(f"{Fore.RED}{Style.BRIGHT}                     '--------'")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}")
        print(r"    __  ___   ______  ______   ______   _  __   ______  ____  ")
        print(r"   /  |/  /  / ____/ /_  __/  / ____/  | |/ /  / ____/ / __ \ ")
        print(r"  / /|_/ /  / __/     / /    / __/     |   /  / /_    / / / / ")
        print(r" / /  / /  / /___    / /    / /___    /   |  / __/   / /_/ /  ")
        print(r"/_/  /_/  /_____/   /_/    /_____/   /_/|_| /_/      \____/   v1.2")
        print(f"{Fore.RED}{Style.BRIGHT}    " + "═" * 53)
        print(f"{Fore.GREEN}{Style.BRIGHT}>> {self.txt['status']:<8}: {Fore.WHITE} <3")
        print(f"{Fore.RED}{Style.BRIGHT}>> {self.txt['targets']:<8}: {Fore.WHITE}{len(self.targets)}")
        print(f"{Fore.RED}{Style.BRIGHT}    " + "═" * 53 + "\n")

    def attack_engine(self, target, port, service_name, version):
        full_service = f"{service_name} {version}".lower().strip()
        service_key = "http" if "http" in service_name.lower() or port in [80, 443, 8080] else service_name.lower()

        if target not in self.processed_targets:
            self.processed_targets[target] = set()

        if port in self.processed_targets[target]:
            return

        self.processed_targets[target].add(port)

        with self.lock:
            print(f"{Fore.RED}{self.txt['analysis']} {Fore.WHITE}{target} ➔ {Fore.GREEN}PORT: {port} {Fore.LIGHTBLACK_EX}[{full_service}]")

        if service_key in self.modern_vulnerability_db:
            for scan_template in self.modern_vulnerability_db[service_key]:
                with self.lock:
                    print(f"{Fore.RED}{self.txt['template_match']} {Fore.LIGHTGREEN_EX}{scan_template['name']}")
                
                self.msf_commands.extend([
                    f"use {scan_template['module']}",
                    f"set RHOSTS {target}",
                    f"set RPORT {port}"
                ])
                if scan_template["setup_commands"]:
                    self.msf_commands.extend(scan_template["setup_commands"])
                self.msf_commands.append("run")

    def worker(self):
        while not self.queue.empty():
            try:
                target = self.queue.get_nowait()
            except Empty:
                break

            with self.lock:
                print(f"{Fore.GREEN}{Style.BRIGHT}{self.txt['scan_start']} {Fore.WHITE}{Back.GREEN} {target} ")

            try:
                self.nm.scan(target, arguments='-sS -sV -T3 --open -p 21,80,443,3306,8080')

                if target in self.nm.all_hosts():
                    for proto in self.nm[target].all_protocols():
                        for port in self.nm[target][proto].keys():
                            service = self.nm[target][proto][port]['name']
                            version = self.nm[target][proto][port].get('version', '')
                            
                            with self.lock:
                                print(f"{Fore.GREEN}{self.txt['port_found']} {Fore.WHITE}{target}:{Fore.RED}{port}")
                                
                            self.attack_engine(target, port, service, version)
                else:
                    with self.lock:
                        print(f"{Fore.LIGHTBLACK_EX}{self.txt['inactive'].format(target)}")
            except Exception as e:
                with self.lock:
                    print(f"{Fore.RED}{self.txt['error'].format(target, str(e))}")
            finally:
                self.queue.task_done()

    def save_rc(self):
        with open(self.rc_file, "w") as f:
            for cmd in self.msf_commands:
                f.write(cmd + "\n")
        
        print(f"\n{Fore.GREEN}{Style.BRIGHT}{self.txt['compile_success']}")
        print(f"➔ {Fore.RED}{self.txt['path']}: {Fore.WHITE}{self.rc_file}")
        print(f"➔ {Fore.GREEN}{self.txt['run_cmd']}: {Fore.RED}msfconsole -q -r {self.rc_file}")

    def run(self):
        self.banner()

        threads = []
        for _ in range(min(5, len(self.targets))):
            t = threading.Thread(target=self.worker)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        self.save_rc()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", required=True)
    parser.add_argument("-l", "--lhost", required=True)
    parser.add_argument("--lang", default="en")

    args = parser.parse_args()
    targets = [t.strip() for t in args.target.split(",")]

    agent = MetexfoModernAgent(targets, args.lhost, args.lang)
    agent.run()
