[Setup]
AppName=JibbleClient
AppVersion=1.0
DefaultDirName={localappdata}\JibbleClient
OutputDir=dist
OutputBaseFilename=JibbleClientInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\jibble_client.exe"; DestDir: "{app}"
Source: "dist\cloudflared-windows-amd64.exe"; DestDir: "{app}"

[Icons]
Name: "{autoprograms}\JibbleClient"; Filename: "{app}\jibble_client.exe"
