FROM mcr.microsoft.com/mssql/server:2019-latest

ENV MSSQL_SA_PASSWORD=Lloyds2022!
ENV ACCEPT_EULA=Y

RUN mkdir -p /opt/mssql-scripts

COPY ./database-products.sql /opt/mssql-scripts


RUN ( /opt/mssql/bin/sqlservr --accept-eula & ) | grep -q "Service Broker manager has started" \
    && /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Lloyds2022!' -i /opt/mssql-scripts/database-products.sql \
    && pkill sqlservr


#This is how i got my image working locally. Pretty similar to yours

#FROM mcr.microsoft.com/mssql/server:2019-latest
#ENV ACCEPT_EULA=Y
#ENV SA_PASSWORD=Lloyds2022!
#ENV MSSQL_PID=Developer
#ENV MSSQL_TCP_PORT=1433
#WORKDIR /src
#COPY database.sql ./database.sql
#RUN (/opt/mssql/bin/sqlservr --accept-eula & ) | grep -q "Service Broker manager has started" &&  /opt/mssql-tools/bin/sqlcmd -S127.0.0.1 -U SA -P Lloyds2022! -i database.sql