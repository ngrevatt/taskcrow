# taskcrow

## Testing Notes

Run `make mysql initmysql` to build and prepare mysql container. 

Run `make upcompose` to build and run containers.

Run `make tests` to run tests.

See `Makefile` for all `make` commands. 

## Project 3 Notes

User stories are [here](user_stories.md).

Run `make tests` to run tests.

Access web service at http://localhost:8000, experience service at http://localhost:8001, and models service at http://localhost:8002.

## Project 2 Notes
request to get a list of users:

    curl -X GET "http://localhost:8002/api/v1/user_profile/"

request to create a user:

    curl -X POST -F "first_name=john" -F "last_name=snow" -F "email=rad@gmail.edu" -F "username=jsnow" -F "phone_number=+5712747486" "http://localhost:8002/api/v1/user_profile/"

request to check that user was created:

    curl -X GET "http://localhost:8002/api/v1/user_profile/3/"

request to update an exisiting user:

    curl -X PUT -F "first_name=john" -F "last_name=snow" -F "email=rad@virginia.edu" -F "username=jsnow" -F "phone_number=+5712747486" "http://localhost:8002/api/v1/user_profile/3/"

request to delete an exisiting user:

    curl -X DELETE "http://localhost:8002/api/v1/user_profile/3/"

in order to work with other modesl, use the endpoints listed at:

    curl -X GET "http://localhost:8002/api/v1/"
