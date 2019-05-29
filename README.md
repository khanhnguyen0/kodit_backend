# kodit_backend
This backend is currently being hosted at https://serene-thicket-22556.herokuapp.com/  
## Installation  
`
git clone git@github.com:midofit/kodit_backend.git  
`  
`
cd kodit_backend  
`  
Install dependencies  
`
pip install -r requirements.txt
`  
## Run the service:  
You can either run it by python (Flask), gunicorn, or Docker .
# Python  
`
python app.py
`  
# gunicorn
`
gunicorn app:app -bind 0.0.0.0:5000
`  
# Docker
Build the docker image  
`
docker build -t kodit_backend .   
`  
Run the container  
`
docker run -p 5000:5000 -e PORT=5000 kodit_backend
`  
The webapp will be served at http://localhost:5000
