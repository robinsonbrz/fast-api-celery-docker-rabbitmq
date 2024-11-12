# !/bin/bash
docker exec -it db psql -U postgres -c "CREATE DATABASE fastapirob;"
docker exec -it db psql -U postgres -c "CREATE DATABASE fastapirob_teste;"
# docker exec -it db psql -U postgres -c "DROP DATABASE fastapirob;"
# docker exec -it db psql -U postgres -c "DROP DATABASE fastapirob_teste;"1