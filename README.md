# csv-to-json
Convert Csv to Json

### Pre requisites
- `git` protocol client installed
- Repository management client like `SourceTree` or something that helps in the `git` workflow
- Docker desktop

### Project checkout flow
Clone the entire repository on your local machine using the command

git clone https://github.com/dashrathdots/csv-to-json.git


Say the above is cloned out in a folder say `csv-to-json`.
Execute the following command to go in the checked out project folder

cd csv-to-json


Checkout to the Beginner branch

git checkout Beginner


Checkout to the Intermediate branch

git checkout Intermediate

After the above, open the `csv-to-json` folder in any IDE of your choice (preferable to use Visual Studio Code).
It has one folder
- csv-to-json: Holds the complete code
- csvtojson: The django based project. This project will read the csv file and create new json file according to nested data.


### Running the csv-to-json project

- Build the `development` version server docker image and run it using the following command
  ```
    sudo docker-compose -f docker-compose.yml up
  ```
- In order to see the start up logs execute the following command
  ```
    sudo docker-compose -f docker-compose.yml logs -f
  ```
- In order to get the server docker image details, execute the following command
  ```
    sudo docker ps

- The development docker image runs the django application using `python manage.py runserver`. So any change made in the project will auto redeploy it in the running docker image

## Setting up base master data
- Execute the below command to build the entire schema in your local postgresql database instance.
  ```
    sudo docker-compose -f docker-compose.yml exec csvtojson python manage.py migrate
  ```

## Backend admin panel access
- Create a superuser in order to login to the admin panel. Execute the following command. You can use the admin panel to modify/add data to the application
  ```
   sudo  docker-compose -f docker-compose.yml exec csvtojson python manage.py createsuperuser
  ```
- Hit the below url to get into the admin panel. Enter the username and password of the superuser that was created in the above step. The above created master data can be viewed and edited from the admin panel too.
  ```
    http://localhost:8000/admin

  ```

## Web access
- Hit the below url and upload the csv file to convert nested json .
```
http://127.0.0.1:8000/upload/csv

Once you upload the file, system will parse it and JSON file will be downloaded automatically in your browser
```

## Run Unit Test Case inside the docker
sudo  docker-compose -f docker-compose.yml exec csvtojson python manage.py test csvapp.tests.ConvertCsvToJsonTestCase.create_tree

Once you upload the file, system will parse it and JSON file will be downloaded automatically in your browser
```

## Run Unit Test Case
python manage.py test csvapp.tests.ConvertCsvToJsonTestCase.create_tree