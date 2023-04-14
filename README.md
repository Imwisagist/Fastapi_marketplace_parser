# Test_for_a_retail_company
### Clone project and enter in the infra folder:
```bash
git clone https://github.com/Imwisagist/Test_for_a_retail_company.git && cd Test_for_a_retail_company/infra
```
### Create a .env file in infra folder and input database config variables:
```bash
nano .env
# Example
DB_HOST=db
DB_PORT=5432
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```
### Run docker-compose:
```bash
docker-compose up -d
```
### Apply migrations:
```bash
winpty docker exec -it fastapi_backend bash -c "alembic upgrade head"
```
### Open your browser:
Open [http://127.0.0.1:8010/docs](http://127.0.0.1:8010/docs) to view it in your browser.
### What does the terms of reference look like:
![screenshot](https://github.com/imwisagist/Test_for_a_retail_company/blob/main/other/Task.jpg?raw=true)