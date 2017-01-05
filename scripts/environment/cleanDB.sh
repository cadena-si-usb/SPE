#!/bin/bash
# cleanDB.sh
# Limpia la base de datos de mysql y la carpeta databases de la respectiva app
echo "---------------------------------------------------------------"
dbName=SPE
username=speclient
dbPasswd=spe2016

scriptDir=$(dirname -- "$(readlink -e -- "$BASH_SOURCE")")
cd "$scriptDir" && rm ../../applications/*/databases/*

dbName=SPE
mysql -uspeclient -pspe2016 <<MYSQL_SCRIPT
DROP DATABASE $dbName;
CREATE DATABASE $dbName;
MYSQL_SCRIPT

if [[ $? -eq 0 ]]; then
	echo "El script finalizo exitosamente"
else
	echo "Error limpiando la base de datos"
	exit
fi