# bottle-auth-test
A test of basic authorization under Python's Bottle framework. This is being tested out for potential use in my other repo "Inky Wiki".

At the time of initial commit logging in, logging out, and persistent cookie based sessions are working.


To Do
---------
  - Add client side validation
  - Add actual server side validation beyond just sessions and passwords matching
  - Once the above are done: implement this as a component of Inky Wiki
  - Have is_logged_in work as a decorator (plugin?) in tandem with Bottle's route decorator


Dependencies
-------------------
To run you will need to install the following (everything is available through pip):
  - Python 2.7.x
  - Bottle

Additionally, the following items from the standard librbary are used:
    - os
    - hashlib
    - datetime
    - sqlite3
    
Deployment
-----------------------
Like Inky, this authorization and session system is intended for deployment on a Pirate Box. Inky also functions really well with Apache2 through WSGI, and so there is a potential use case there as well, though for that use case I will want to increase security and validation.
