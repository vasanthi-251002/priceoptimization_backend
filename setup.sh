#!/bin/bash
# Quick setup script for Price Optimization Tool
# Run from the root of the project: bash setup.sh

set -e

echo ""
echo "=============================="
echo "  Price Optimization Tool"
echo "  Setup Script"
echo "=============================="
echo ""

# ── BACKEND ─────────────────────────────────────────────
echo "[1/5] Setting up Django backend..."
cd backend

python -m venv venv
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null

pip install -r requirements.txt --quiet

echo "[2/5] Running database migrations..."
python manage.py makemigrations --no-input
python manage.py migrate --no-input

echo "[3/5] Seeding demo data..."
python manage.py seed_data

echo ""
echo "✅ Backend ready!"
echo "   Start with: cd backend && source venv/bin/activate && python manage.py runserver"
echo ""

cd ..

# ── FRONTEND ─────────────────────────────────────────────
echo "[4/5] Installing React dependencies..."
cd frontend
npm install --silent

echo ""
echo "✅ Frontend ready!"
echo "   Start with: cd frontend && npm start"
echo ""

cd ..

echo "[5/5] Done!"
echo ""
echo "=============================="
echo "  DEMO LOGIN"
echo "  Email:    admin@demo.com"
echo "  Password: Admin@1234"
echo "=============================="
echo ""
echo "Open two terminals:"
echo "  Terminal 1: cd backend && source venv/bin/activate && python manage.py runserver"
echo "  Terminal 2: cd frontend && npm start"
echo ""
echo "Then open: http://localhost:3000"
