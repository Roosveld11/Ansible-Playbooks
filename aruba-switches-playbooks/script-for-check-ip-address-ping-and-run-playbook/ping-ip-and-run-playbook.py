import os
import subprocess


#---Change the IP address to yours
response = os.system("ping -c 5 192.168.1.1")

if response == 0:
    print('\n----------IP address is available-----------\n')

else:
    print('\n----------IP address is not available. Run the PLAYBOOK----------\n')
    subprocess.run(['ansible-playbook', '/"specify-the-path-to-the-file"/aruba-commands.yaml', '-i', '/"specify-the-path-to-the-file"/hosts'])
