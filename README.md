# voice-diary
## Database setup

To setup the database for use, add a user named `python_user` and give it the password `Python!`. Make sure that it has permissions to create and edit databases, then execute the following in your command line.

<!-- Help with this command from https://stackoverflow.com/a/16228713-->
```zsh
mysql -u python_user --password="Python\!" < database_creation.sql
```
