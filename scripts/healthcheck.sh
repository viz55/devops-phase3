#!/bin/bash
URL=localhost:8080/health
for i in 1 2 3; do
  curl -sf $URL && exit 0
  sleep 2
done
exit 1
