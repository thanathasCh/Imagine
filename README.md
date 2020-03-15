# Imagine

## Installing
This is project based on python. In order to run this project, you need following libraries:

1. Flask
2. Numpy
3. More will come

## Developing

### Flask

In flask, there are folder specific folder for components:
    1. templates: All html files or your website's pages will be saved within this folder
    2. statuc: Static folders such as: Javascript, Css, Image or Font are located in this folder. I already seperated them in to folders that corresspond to their name like js, css, images and font accordingly.

Creating Page:
    After you have craeted the new website page and want it to be accessable in URL, you will have to create function inside `main.py` and add it to application's route.

For example, I have created a page called newPage.html and want to add it to website. 
    First parameter inside @app.route is url path so if I want to call this function from url dict. 
    The second parameter is optional, it is used to specify method that this route allows to make access.

    At the end, youu will have to return with render_template which is equivalence to return View() in .net core, and inside it will be string which is the same as html file that you want to show. Moreover, you can pass the model or data to view passs well with the following code

    ```
    @app.route('/newPage', methods=['GET', 'POST']):
        data = {
            ..... json format .....
        }

        return render_template('newPage.html', model=data)
    ```

    At some point, you may need to use flash message and you can call it with simple `flash()`, where the first parameter is the message and the second one is type of message which will be shown to different color.

    ```
    @app.route('/newPage', methods=['GET', 'POST']):
        flash('message', 'type') # types: info, danger, warning, success

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

If you want to add new html page, you will have to put content block to import requried js, css and header to yuor page

````
{% set title = 'Page Name' %}   <-- Add page name over here
{% extends "shared/layout.html" %}
{% block content %}

html body

{% endblock %}
```

