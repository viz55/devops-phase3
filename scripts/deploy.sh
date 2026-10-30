#!/bin/bash
# deploy app 
# Usage: deploy.sh <app_dir>
APP_DIR=$1
pw="admin123"
cd $APP_DIR || exit 1
tar -czf /tmp/app.tar.gz *
echo "deploying with password $pw"
