"""
Bot runner — bot.so লোড করে চালায়
চালান: python3 run.py
"""

import sys
import os
import importlib.util
import glob

# .env লোড করো
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv না থাকলেও চলবে, sys env থেকে নেবে

# .so ফাইল খোঁজো
so_files = glob.glob("bot.cpython*.so") + glob.glob("bot.so")

if not so_files:
    print("❌ bot.so ফাইল পাওয়া যায়নি!")
    print("   আগে compile করুন: bash compile.sh")
    sys.exit(1)

so_path = so_files[0]
print(f"✅ Loading: {so_path}")

# bot.so ইমপোর্ট ও চালু করো
spec = importlib.util.spec_from_file_location("bot", so_path)
bot_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bot_module)

# main() চালাও
if hasattr(bot_module, "main"):
    bot_module.main()
else:
    print("❌ bot module এ main() function পাওয়া যায়নি!")
    sys.exit(1)
