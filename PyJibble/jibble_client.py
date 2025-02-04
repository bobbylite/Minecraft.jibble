import os
import sys
import pystray
import PIL.Image
import subprocess
import threading

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
    else:
        print("No active Cloudflare Tunnel.")

def on_clicked(icon, item):
    """Handles tray menu clicks."""
    if str(item) == "Enable":
        threading.Thread(target=start_cloudflare_tunnel, daemon=True).start()
    elif str(item) == "Disable":
        stop_cloudflare_tunnel()
    elif str(item) == "Exit":
        stop_cloudflare_tunnel()
        icon.stop()

icon = pystray.Icon("jibble_client", image, menu=pystray.Menu(
    pystray.MenuItem("Cloudflare", pystray.Menu(
        pystray.MenuItem("Enable", on_clicked),
        pystray.MenuItem("Disable", on_clicked)
    )),
    pystray.MenuItem("Exit", on_clicked)
))

icon.run()
