FROM mcr.microsoft.com/mssql/server:2019-latest

ENV MSSQL_SA_PASSWORD=Lloyds2022!
ENV ACCEPT_EULA=Y

RUN mkdir -p /opt/mssql-scripts

COPY ./database-products.sql /opt/mssql-scripts


RUN ( /opt/mssql/bin/sqlservr --accept-eula & ) | grep -q "Service Broker manager has started" \
    && /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Lloyds2022!' -i /opt/mssql-scripts/database-products.sql \
    && pkill sqlservr

