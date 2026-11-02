# 1. Mengimpor seluruh modul
import Exercise8_16 as fungsi_salam

fungsi_salam.sapa_pengguna('Sergie')


# 2. Mengimpor fungsi tertentu
from Exercise8_16 import sapa_pengguna

sapa_pengguna('Sergie')


# 3. Mengimpor fungsi dengan nama alias
from Exercise8_16 import sapa_pengguna as sp

sp('Sergie')


# 4. Mengimpor modul dengan nama alias
import Exercise8_16 as mn

mn.sapa_pengguna('Sergie')


# 5. Mengimpor semua fungsi dari modul
from Exercise8_16 import *

sapa_pengguna('Sergie')