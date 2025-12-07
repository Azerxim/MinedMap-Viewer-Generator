# MinedMap Viewer Generator - PowerShell Launch Script
# This script manages the virtual environment and runs main.py

function Show-Menu {
    Clear-Host
    Write-Host "================================" -ForegroundColor Green
    Write-Host "  MinedMap Viewer Generator" -ForegroundColor Green
    Write-Host "================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Select an option:" -ForegroundColor Yellow
    Write-Host "1) Install virtual environment"
    Write-Host "2) Run main.py"
    Write-Host "3) Remove virtual environment"
    Write-Host "4) Exit"
    Write-Host ""
    Write-Host "================================" -ForegroundColor Green
    Write-Host ""
}

function Install-VirtualEnv {
    Clear-Host
    Write-Host "Installing virtual environment..." -ForegroundColor Cyan
    Write-Host ""
    
    if (Test-Path ".\.env") {
        Write-Host "Virtual environment already exists. Skipping installation." -ForegroundColor Yellow
    } else {
        python -m venv .env
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Virtual environment created successfully." -ForegroundColor Green
        } else {
            Write-Host "Error creating virtual environment." -ForegroundColor Red
            return $false
        }
    }
    
    # Activate and upgrade pip
    Write-Host "Activating virtual environment and upgrading pip..." -ForegroundColor Cyan
    & ".\\.env\\Scripts\\python.exe" -m pip install --upgrade pip
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Virtual environment ready." -ForegroundColor Green
    } else {
        Write-Host "Error upgrading pip." -ForegroundColor Red
        return $false
    }
    
    Write-Host ""
    Write-Host "Press any key to return to menu..." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}

function Run-MainScript {
    Clear-Host
    Write-Host "Running main.py..." -ForegroundColor Cyan
    Write-Host ""
    
    if (-not (Test-Path ".\.env")) {
        Write-Host "Virtual environment not found. Please install it first." -ForegroundColor Red
        Write-Host ""
        Write-Host "Press any key to return to menu..." -ForegroundColor Yellow
        $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        return
    }
    
    & ".\\.env\\Scripts\\python.exe" main.py
    
    Write-Host ""
    Write-Host "Press any key to return to menu..." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}

function Remove-VirtualEnv {
    Clear-Host
    Write-Host "Removing virtual environment..." -ForegroundColor Cyan
    Write-Host ""
    
    if (Test-Path ".\.env") {
        Remove-Item -Recurse -Force ".\.env"
        Write-Host "Virtual environment removed successfully." -ForegroundColor Green
    } else {
        Write-Host "Virtual environment not found." -ForegroundColor Yellow
    }
    
    Write-Host ""
    Write-Host "Press any key to return to menu..." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}

# Main loop
do {
    Show-Menu
    $choice = Read-Host "Enter your choice (1-4)"
    
    switch ($choice) {
        "1" { Install-VirtualEnv }
        "2" { Run-MainScript }
        "3" { Remove-VirtualEnv }
        "4" { 
            Write-Host "Exiting..." -ForegroundColor Yellow
            exit
        }
        default {
            Write-Host "Invalid option. Please try again." -ForegroundColor Red
            Start-Sleep -Seconds 2
        }
    }
} while ($true)
