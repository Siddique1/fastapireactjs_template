#Basic user in FastAPI API backend interface and CRUD functionalities.
This repo is running basic user model in postgresql on api interface and successfully check CRUD commands on api endpoint.
###The following steps were done as mentioned with this commit.
1. This command  ```alembic init -t async alembic``` is used to generate async verson of alembic for sqlalchemy migration to database.
2. Generated **env.py** due to above command is modified to work with database_url for for my own setting of local server.
3. 



> [!CAUTION]
> This is dev version. Use at your own risk.


## Task list
- [x] basic user (only user table) with CRUD operation in local PC development. Tested on document interface http://localhost:8000/docs#/. The password is plain text not yet hash implemented.
- [ ] Role Based Access Control (RBAC) functionality in user model and decide whatever table to add. This is also local dev server. Also ensure database password hashed.
- [ ] Basic reactjs based frontend to run on local PC and send/receive user data to fastapi backend server.
- [ ] Docker based implementation.
- [ ] plan and implement a product database table(s) and connection and implement it.