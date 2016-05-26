#!/bin/bash
# loadData.sh
# Recibe el archivo de con el dump de la base de datos y lo carga en la bd SPE
echo "---------------------------------------------------------------"
if [ -z $1 ]; then
	dumpFile=spe_dump.sql
else
	dumpFile=$1
fi

echo "Iniciando carga de nueva base de datos"
./cleanDB 1
./cleanDB 2

dbName=SPE
mysql -u speclient -pspe2016 $dbName < $dumpfile

if [[ $? -eq 0 ]]; then
	echo "El script finalizo exitosamente"
else
	echo "Error limpiando la base de datos"
	exit
fi