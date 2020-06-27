echo "Iniciando Backup"

folder="/"
file_prefix="$(/bin/date '+%Y%m%d_%H%M%S')_"
file_suffix=".sql"

PG_PORT=$(grep PG_PORT .env | cut -d '=' -f2)
PG_DATABASE=$(grep PG_DATABASE .env | cut -d '=' -f2)
PG_HOST=$(grep PG_HOST .env | cut -d '=' -f2)
PG_USER=$(grep PG_USER .env | cut -d '=' -f2)
PG_PWD=$(grep PG_PWD .env | cut -d '=' -f2)

db_name=$PG_DATABASE
host=$PG_HOST
db_user=$PG_USER

PGPASSWORD="$PG_PWD" pg_dump -h ${host} -p $PG_PORT -U $db_user $db_name > ${file_prefix}${db_name}${file_suffix}

gzip ${file_prefix}${db_name}${file_suffix}

rm -f ${file_prefix}${db_name}${file_suffix}

echo "## INICIANDO ENVIO PARA S3"
echo ""

python3 backup.py "${file_prefix}${db_name}${file_suffix}.gz"


echo "## ENVIADO ARQUIVO PARA S3"
echo ""
echo "## APAGANDO ARQUIVO LOCAL"

rm -f ${file_prefix}${db_name}${file_suffix}.gz

echo ""
echo "## FINISHED"