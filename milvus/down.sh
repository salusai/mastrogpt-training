#!/bin/bash
cd "$(dirname $0)"
sudo docker compose down
sudo rm -Rvf volumes