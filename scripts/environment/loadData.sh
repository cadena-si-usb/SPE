#!/bin/bash
# loadData.sh
# Recibe el archivo de con el dump de la base de datos y lo carga en la bd SPE
echo "---------------------------------------------------------------"
if [ -z $1 ]; then
	dumpFile=spe_dump.sql
else
	dumpFile=$1
fi

dbName=SPE
mysql -uroot -proot <<MYSQL_SCRIPT
DROP DATABASE IF EXISTS $dbName;
CREATE DATABASE $dbName;
MYSQL_SCRIPT

echo "Iniciando carga de nueva base de datos"
./cleanD.sh 1
./cleanDB.sh 2

dbName=SPE
mysql -u speclient -pspe2016 $dbName < $dumpFile

if [[ $? -eq 0 ]]; then
	echo "El script finalizo exitosamente"
else
	echo "Error limpiando la base de datos"
	exit
fi