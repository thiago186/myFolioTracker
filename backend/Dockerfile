# Usa a imagem oficial do PostgreSQL como base
FROM postgres:latest

# Copia scripts SQL para serem executados durante a inicialização do contêiner
COPY ./init-scripts/ /docker-entrypoint-initdb.d/

# Expõe a porta do PostgreSQL
EXPOSE 5432
