#!/bin/bash
# cleanDB.sh
# Limpia la base de datos de mysql y la carpeta databases de la respectiva app
echo "---------------------------------------------------------------"
dbName=spe
username=speclient
dbPasswd=spe2016

scriptDir=$(dirname -- "$(readlink -e -- "$BASH_SOURCE")")
cd "$scriptDir" && rm -rf ../../applications/*/databases/*

dbName=spe

sudo -u postgres dropdb spe
sudo -u postgres createdb -O speclient -E UTF8 spe

if [[ $? -eq 0 ]]; then
	echo "El script finalizo exitosamente"
else
	echo "Error limpiando la base de datos"
	exit
fi