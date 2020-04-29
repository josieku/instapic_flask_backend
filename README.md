# InstaPic Backend (Reap Coding Challenge)

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

## TO DOs ## 
Due to time constraints and my lack of experience with Flask, I have left out significant parts of the project.

- Performance optimization with image storage.  Images are now stored as base64 strings, which is not ideal.  I'd like to spend more time researching storing images as binary files or potentially even using a separate file system for enhanced performance.
- User specific functionality - profile, settings
- User interaction functionality - likes, bookmarks
- Clean up REST responses (to be consistent)
- Reach 100% test coverage (currently at 97%)
- More comments and documentation for greater degree of legibility

## Acknowledgements
Developed from [cosmic-byte's Flask Restplus Boilerplate](https://github.com/cosmic-byte/flask-restplus-boilerplate.git
).  
