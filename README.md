# Projeto Docker para Backup do PostGreSql e enviar para S3 #

![](https://img.shields.io/badge/Python-3.6-blue.svg)

Esse projeto faz o backup de uma base de dados PostGreSQL e envia para um Bucket no AWS S3


### Arquivo .env ###

Renomear o arquivo .env_sample ou criar um outro arquivo .env com estrutura

```
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
PG_HOST=''
PG_PORT=''
PG_DATABASE=''
PG_USER=''
PG_PWD=''

``` 

### Como rodar ? ###

- Configure um arquivo .env
- execute o comando:

```
docker-compose up --force-recreate --build db-bkp-postgres
```

### Docker Network - se for rodar na mesma rede ###

Verifique se o seu banco Postgres está na mesma rede (network) do Docker.

```
networks:
  backend:
    external:
      name: backend
```


### Criar um Cron ###

Se executar o processo pelo CRON do Linux:

```
crontab -e
```

Colocar a linha de execução do .sh com os horários que deseja

No exemplo abaixo, executa o backup a cada 12 (doze) horas, diariamente:

```
0 */12 * * * /bin/bash /pasta-onde/estará-o-.sh/start-backup-via-cron.sh
```