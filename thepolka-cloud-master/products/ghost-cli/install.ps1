$ErrorActionPreference = "Stop"
$installDirectory = Join-Path $env:LOCALAPPDATA "ThePolka\GhostAgent"
New-Item -ItemType Directory -Force -Path $installDirectory | Out-Null
Copy-Item "$PSScriptRoot\ghost.py" $installDirectory -Force
Copy-Item "$PSScriptRoot\run.ps1" $installDirectory -Force
Write-Host "Installed Ghost Agent at $installDirectory"
Write-Host "Start it with: & '$installDirectory\run.ps1'"
