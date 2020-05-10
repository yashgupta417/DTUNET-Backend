# DTUNET-Backend
Base Url:http://dtunet.pythonanywhere.com/api/

*Login API
Url endpoint:http://dtunet.pythonanywhere.com/api/login/
HTTP method:POST
Request Body:{
	      "email":"example@gmail.com",
	      "password":"12345678"
             }

Response:{
          "token": "19e56449311b1c41d5c1e1be8adc27e64a5ffbab"
         }

*SignUp API
Url endpoint:http://dtunet.pythonanywhere.com/api/signup/
HTTP method:POST
Required fields=['email','password','name']
Request Body:{
    	      "password": "123456789",            
    	      "name": "Yash",
    	      "email": "test55@gmail.com",
    	      "image": "example\imageurl.com",
    	      "label": "Student",
    	      "bio": "DTU 2nd year",
             }

Response:{
    	"u_id": "5ca30691-9234-4a24-a90d-5e6258ab8d10",
    	"name": "Yash",
    	"email": "test55@gmail.com",
    	"image": "example\imageurl.com",
    	"label": "Student",
    	"bio": "DTU 2nd year",
	"is_online": false
	}

*User Detail API
URL endpoint:http://dtunet.pythonanywhere.com/api/user_detail/{u_id}/
	     eg: http://dtunet.pythonanywhere.com/api/user_detail/df2dbab8bd824adeaec438b214686802/
HTTP method:GET
Request Header:{
		"Authorization":"Token {user token}"
	       }
Response:{
    	"u_id": "5ca30691-9234-4a24-a90d-5e6258ab8d10",
    	"name": "Yash",
    	"email": "test55@gmail.com",
    	"image": "example\imageurl.com",
    	"label": "Student",
    	"bio": "DTU 2nd year",
	"is_online": false
	}

		


