# Forum-App---Blue-Team



## Mirco Services

Services Diagram: https://drive.google.com/file/d/1F0TJUsSgpBRfgQxqt7P9CZrsrrrTHWkZ/view?usp=sharing

### Gateway Service
The port for each service is specified in the config.py file. For example, according to the configuration below, the authentication service should use port 6000.

{"service_name": "authentication",
 "url": "http://127.0.0.1:6000/authentication/",
 "netloc": "127.0.0.1"
 }

Start the Gateway service (assuming it's running on http://127.0.0.1:5000) and the service you want to test (assuming it's the authentication service). Then you can use Postman to test the URL "http://127.0.0.1:5000/<service_name>)".
