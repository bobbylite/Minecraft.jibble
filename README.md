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

## Installation Steps

### 1. Download Minecraft
If you haven't already, download and install Minecraft from the official website:
- [Minecraft Download](https://www.minecraft.net/en-us/download)

### 2. Download Cloudflared Client
Download the latest Cloudflared executable for Windows:
- [Download Cloudflared](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe)

### 3. Set Up Cloudflare Tunnel
Once the client is downloaded, follow these steps:
1. **Navigate to your Downloads folder**:
   - Press `Win + E` to open File Explorer.
   - Go to the location where you downloaded `cloudflared-windows-amd64.exe`.

2. **Run the following command in PowerShell**:
   - Open PowerShell (`Win + X` → `Windows Terminal (Admin)` or `PowerShell`).
   - Change directory to the Downloads folder:
     ```powershell
     cd $HOME\Downloads
     ```
   - Run the Cloudflare Tunnel:
     ```powershell
     .\cloudflared-windows-amd64.exe access tcp --hostname mc.9livesgaming.com --url localhost:25565
     ```

### 4. Connect to the Minecraft Server
- Open **Minecraft** and navigate to `Multiplayer`.
- Add a new server with the address: `localhost:25565`.
- Join the server and enjoy!

---

## Troubleshooting
- **PowerShell Execution Policy Issue**: If you encounter an execution policy error, try running:
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  ```
- **Connection Issues**: Ensure that Cloudflared is running and correctly connected to `mc.9livesgaming.com`.
- **Firewall or Antivirus Interference**: Temporarily disable your firewall or whitelist the Cloudflared client.

---

## Notes
- The Cloudflare Tunnel must remain **open** while playing.
- Every time you restart your PC, you must run the command again.

---

### 🚀 Enjoy your Minecraft adventure with Cloudflare security! 🎮

