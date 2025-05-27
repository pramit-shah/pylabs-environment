#!/bin/bash

echo "🚀 Building and starting all PyLabs services..."

docker-compose -f ../docker-compose.yml up --build -d

echo "✅ All services are up and running!"
