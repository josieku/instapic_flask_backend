# InstaPic Backend (Reap Backend Coding Challenge)

This is a Flask REST backend for a photo sharing platform, InstaPic.  

## Terminal commands

Initial installation (after setting up virtual environment): `make install`

To run test and see coverage: `make coverage`

To run application: `make run`

To run all commands at once : `make all`


## Running and viewing the app locally ##

Once you run `make run` in the terminal, you can open the following url on your browser to view swagger documentation
http://127.0.0.1:5000/


## Using Postman ##

Authorization header is in the following format:
```
Key: Authorization
Value: "token_generated_during_login"
```
Most routes require this token.

## To Dos ## 
Due to time constraints and my lack of experience with Flask, I have left out significant parts of the project.

- User specific functionality - profile, settings
- User interaction functionality - likes, bookmarks
- Clean up REST responses (to be consistent)
- Reach 100% test coverage (currently at 97%)
- More comments and documentation for greater degree of legibility


## Acknowledgements
Developed from [cosmic-byte's Flask Restplus Boilerplate](https://github.com/cosmic-byte/flask-restplus-boilerplate.git
).  
