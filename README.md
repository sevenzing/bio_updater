Time bio auto updater
===

## What does it do?
1. Update your bio every minute and set **current time** in words **in russian**:

    ![](media/example.png)


2. Does not make you online always

## How to install?

1. You need your telegram `api_id` and `api_hash`. 
    
    + Create your telegram app [here](https://my.telegram.org/apps)
    + Copy hash and id: 
    ![](media/my_telegram.png)
    + Do not share it to anyone!

2. Paste your cridentials in `cridentials.py`:
```python
credentials = {    
    'api_id': <api_id>,
    'api_hash': '<api_hash>',
    'session': 'account0.session'   
}
```
3. Build docker

```console
$ docker-compose build
```

4. Create session file (you need to do it only once)
```console
$ docker-compose run session_creator
Creating status_auto_update_session_creator_run ... done
Please enter your phone (or bot token): <your telephone>
Please enter the code you received: <code you received>
Please enter your password: <your password>
Signed in successfully as Lev Lymarenko
```

You can notice that file `sessions/account0.session` has been created. Using this file **everyone** can access your account. Do not share to anyone either!

5. Run the poliing script using docker:

```console
$ docker-compose up -d updater
```
