#!/bin/bash
if [ -z $1 ]; then
	echo "Seleccione en cual aplicacion desea realizar la limpieza de base de datos"
	echo "   1) SPE"
	echo "   2) Empresas"
	printf "(1/2): "
	read ans
else
	ans=$1
fi

if [ $ans -eq "1" ]; then
	dbName=SPE
elif [ $ans -eq "2" ]; then
	dbName=Empresas
else
	echo "ERROR: Debe introducir 1 si desea limpiar SPE o 2 si desea limpiar Empresas"
	exit
fi
username=speclient
dbPasswd=spe2016

scriptDir=$(dirname -- "$(readlink -e -- "$BASH_SOURCE")")
cd "$scriptDir" && rm ../../applications/$dbName/databases/*

dbName=SPE
mysql -uroot -proot <<MYSQL_SCRIPT
DROP DATABASE $dbName;
CREATE DATABASE $dbName;
MYSQL_SCRIPT

if [[ $? -eq 0 ]]; then
	echo "El script finalizo exitosamente"
else
	echo "Error limpiando la base de datos"
	exit
fi