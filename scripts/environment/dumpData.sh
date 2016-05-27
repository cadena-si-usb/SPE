#!/bin/bash
# dumpData.sh
# Crea el archivo spe_dump.sql con la data de la base de datos SPE
echo "---------------------------------------------------------------"
mysqldump -u speclient -pspe2016 SPE > spe_dump.sql

if [[ $? -eq 0 ]]; then
	echo "El script finalizo exitosamente"
else
	echo "Error dumpeando la base de datos"
	exit
fi

