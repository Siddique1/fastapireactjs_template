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
- [x] Role Based Access Control (RBAC) functionality in user model implemented by adding two more tables. One table roles which tally id(PK) autoincrement with it's description explaining it's role and access. Second table user_roles which record which user_id have which role_id. 
- [x] JWT token mechanism is added. A login end point is also added to verify JWT token functionality and future login for front-end.
- [ ] Basic reactjs based frontend to run on local PC and send/receive user data to fastapi backend server.
- [ ] Docker based implementation.
- [ ] plan and implement a product database table(s) and connection and implement it.