# Minecraft.jibble
Guide for the infamous JB minecraft server.

# Minecraft Cloudflare Tunnel Setup

## Introduction
This guide will help you set up and connect to a Minecraft server using Cloudflare's Cloudflared client. Follow the steps below to get started.

---

## Prerequisites
- A **Minecraft** client installed on your system ([Download here](https://www.minecraft.net/en-us/download)).
- A **Cloudflare Tunnel client** (Cloudflared) downloaded.
- Basic familiarity with the command line.

---

## Jibble Client
The following mods are used in this setup:
- **Cloudflare Client**: [jibble_client.exe](https://github.com/bobbylite/Minecraft.jibble/raw/refs/heads/main/release/jibble_client.exe)

---

## Easy Installation Steps
### 1. Download the `jibble.ps1` script [ here](https://raw.githubusercontent.com/bobbylite/Minecraft.jibble/refs/heads/main/jibble.ps1)
### 2. Run the `jibble.ps1` script

## Manual Installation Steps

### 1. Download Minecraft
If you haven't already, download and install Minecraft from the official website:
- [Minecraft Download](https://www.minecraft.net/en-us/download)

### 2. Download Cloudflared Client
Download the latest Cloudflared executable for Windows:
- [Download Cloudflared](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe)

### 3. Set Up Cloudflare Tunnel
Once the client is downloaded, follow these steps:
1. **Navigate to your Downloads folder**:
   - Press Win + E to open File Explorer.
   - Go to the location where you downloaded cloudflared-windows-amd64.exe.

2. **Run the following command in PowerShell**:
   - Open PowerShell (Win + X → Windows Terminal (Admin) or PowerShell).
   - Change directory to the Downloads folder:
     
     ```powershell
     cd $HOME\Downloads
     ```
     
   - Run the Cloudflare Tunnel:
     
     ```powershell
     .\cloudflared-windows-amd64.exe access tcp --hostname mc.9livesgaming.com --url localhost:25565
     ```

### 4. Connect to the Minecraft Server
- Open **Minecraft** and navigate to Multiplayer.
- Add a new server with the address: localhost:25565.
- Join the server and enjoy!

---

## Troubleshooting
- **PowerShell Execution Policy Issue**: If you encounter an execution policy error, try running:
  
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  ```
  
- **Connection Issues**: Ensure that Cloudflared is running and correctly connected to mc.9livesgaming.com.
- **Firewall or Antivirus Interference**: Temporarily disable your firewall or whitelist the Cloudflared client.

---

## Notes
- The Cloudflare Tunnel must remain **open** while playing.
- Every time you restart your PC, you must run the command again.

---

## Mods
The following mods are used in this setup:
- **OptiFine**: [Download OptiFine](https://optifine.net/adloadx?f=preview_OptiFine_1.21.4_HD_U_J3_pre10.jar&x=0f37)
- **BSL Shaders**: [Download BSL Shaders](https://www.curseforge.com/minecraft/shaders/bsl-shaders/files/6018643)

---

## Development
Run this command in the `PyJibble` directory to build the jibble_client.py executable for windows.
```bsh
pyinstaller --noconsole --onefile --icon=jibble.py\icon.ico --add-binary "jibble.py\\cloudflared-windows-amd64.exe;." --add-data "jibble.py\\icon.ico;." jibble.py\jibble_client.py
```

---

### 🚀 Enjoy your Minecraft adventure with Cloudflare security! 🎮

