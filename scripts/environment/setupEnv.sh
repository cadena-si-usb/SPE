#!/bin/bash
# setupEnv.sh
# Este script prepara el entorno de desarrollo para la aplicacion de SPE

# Chequeando que la distribucion de linux instalada este basada en debian
/usr/bin/rpm -q -f /usr/bin/rpm >/dev/null 2>&1
if [[ $? -eq $zero ]]; then
	echo "--------------------------------------------------------------"
	echo "Su version de Linux instalada no es soportada por este script"
	echo "--------------------------------------------------------------"
	exit
else
	echo "---------------------------------------------------------------"
	echo "Su version de linux es compatible con el script de instalacion"
	echo "---------------------------------------------------------------"
fi

# Instalando dependencias para usar el cas
echo "Instalando dependencias"
echo "---------------------------------------------------------------"
sudo apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev ldap-utils python-tk
echo "Instalando ambiente virtual"
echo "---------------------------------------------------------------"
cd ../../
rm -rf env
virtualenv -p python env
env/bin/pip install -r requirements.txt

if [[ $? -ne $zero ]]; then
	echo "No se instalaron las dependencias correctamente. Abortando instalacion"
	exit
fi

# Verificando que el servidor este instalado previamente
dpkg-query -s postgresql > /dev/null 2>&1
if [[ $? -eq 0 ]]; then
	echo "Servidor PostgreSQL previamente instalado, saltando este paso"
	echo "---------------------------------------------------------------"

else
	echo "Instalando servidor de PostgreSQL"
	echo "---------------------------------------------------------------"

	# Instala el servidor de PostgreSQL en Debian/Ubuntu
	sudo apt-get -y install postgresql
fi

PGPASSWORD=postgres

username=speclient
dbName=SPE
dbPasswd=spe2016


sudo -u postgres psql postgres << EOF
CREATE USER speclient WITH PASSWORD 'spe2016';
CREATE SCHEMA IF NOT EXISTS spe;
CREATE DATABASE SPE OWNER speclient;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA spe TO speclient;
GRANT ALL PRIVILEGES ON DATABASE SPE TO speclient;
EOF

echo "Cuentas habilitadas:"
echo "------------------------------"
echo "   - Username: postgres"
echo "     Password: postgres"
echo "------------------------------"
echo "   - Username: speclient"
echo "     Password: spe2016"
echo "---------------------------------------------------------------"
echo "Configurando Base de datos SPE:"


echo "La base de datos fue configurada exitosamentes"
echo "---------------------------------------------------------------"

echo "Iniciando la migracion de sqlite a MySQL"
echo "Ejecute el siguiente comando en la carpeta de su web2py: "
echo "python web2py.py -S SPE -M –P"
echo "luego presione cualquier tecla:"
read ans

echo "La migracion fue completada exitosamente. De presentarse una falla, mandar"
echo "captura de pantalla con el error de la consola a hectoragoncalvesp@gmail.com"
echo "---------------------------------------------------------------"
#mysql -u speclient SPE -pspe2016 < mysql_dump.sql
