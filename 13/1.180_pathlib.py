# Can manipulate Windows paths on a Unix machine (or vice versa).
from pathlib import Path

# !!!!! Відносто директорії де запускається скрипт, а не там де він фактично знаходиться!!!!!!! 
p = Path('.')

#print([x for x in p.iterdir() if x.is_dir()])

print(list(p.glob('*.py')))