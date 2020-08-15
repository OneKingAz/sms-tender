<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <style>
            #logout {
                display: inline-block;
                position: fixed;
                top: 10px;
                right: 25px;
            }
        </style>
    </head>
    <body>
        <h1>{{username}}</h1>
        <p>You made it to the secure section!!</p>
        <span id="logout"><a href="/logout">Log Out</a></span>
    </body>
</html>
