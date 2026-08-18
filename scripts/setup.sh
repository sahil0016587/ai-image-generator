#!/bin/bash
# Clean Auto-Setup Script for ComfyUI Environment

echo "🚀 Starting System Setup..."

# 1. Clone ComfyUI if not present
if [ ! -d "ComfyUI" ]; then
    echo "📦 Cloning ComfyUI..."
    git clone https://github.com/comfyanonymous/ComfyUI.git
fi

cd ComfyUI

# 2. Install Required Custom Nodes
echo "🔌 Installing Custom Nodes..."
cd custom_nodes

# ComfyUI Manager
if [ ! -d "ComfyUI-Manager" ]; then
    git clone https://github.com/ltdrdata/ComfyUI-Manager.git
fi

# Reactor (Face Swap Node)
if [ ! -d "comfyui-reactor-node" ]; then
    git clone https://github.com/Gourieff/comfyui-reactor-node.git
fi

cd ..

# 3. Install Python Dependencies
echo "📚 Installing Python packages..."
pip install -r requirements.txt
pip install fastapi uvicorn requests python-multipart

echo "✅ Environment Setup Completed Successfully!"
