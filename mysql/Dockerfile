FROM mcr.microsoft.com/mssql/server:2019-latest

COPY ./database_products.sql .

ENV MSSQL_SA_PASSWORD=root
ENV ACCEPT_EULA=Y

RUN sqlcmd -i database_products.sql 

