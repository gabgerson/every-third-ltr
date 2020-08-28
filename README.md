# Every Third Letter

## Tech Stack

Flask, Python


## Features
Make a new string from every third letter of input string 

This application, "Accepts a POST request to the route “/test”, which accepts one argument “string_to_cut” 
Returns a JSON object with the key “return_string” and a string containing every third letter from the original string
(e.g.) If you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}." https://boards.greenhouse.io/lyft/jobs/4691551002

![example of working curl post request](https://user-images.githubusercontent.com/49376684/88744309-d066fb00-d0fb-11ea-99c3-44d93d520fad.jpg)




## Run Every Third Letter Locally

### Requirements

* Python 3.6


__Clone Repository:__
```
$ git clone https://github.com/gabgerson/every-third-ltr
```
__Create virtual environment:__

```
$ virtualenv env
```
__Activate virtual environment:__

```
$ source env/bin/activate
```

__Install dependencies:__

```
$ pip install -r requirements.txt
```

__Run the app:__

```
$ python server.py
```

__Run the following command:__

```
$ curl -X POST http://0.0.0.0:5000/test  --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
```
The following should be returned {"return_string": "muydv"}. The string can be changed in the json object '{"string_to_cut": "YourStringHere"}'

## About the developer

Learn more here [LinkedIn](https://www.linkedin.com/in/gabriela-gerson)
