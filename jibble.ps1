$downloadsPath = "$HOME\Downloads"
$destinationPath = "$HOME\Minecraft.jibble"
$fileName = "cloudflared-windows-amd64.exe"
$filePath = "$downloadsPath\$fileName"

# Check if the file exists in Downloads
if (Test-Path $filePath) {
    # Create the destination folder if it doesn't exist
    if (!(Test-Path $destinationPath)) {
        New-Item -ItemType Directory -Path $destinationPath | Out-Null
    }
    
    # Move the file to the new folder
    Move-Item -Path $filePath -Destination $destinationPath -Force
    Write-Output "Moved $fileName to $destinationPath"
    
    # Navigate to the new folder
    Set-Location -Path $destinationPath
    
    # Run the Cloudflared command
    .\cloudflared-windows-amd64.exe access tcp --hostname mc.9livesgaming.com --url localhost:25565
} else {
    Write-Output "$fileName not found in Downloads folder."
}
