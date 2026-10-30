#!/bin/bash
# deploy app
APP_DIR=$1
pw="admin123"
cd $APP_DIR
tar -czf /tmp/app.tar.gz *
echo "deploying with password $pw"
