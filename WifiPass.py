import subprocess

class NetworkInformation:
    
    def __init__(self):
        self._getNetworkInfo()
        
    def _getNetworkInfo(self):
        profile = subprocess.run('netsh wlan show profiles', shell=True, capture_output=True, text=True)
        self.decoded_profile = profile.stdout.split('\n')
        while '' in self.decoded_profile:
            self.decoded_profile.remove('')
        
        start_index = self.decoded_profile.index('-------------')
        self.Networks = self.decoded_profile[start_index + 1: len(self.decoded_profile)]
        self.networkName = []
        
        for network in self.Networks:
            self.networkName.append(network.split(':')[-1].lstrip())
        
        self._getKey(self.networkName)
        
    def _getKey(self, name):
        keys = []
        for names in name:
            try:
                self.key_data = subprocess.run(f'netsh wlan show profiles {names} key=clear', 
                                                   shell=True, 
                                                   capture_output=True, 
                                                   text=True)
            except:
                print(f"Could not obtain key of {names}. Please check if you have Adiministrator Privileges on this decive")
            
                
            byte_data = self.key_data.stdout.split('\n')
            self.parsed_data = []
            while '' in byte_data:
                byte_data.remove('')
            
            for i in range(len(byte_data)):
                self.parsed_data.append(byte_data[i].lstrip())
            
            found_key = False
            for line in self.parsed_data:
                if 'Name' in line:
                    self.name = line.split(':')[-1].lstrip()
                if 'Key Content' in line:
                    print(f"the key of {self.name} is {line.split(':')[-1].lstrip()}")
                    found_key = True
                
            if found_key == False:        
                print(f"\n Could not find key for {self.name} or key does not exist. Please check if you have Administrator Privileges on this decive")
print(r'''   _____                                 _____      _   _                       
  / ____|                               |  __ \    | | (_)                      
 | (___  _ __ ___  _____   ____ _ _ __  | |__) |_ _| |_ _ _   _  __ _ _ __ __ _ 
  \___ \| '__/ _ \/ _ \ \ / / _` | '__| |  ___/ _` | __| | | | |/ _` | '__/ _` |
  ____) | | |  __/  __/\ V / (_| | |    | |  | (_| | |_| | |_| | (_| | | | (_| |
 |_____/|_|  \___|\___| \_/ \__,_|_|    |_|   \__,_|\__|_|\__, |\__,_|_|  \__,_|
                                                           __/ |                
                                                          |___/                 ''')
print('\n********************************************************************************')
print("\n* Copyright of Sreevar Patiyara, 2022")
print('\n* Github: https://github.com/SreevarP')
print('\n* Email: sreevarpatiyara@gmail.com')
print(r'''  _       ___ _____ ____                 
| |     / (_) __(_) __ \____ ___________
| | /| / / / /_/ / /_/ / __ `/ ___/ ___/
| |/ |/ / / __/ / ____/ /_/ (__  |__  ) 
|__/|__/_/_/ /_/_/    \__,_/____/____/  
                                        ''')
print("\n Version 1.0")
print('\n********************************************************************************')
if __name__ == '__main__':
    NetworkInformation()