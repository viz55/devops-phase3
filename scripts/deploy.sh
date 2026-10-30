#!/bin/bash
# Usage: deploy.sh <app_dir>
# Requires DEPLOY_PASSWORD to be set in the environment.
set -euo pipefail

app_dir="${1:?usage: deploy.sh <app_dir>}"
: "${DEPLOY_PASSWORD:?DEPLOY_PASSWORD must be set in the environment}"

cd "$app_dir"
tar -czf /tmp/app.tar.gz ./*
echo "Deploying ${app_dir}"
