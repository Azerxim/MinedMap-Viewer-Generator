#!/bin/bash
# MinedMap Viewer Generator - Bash Launch Script
# This script manages the virtual environment and runs main.py

show_menu() {
    clear
    echo "================================"
    echo "  MinedMap Viewer Generator"
    echo "================================"
    echo ""
    echo "Select an option:"
    echo "1) Install virtual environment"
    echo "2) Run main.py"
    echo "3) Remove virtual environment"
    echo "4) Exit"
    echo ""
    echo "================================"
    echo ""
}

install_venv() {
    clear
    echo "Installing virtual environment..."
    echo ""
    
    if [ -d ".env" ]; then
        echo "Virtual environment already exists. Skipping installation."
    else
        python3 -m venv .env
        if [ $? -eq 0 ]; then
            echo "Virtual environment created successfully."
        else
            echo "Error creating virtual environment."
            read -p "Press Enter to return to menu..."
            return 1
        fi
    fi
    
    # Activate and upgrade pip
    echo "Activating virtual environment and upgrading pip..."
    source .env/bin/activate
    python -m pip install --upgrade pip
    
    if [ $? -eq 0 ]; then
        echo "Virtual environment ready."
    else
        echo "Error upgrading pip."
        deactivate 2>/dev/null
        read -p "Press Enter to return to menu..."
        return 1
    fi
    
    deactivate
    echo ""
    read -p "Press Enter to return to menu..."
}

run_main_script() {
    clear
    echo "Running main.py..."
    echo ""
    
    if [ ! -d ".env" ]; then
        echo "Virtual environment not found. Please install it first."
        echo ""
        read -p "Press Enter to return to menu..."
        return
    fi
    
    source .env/bin/activate
    python main.py
    deactivate
    
    echo ""
    read -p "Press Enter to return to menu..."
}

remove_venv() {
    clear
    echo "Removing virtual environment..."
    echo ""
    
    if [ -d ".env" ]; then
        rm -rf .env
        echo "Virtual environment removed successfully."
    else
        echo "Virtual environment not found."
    fi
    
    echo ""
    read -p "Press Enter to return to menu..."
}

# Main loop
while true; do
    show_menu
    read -p "Enter your choice (1-4): " choice
    
    case $choice in
        1) install_venv ;;
        2) run_main_script ;;
        3) remove_venv ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option. Please try again."
            sleep 2
            ;;
    esac
done
