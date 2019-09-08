 ## 1. Install virtual env
```bash
    pip install virtualenv
```
## 2. Create a virtual environment
```bash
    virtualenv flask_api_app
```

## 3. Activate the virtual env
```bash
    source flask_api_app/bin/activate
```
```bash
    #To deactivate the environment use
    deactivate
```
## 4. Copy the files to the project folder
## 5. Install the packages from requirements.txt file
```bash
    pip install -r requirements.txt
    # This will install Flask, Flask-Restfull, Gunicorn and Json packages to the environment
```
## 6. Run Gunicorn by going from the project folder
```bash
   # First know how make cores you have using
   
   nproc -all
   4
   # Number of workers will be (2 *number of cores ) + 1 
   
   # start the Gunicorn
   
   gunicorn -w 9 api:app
   # api: is the our main file and the app is the flask app we want to run in that file.

   #By default guniocorn runs at 127.0.0.1:8000
   #Note the port number down i.e 8000

```
## 7. Install ngrok in your system
## 8. Run ngrok specifing the port 8000 to look to.
```bash
   ./ngrok http 8000

   # copy the address provided by ngrok to your server.
```
## 9. Go to any browser and paste the address
```
    http:somthiung.ngrok.io\countryname
```
```
   It should return following json data:
   if country is valid
   {
       'country':'India',
       'capital':'New Delhi',
   }
   else
   {
       'country':'India',
       'capital':'Not Found',
   }
```