import os
import sys
import pystray
import PIL.Image
import subprocess
import threading
from pystray import MenuItem as item

def get_resource_path(filename):
    """Get the correct path for files, whether running as a script or an exe."""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, filename)

icon_path = get_resource_path("icon.ico")
image = PIL.Image.open(icon_path)
cloudflared_path = get_resource_path("cloudflared-windows-amd64.exe")
tunnel_process = None

def start_cloudflare_tunnel():
    """Starts the Cloudflare Tunnel connection."""
    global tunnel_process
    if tunnel_process is None:
        try:
            tunnel_process = subprocess.Popen(
                [cloudflared_path, "access", "tcp", "--hostname", "mc.9livesgaming.com", "--url", "localhost:25565"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            print("Cloudflare Tunnel started.")
            update_menu(True)
        except Exception as e:
            print(f"Failed to start Cloudflare Tunnel: {e}")
    else:
        print("Cloudflare Tunnel is already running.")

def stop_cloudflare_tunnel():
    """Stops the Cloudflare Tunnel connection."""
    global tunnel_process
    if tunnel_process:
        tunnel_process.terminate()
        tunnel_process.wait()
        tunnel_process = None
        print("Cloudflare Tunnel stopped.")
        update_menu(False)
    else:
        print("No active Cloudflare Tunnel.")

def update_menu(enabled):
    """Updates the tray menu to reflect the tunnel status."""
    global icon
    indicator_text = "\u2714 Cloudflare (Enabled)" if enabled else "\u2716 Cloudflare (Disabled)"
    indicator_color = "green" if enabled else "red"
    icon.menu = pystray.Menu(
        item(indicator_text, lambda: None, enabled=False),
        item("Enable", on_clicked, enabled=not enabled),
        item("Disable", on_clicked, enabled=enabled),
        item("Exit", on_clicked)
    )
    icon.update_menu()

def on_clicked(icon, menu_item):
    """Handles tray menu clicks."""
    if str(menu_item) == "Enable":
        threading.Thread(target=start_cloudflare_tunnel, daemon=True).start()
    elif str(menu_item) == "Disable":
        stop_cloudflare_tunnel()
    elif str(menu_item) == "Exit":
        stop_cloudflare_tunnel()
        icon.stop()

# Initialize menu with disabled indicator
icon = pystray.Icon("jibble_client", image, menu=pystray.Menu(
    item("\u2716 Cloudflare (Disabled)", lambda: None, enabled=False),
    item("Enable", on_clicked),
    item("Disable", on_clicked, enabled=False),
    item("Exit", on_clicked)
))

icon.run()
