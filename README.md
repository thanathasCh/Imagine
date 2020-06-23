# Imagine
This is web application project from Flask that I did for my term project in Intelligence System Development class.
The application of this program is searching the images that have you in it by the given images of yourself.

It also allows organizers to create, edit, and delete the event.

## Installing
This is a project based on python. In order to run this project, you need the following libraries:

1. Flask
2. Numpy
3. dlib
4. pyodbc
5. pyrebase
6. opencv-python
7. json
8. passlib

Or: 
you can use yml file to recreate the conda environment with the library version that dev has bee used during development.

## Developing

### Flask

In flask, there are folder specific folders for components:
    1. templates: All HTML files or your website's pages will be saved within this folder
    2. static: Static folders such as Javascript, CSS, Image, or Font are located in this folder. 
    I already separated them into folders that correspond to their names like JS, CSS, images, and font accordingly.

Creating Page:
    After you have created the new website page and want it to be accessible in URL, you will have to 
    
    create function inside `main.py` and add it to the application's route.

For example, I have created a page called newPage.html and want to add it to the website. 
    The first parameter inside @app.route is URL path so if I want to call this function from URL dict. 
    The second parameter is optional, it is used to specify method that this route allows making access.

In the end, you will have to return with render_template which is equivalence to return View() in .net core,
 and inside it will be string which is the same as HTML file that you want to show. Moreover, 
 you can pass the model or data to view pass well with the following code

```
@app.route('/newPage', methods=['GET', 'POST']):
    data = {
        ..... json format .....
    }

    return render_template('newPage.html', model=data)
```

At some point, you may need to use flash message and you can call it with simple `flash`. 
I have already created the class called flash, you can use it like this

```
@app.route('/newPage', methods=['GET', 'POST']):
    flash.success('Message') # parameter is message that you want to show

    return render_template('newPage.html')
```

However, I do recommend you to add new message to messages.py file, so you can simply call it 
with `messages.{name of message}` like this

```
@app.route('/newPage', methods=['GET', 'POST']):
    flash.success(message.something)

    return render_template('newPage.html')
```

### Jinjar

Jinjar is template language that allows you to add programming logic to your HTML code, 
just like razor in .net core

Most used jinja
1. variable block

```
{{ value }}
```

2. if else block

```
{% if _expression_ %}
    code
{% else %}
    code for else
{% endif %}
```

3. for loop block

```
{% for _ in _ %}
    code
{% endfor %}
```

### Html

If you want to add new HTML page, you will have to put a content block to import required JS, 
CSS and header to your page

```
{% set title = 'Page Name' %}   <-- Add page name over here
{% extends "shared/_layout.html" %}
{% block content %}

html body

{% endblock %}
```

### Screenshots and Explanations

The following sections will be the explanation of the program and processes.

The program's flow will start by adding an event. This is the process that only the organizer can do. 
Organizers is like admin who can add, edit and delete the events.

![Organizer's View]()

After every information has been filled including the event's images. The program will read those 
information and add them to the SQL database. However, I chose to keep the images on Cloud Storage 
like Firebase instead. Next, the program will transform all images into 128-D array for face comparison. 
The process contains 
Detecting faces in each image
Put them into face embedding model from dlib
Save into SQL database as char sequence
I did all of this to reduce the computation time and power when the user comes and searches for their images. 
Without these preparations, the server side will have to do the same redundant tasks every time one user 
requests.

![Adding page]()

After the event has been created, users will be able to see all events and images inside. 
User can click on a specific image to enhance it. And when the user wants to find him/herself over 
every image, he/she can click on the `find yourself` button.

![event detail]()

![modal]()

The program will show another page, where it requests user the images with clear frontal face. 
User can either choose to take photos through their webcam or images from their machine. 
User can choose the similarity value as well. Higher the similarity value will decrease the fault 
positive, but could return less images. While lower the similarity value might increase the number 
of returned images, but higher the fault positive images.

![select image page]()

![return image]()