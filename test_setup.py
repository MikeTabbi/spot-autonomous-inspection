#!/usr/bin/env python3

import sys
import subprocess

print(f"Python version: {sys.version}")

# Check Spot SDK
try:
    import bosdyn.client
    print("✅ Spot SDK: Installed")
except:
    print("❌ Spot SDK: Not installed")

# Check Git CLI
def check_git():
    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return True
    except:
        return False

print("✅ Git: Available" if check_git() else "❌ Git: Not available")

print("\n🎉 Setup complete! Ready to start Week 1.")

