# Imagine

## Installing
This is project based on python. In order to run this project, you need following libraries:

1. Flask
2. Numpy
3. dlib
4. pyodbc
5. pyrebase
6. opencv-python
7. json
8. passlib

Or: 
you can use yml file to recreate the conda environment with library version that dev has bee used during developing.

## Developing

### Flask

In flask, there are folder specific folder for components:
    1. templates: All html files or your website's pages will be saved within this folder
    2. static: Static folders such as: Javascript, Css, Image or Font are located in this folder. I already separated them in to folders that correspond to their name like js, css, images and font accordingly.

Creating Page:
    After you have created the new website page and want it to be accessible in URL, you will have to create function inside `main.py` and add it to application's route.

For example, I have created a page called newPage.html and want to add it to website. 
    First parameter inside @app.route is url path so if I want to call this function from url dict. 
    The second parameter is optional, it is used to specify method that this route allows to make access.

At the end, you will have to return with render_template which is equivalence to return View() in .net core, and inside it will be string which is the same as html file that you want to show. Moreover, you can pass the model or data to view pass well with the following code

```
@app.route('/newPage', methods=['GET', 'POST']):
    data = {
        ..... json format .....
    }

    return render_template('newPage.html', model=data)
```

At some point, you may need to use flash message and you can call it with simple `flash`. I have already created the class called flash, you can use it like this

```
@app.route('/newPage', methods=['GET', 'POST']):
    flash.success('Message') # parameter is message that you want to show

    return render_template('newPage.html')
```

However, I do recommend you to add new message to messages.py file, so you can simple call it with `messages.{name of message}` like this

@app.route('/newPage', methods=['GET', 'POST']):
    flash.success(message.something)

    return render_template('newPage.html')
```

### Jinjar

Jinjar is template language that allow you to add programming logic to your html code, just like razor in .net core

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

If you want to add new html page, you will have to put content block to import required js, css and header to your page

````
{% set title = 'Page Name' %}   <-- Add page name over here
{% extends "shared/_layout.html" %}
{% block content %}

html body

{% endblock %}
```

