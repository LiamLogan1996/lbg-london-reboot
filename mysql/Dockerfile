FROM mcr.microsoft.com/mssql/server:2019-latest

COPY ./database-products.sql .

ENV MSSQL_SA_PASSWORD=Lloyds2022!
ENV ACCEPT_EULA=Y

ADD database-products.sql /docker-entrypoint-initdb.d
