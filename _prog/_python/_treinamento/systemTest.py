import os
print(os.system('lscpu' if os.name == 'posix' else 'systeminfo'))

