# This script will be too large, so I'll do it in batches
# First, let's check what hysteroscopy looks like
import subprocess
result = subprocess.run(['wsl', 'bash', '-c', 'sed -n \"170,190p\" pages/procedures/pelvic-reproductive/hysteroscopy.html'], 
                       capture_output=True, text=True)
print(result.stdout)
