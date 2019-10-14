# flask-on-nginx-docker    
Sample Flask application running on nginx and wsgi in a Docker container    
To build the container:    
sudo docker build . -t flask-on-nginx-docker     
To run the container:     
sudo docker run -d --name flask-on-nginx-docker -p 80:80  flask-on-nginx-docker   


