$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
if (Get-Command py -ErrorAction SilentlyContinue) {
    py -3 ghost.py
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    python ghost.py
} else {
    throw "Python 3 was not found. Install it from https://python.org/downloads/."
}
