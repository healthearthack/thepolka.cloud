$installDirectory = Join-Path $env:LOCALAPPDATA "ThePolka\GhostAgent"
if (Test-Path $installDirectory) {
    Remove-Item $installDirectory -Recurse -Force
}
Write-Host "Ghost Agent application files removed."
Write-Host "Your local ledger remains at $env:USERPROFILE\.ghost\stream.log"
