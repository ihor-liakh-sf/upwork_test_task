Project setup instructions:
====================
There are 2 ways to run the project:
1. Inside Docker container:  
   Follow these steps:   
      * Inside root directory run `make start`
      * The project will be available at http://0.0.0.0:8000, test page is on http://0.0.0.0:8000/hello-world
    
   _Other Makefile commands:_  
   * `make test` - run tests
   * `make migrate` - run migration
   * `make logs` - show logs
   * `make fixtures` - load fixtures

2. Using machine Python interpreter through some virtual environment tool.  
   Follow these steps:
      * Install required packages from `./requirements.txt`
      * Inside `hello_world` directory run:   
        `python manage.py migrate`   
        _(Optionally) load init data fixtures `python manage.py loaddata hello_world`_ 
        `python manage.py runserver`  
      * The project will be available at http://0.0.0.0:8000, test page is on http://0.0.0.0:8000/hello-world   
