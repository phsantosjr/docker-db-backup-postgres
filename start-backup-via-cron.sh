#!/bin/bash
set -e
echo -e " "
echo -e " ### Iniciando Backups ### "
cd /opt/projects/docker-db-backup-postgres/
echo -e " ## Entrou na pasta "
echo -e " ## Iniciando Bakup LC LOGS "
docker compose up db-bkp-postgres