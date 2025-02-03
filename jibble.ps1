# Correct backslash escaping
$downloadsPath = "$HOME\Downloads"
$destinationFolder = "$HOME\AppData\Roaming\.minecraft\jibble"
$fileName = "cloudflared-windows-amd64.exe"
$filePath = "$downloadsPath\$fileName"

# Check if the file exists in Downloads
if (Test-Path $filePath) {
    # Create the destination folder if it doesn't exist
    if (!(Test-Path $destinationFolder)) {
        New-Item -ItemType Directory -Path $destinationFolder -Force | Out-Null
    }
    
    # Move the file to the new folder
    $destinationFilePath = Join-Path -Path $destinationFolder -ChildPath $fileName
    Move-Item -Path $filePath -Destination $destinationFilePath -Force
    Write-Output "Moved $fileName to $destinationFolder"
    
    # Navigate to the new folder
    Set-Location -Path $destinationFolder
    
    # Run the Cloudflared command
    Start-Process -FilePath $destinationFilePath -ArgumentList "access tcp --hostname mc.9livesgaming.com --url localhost:25565" -NoNewWindow
} else {
    Write-Output "$fileName not found in Downloads folder."
}
