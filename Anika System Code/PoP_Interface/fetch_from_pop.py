import pyperclip
import pandas as pd
import time
import os
import subprocess
from datetime import datetime
from io import StringIO

def open_publish_or_perish():
    path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Publish or Perish 8.lnk"
    subprocess.Popen(['cmd', '/c', 'start', '', path])
    print(f"🚀 Opened Publish or Perish")

def close_publish_or_perish():
    subprocess.call(['taskkill', '/F', '/IM', 'Publish or Perish.exe'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("❌ Closed Publish or Perish")

def wait_for_excel_clipboard_and_process():
    open_publish_or_perish()
    print("📋 Waiting for Excel data from clipboard... Please use 'Copy as Excel with Header'")

    # Clear clipboard to avoid using old data
    pyperclip.copy("")
    old_clipboard = ""

    while True:
        time.sleep(1)
        current_clipboard = pyperclip.paste()
        if current_clipboard != old_clipboard and "\t" in current_clipboard:
            try:
                df = pd.read_csv(StringIO(current_clipboard), sep="\t")
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                save_path = f"pop_data_{timestamp}.xlsx"
                df.to_excel(save_path, index=False)
                print(f"✅ Saved copied data to {save_path}")
                close_publish_or_perish()
                return save_path
            except Exception as e:
                print(f"⚠️ Error: {e}")
        else:
            print("⌛ Waiting for new clipboard content...")
        old_clipboard = current_clipboard
