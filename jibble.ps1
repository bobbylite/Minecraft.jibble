# Define paths
$destinationFolder = "$HOME\AppData\Roaming\.minecraft\jibble"
$exeUrl = "https://github.com/bobbylite/Minecraft.jibble/raw/main/minecraft-jibble/cloudflared-windows-amd64.exe"
$iconUrl = "https://raw.githubusercontent.com/bobbylite/Minecraft.jibble/refs/heads/main/minecraft-jibble/src/icon.ico"
$fileName = "cloudflared-windows-amd64.exe"
$iconFileName = "cloudflared-icon.ico"
$destinationExePath = Join-Path -Path $destinationFolder -ChildPath $fileName
$destinationIconPath = Join-Path -Path $destinationFolder -ChildPath $iconFileName

# Create the destination folder if it doesn't exist
if (!(Test-Path $destinationFolder)) {
    New-Item -ItemType Directory -Path $destinationFolder -Force | Out-Null
}

# Function to download a file
function Download-File {
    param (
        [string]$url,
        [string]$destinationPath
    )
    try {
        Invoke-WebRequest -Uri $url -OutFile $destinationPath -ErrorAction Stop
        Write-Output "Downloaded $(Split-Path -Path $destinationPath -Leaf) successfully."
    } catch {
        Write-Output "Failed to download $(Split-Path -Path $destinationPath -Leaf): $_"
    }
}

# Download the executable file
Download-File -url $exeUrl -destinationPath $destinationExePath

# Download the icon file
Download-File -url $iconUrl -destinationPath $destinationIconPath

# Navigate to the new folder
Set-Location -Path $destinationFolder

# Run the Cloudflared command
Start-Process -FilePath $destinationExePath -ArgumentList "access tcp --hostname mc.9livesgaming.com --url localhost:25565" -NoNewWindow
