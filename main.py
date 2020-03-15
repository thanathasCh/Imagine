from flask import Flask, request, render_template, url_for, flash
import numpy as np

app = Flask('Imagine')

'''
    flash('text', 'type')

    types: info, danger, warning, success
'''

@app.route('/')
def index():
    return render_template('main.html')

# Login Page
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'admin':
        flash('Login Successfullly.', 'success')
    else:
        flash('Login Failed: Incorrect Username or password.', 'danger')
    
    return render_template('main.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signCheck', methods=['POST'])
def signCheck():
    username = request.form['username']
    password = request.form['password']
    firstName = request.form['firstName']
    lastName = request.form['lastName']

    flash('Sign in successfully.', 'success')
    return render_template('main.html')
    
# end

# Event Page
@app.route('/event')
def event():
    events = [
                {
                    'id': 1,
                    'eventName': 'Au Freshy Day and Night',
                    'imageUrl': 'https://www.abactoday.com/wp-content/uploads/2015/08/uc59282e7be59f20b867d53511131956f-1_14401580346861.jpg',
                    'description': 'Bla Bla Bla Bla'
                },
                {
                    'id': 2,
                    'eventName': 'Au Freshy Day and Night',
                    'imageUrl': 'https://www.abactoday.com/wp-content/uploads/2015/08/uc59282e7be59f20b867d53511131956f-1_14401580346861.jpg',
                    'description': 'Bla Bla Bla Bla'
                },
                {
                    'id': 3,
                    'eventName': 'Au Freshy Day and Night',
                    'imageUrl': 'https://www.abactoday.com/wp-content/uploads/2015/08/uc59282e7be59f20b867d53511131956f-1_14401580346861.jpg',
                    'description': 'Bla Bla Bla Bla'
                }
            ]
            
    return render_template('event.html', events=events)

@app.route('/addEvent')
def addEvent():
    return render_template('addevent.html')

@app.route('/addEventSubmit', methods=['POST'])
def addEventSubmit():
    # if request.method == 'POST':
    #     # name = request.form['eventname']
    #     # description = request.form['description']
    #     # date = request.form['date']
    #     # images = request.files['eventImages']
    #     print(request.files)
    #     if request.files:
    #         print(request.files['eventImages'])
    #         return 'done'
    #     return('halfly done')
    events = [
                {
                    'id': 1,
                    'eventName': 'Au Freshy Day and Night',
                    'imageUrl': 'https://www.abactoday.com/wp-content/uploads/2015/08/uc59282e7be59f20b867d53511131956f-1_14401580346861.jpg',
                    'description': 'Bla Bla Bla Bla'
                },
                {
                    'id': 2,
                    'eventName': 'Au Freshy Day and Night',
                    'imageUrl': 'https://www.abactoday.com/wp-content/uploads/2015/08/uc59282e7be59f20b867d53511131956f-1_14401580346861.jpg',
                    'description': 'Bla Bla Bla Bla'
                },
                {
                    'id': 3,
                    'eventName': 'Au Freshy Day and Night',
                    'imageUrl': 'https://www.abactoday.com/wp-content/uploads/2015/08/uc59282e7be59f20b867d53511131956f-1_14401580346861.jpg',
                    'description': 'Bla Bla Bla Bla'
                }
            ]

    flash('Add Event Successfully', 'info')
    return render_template('event.html', events=events)

    return 'undone'
    # return render_template('event.html')

@app.route('/eventDetail/<int:id>')
def eventDetail(id):
    model = {
        'id': id,
        'name': 'Freshy day and night',
        'date': '12/12/2020',
        'images': [
            'https://scontent.fbkk2-6.fna.fbcdn.net/v/t31.0-0/c58.0.200.200a/p200x200/14425558_1025835850848219_1733950060278712461_o.jpg?_nc_cat=104&_nc_sid=cdbe9c&_nc_ohc=1uzMmTIv1dYAX_HJv0q&_nc_ht=scontent.fbkk2-6.fna&oh=910587ad77ac4f0f67a1c9d37c393fab&oe=5E8E9FEE',
            'https://scontent.fbkk2-5.fna.fbcdn.net/v/t31.0-0/c36.0.200.200a/p200x200/14352140_1025835940848210_772111150301797504_o.jpg?_nc_cat=110&_nc_sid=cdbe9c&_nc_ohc=iMtyoOKE7O4AX8Pb83G&_nc_ht=scontent.fbkk2-5.fna&oh=570db0a836fc51be5761b254b888ff24&oe=5E9974F6',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c53.0.200.200a/p200x200/14362449_1025836140848190_5441216761723762681_o.jpg?_nc_cat=106&_nc_sid=cdbe9c&_nc_ohc=4tTPsFxsiFoAX_K4F3c&_nc_ht=scontent.fbkk2-7.fna&oh=f6276eed5e6f88b9bb15e7722d33470f&oe=5E91166A',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c100.0.200.200a/p200x200/14445218_1025836430848161_3342879240495006392_o.jpg?_nc_cat=106&_nc_sid=cdbe9c&_nc_ohc=2MMU8VpRa58AX_jF8n-&_nc_ht=scontent.fbkk2-7.fna&oh=2fd00c3870a5571e1ed6d6372038682e&oe=5E95536C',
            'https://www.abactoday.com/wp-content/uploads/2015/08/uc59282e7be59f20b867d53511131956f-1_14401580346861.jpg',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c54.0.200.200a/p200x200/14444641_1025836984181439_8808349409796662954_o.jpg?_nc_cat=108&_nc_sid=cdbe9c&_nc_ohc=6RNd8EOKz9oAX9WEO7h&_nc_ht=scontent.fbkk2-7.fna&oh=d976a23382f8ad02b631b7b915236356&oe=5E98E9330',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c49.0.200.200a/p200x200/14424727_1025837387514732_1358339369238814549_o.jpg?_nc_cat=105&_nc_sid=cdbe9c&_nc_ohc=m5t7Z9A-NSMAX9DzxQJ&_nc_ht=scontent.fbkk2-8.fna&oh=aaf13cfe09a0f900b1c184d19d7a45c9&oe=5E929318',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c55.0.200.200a/p200x200/14445159_1025837907514680_4422708166650316924_o.jpg?_nc_cat=103&_nc_sid=cdbe9c&_nc_ohc=3glQMk78DzcAX82gVVk&_nc_ht=scontent.fbkk2-8.fna&oh=f3ae744501055d57389dd851ee611bd9&oe=5E9323D8',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c53.0.200.200a/p200x200/14444806_1025838224181315_1956270792039579357_o.jpg?_nc_cat=102&_nc_sid=cdbe9c&_nc_ohc=sBRDvizddZcAX9FxMs4&_nc_ht=scontent.fbkk2-8.fna&oh=51fc6dcab2436f4d881024e50b209cec&oe=5E99498F',
            'https://scontent.fbkk2-6.fna.fbcdn.net/v/t31.0-0/c58.0.200.200a/p200x200/14425558_1025835850848219_1733950060278712461_o.jpg?_nc_cat=104&_nc_sid=cdbe9c&_nc_ohc=1uzMmTIv1dYAX_HJv0q&_nc_ht=scontent.fbkk2-6.fna&oh=910587ad77ac4f0f67a1c9d37c393fab&oe=5E8E9FEE',
            'https://scontent.fbkk2-5.fna.fbcdn.net/v/t31.0-0/c36.0.200.200a/p200x200/14352140_1025835940848210_772111150301797504_o.jpg?_nc_cat=110&_nc_sid=cdbe9c&_nc_ohc=iMtyoOKE7O4AX8Pb83G&_nc_ht=scontent.fbkk2-5.fna&oh=570db0a836fc51be5761b254b888ff24&oe=5E9974F6',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c53.0.200.200a/p200x200/14362449_1025836140848190_5441216761723762681_o.jpg?_nc_cat=106&_nc_sid=cdbe9c&_nc_ohc=4tTPsFxsiFoAX_K4F3c&_nc_ht=scontent.fbkk2-7.fna&oh=f6276eed5e6f88b9bb15e7722d33470f&oe=5E91166A',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c100.0.200.200a/p200x200/14445218_1025836430848161_3342879240495006392_o.jpg?_nc_cat=106&_nc_sid=cdbe9c&_nc_ohc=2MMU8VpRa58AX_jF8n-&_nc_ht=scontent.fbkk2-7.fna&oh=2fd00c3870a5571e1ed6d6372038682e&oe=5E95536C',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c54.0.200.200a/p200x200/14444641_1025836984181439_8808349409796662954_o.jpg?_nc_cat=108&_nc_sid=cdbe9c&_nc_ohc=6RNd8EOKz9oAX9WEO7h&_nc_ht=scontent.fbkk2-7.fna&oh=d976a23382f8ad02b631b7b915236356&oe=5E98E9330',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c49.0.200.200a/p200x200/14424727_1025837387514732_1358339369238814549_o.jpg?_nc_cat=105&_nc_sid=cdbe9c&_nc_ohc=m5t7Z9A-NSMAX9DzxQJ&_nc_ht=scontent.fbkk2-8.fna&oh=aaf13cfe09a0f900b1c184d19d7a45c9&oe=5E929318',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c55.0.200.200a/p200x200/14445159_1025837907514680_4422708166650316924_o.jpg?_nc_cat=103&_nc_sid=cdbe9c&_nc_ohc=3glQMk78DzcAX82gVVk&_nc_ht=scontent.fbkk2-8.fna&oh=f3ae744501055d57389dd851ee611bd9&oe=5E9323D8',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c53.0.200.200a/p200x200/14444806_1025838224181315_1956270792039579357_o.jpg?_nc_cat=102&_nc_sid=cdbe9c&_nc_ohc=sBRDvizddZcAX9FxMs4&_nc_ht=scontent.fbkk2-8.fna&oh=51fc6dcab2436f4d881024e50b209cec&oe=5E99498F',
            'https://scontent.fbkk2-6.fna.fbcdn.net/v/t31.0-0/c58.0.200.200a/p200x200/14425558_1025835850848219_1733950060278712461_o.jpg?_nc_cat=104&_nc_sid=cdbe9c&_nc_ohc=1uzMmTIv1dYAX_HJv0q&_nc_ht=scontent.fbkk2-6.fna&oh=910587ad77ac4f0f67a1c9d37c393fab&oe=5E8E9FEE',
            'https://scontent.fbkk2-5.fna.fbcdn.net/v/t31.0-0/c36.0.200.200a/p200x200/14352140_1025835940848210_772111150301797504_o.jpg?_nc_cat=110&_nc_sid=cdbe9c&_nc_ohc=iMtyoOKE7O4AX8Pb83G&_nc_ht=scontent.fbkk2-5.fna&oh=570db0a836fc51be5761b254b888ff24&oe=5E9974F6',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c53.0.200.200a/p200x200/14362449_1025836140848190_5441216761723762681_o.jpg?_nc_cat=106&_nc_sid=cdbe9c&_nc_ohc=4tTPsFxsiFoAX_K4F3c&_nc_ht=scontent.fbkk2-7.fna&oh=f6276eed5e6f88b9bb15e7722d33470f&oe=5E91166A',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c100.0.200.200a/p200x200/14445218_1025836430848161_3342879240495006392_o.jpg?_nc_cat=106&_nc_sid=cdbe9c&_nc_ohc=2MMU8VpRa58AX_jF8n-&_nc_ht=scontent.fbkk2-7.fna&oh=2fd00c3870a5571e1ed6d6372038682e&oe=5E95536C',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c54.0.200.200a/p200x200/14444641_1025836984181439_8808349409796662954_o.jpg?_nc_cat=108&_nc_sid=cdbe9c&_nc_ohc=6RNd8EOKz9oAX9WEO7h&_nc_ht=scontent.fbkk2-7.fna&oh=d976a23382f8ad02b631b7b915236356&oe=5E98E9330',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c49.0.200.200a/p200x200/14424727_1025837387514732_1358339369238814549_o.jpg?_nc_cat=105&_nc_sid=cdbe9c&_nc_ohc=m5t7Z9A-NSMAX9DzxQJ&_nc_ht=scontent.fbkk2-8.fna&oh=aaf13cfe09a0f900b1c184d19d7a45c9&oe=5E929318',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c55.0.200.200a/p200x200/14445159_1025837907514680_4422708166650316924_o.jpg?_nc_cat=103&_nc_sid=cdbe9c&_nc_ohc=3glQMk78DzcAX82gVVk&_nc_ht=scontent.fbkk2-8.fna&oh=f3ae744501055d57389dd851ee611bd9&oe=5E9323D8',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c53.0.200.200a/p200x200/14444806_1025838224181315_1956270792039579357_o.jpg?_nc_cat=102&_nc_sid=cdbe9c&_nc_ohc=sBRDvizddZcAX9FxMs4&_nc_ht=scontent.fbkk2-8.fna&oh=51fc6dcab2436f4d881024e50b209cec&oe=5E99498F',
            'https://scontent.fbkk2-6.fna.fbcdn.net/v/t31.0-0/c58.0.200.200a/p200x200/14425558_1025835850848219_1733950060278712461_o.jpg?_nc_cat=104&_nc_sid=cdbe9c&_nc_ohc=1uzMmTIv1dYAX_HJv0q&_nc_ht=scontent.fbkk2-6.fna&oh=910587ad77ac4f0f67a1c9d37c393fab&oe=5E8E9FEE',
            'https://scontent.fbkk2-5.fna.fbcdn.net/v/t31.0-0/c36.0.200.200a/p200x200/14352140_1025835940848210_772111150301797504_o.jpg?_nc_cat=110&_nc_sid=cdbe9c&_nc_ohc=iMtyoOKE7O4AX8Pb83G&_nc_ht=scontent.fbkk2-5.fna&oh=570db0a836fc51be5761b254b888ff24&oe=5E9974F6',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c53.0.200.200a/p200x200/14362449_1025836140848190_5441216761723762681_o.jpg?_nc_cat=106&_nc_sid=cdbe9c&_nc_ohc=4tTPsFxsiFoAX_K4F3c&_nc_ht=scontent.fbkk2-7.fna&oh=f6276eed5e6f88b9bb15e7722d33470f&oe=5E91166A',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c100.0.200.200a/p200x200/14445218_1025836430848161_3342879240495006392_o.jpg?_nc_cat=106&_nc_sid=cdbe9c&_nc_ohc=2MMU8VpRa58AX_jF8n-&_nc_ht=scontent.fbkk2-7.fna&oh=2fd00c3870a5571e1ed6d6372038682e&oe=5E95536C',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c54.0.200.200a/p200x200/14444641_1025836984181439_8808349409796662954_o.jpg?_nc_cat=108&_nc_sid=cdbe9c&_nc_ohc=6RNd8EOKz9oAX9WEO7h&_nc_ht=scontent.fbkk2-7.fna&oh=d976a23382f8ad02b631b7b915236356&oe=5E98E9330',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c49.0.200.200a/p200x200/14424727_1025837387514732_1358339369238814549_o.jpg?_nc_cat=105&_nc_sid=cdbe9c&_nc_ohc=m5t7Z9A-NSMAX9DzxQJ&_nc_ht=scontent.fbkk2-8.fna&oh=aaf13cfe09a0f900b1c184d19d7a45c9&oe=5E929318',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c55.0.200.200a/p200x200/14445159_1025837907514680_4422708166650316924_o.jpg?_nc_cat=103&_nc_sid=cdbe9c&_nc_ohc=3glQMk78DzcAX82gVVk&_nc_ht=scontent.fbkk2-8.fna&oh=f3ae744501055d57389dd851ee611bd9&oe=5E9323D8',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c53.0.200.200a/p200x200/14444806_1025838224181315_1956270792039579357_o.jpg?_nc_cat=102&_nc_sid=cdbe9c&_nc_ohc=sBRDvizddZcAX9FxMs4&_nc_ht=scontent.fbkk2-8.fna&oh=51fc6dcab2436f4d881024e50b209cec&oe=5E99498F',
            'https://scontent.fbkk2-6.fna.fbcdn.net/v/t31.0-0/c58.0.200.200a/p200x200/14425558_1025835850848219_1733950060278712461_o.jpg?_nc_cat=104&_nc_sid=cdbe9c&_nc_ohc=1uzMmTIv1dYAX_HJv0q&_nc_ht=scontent.fbkk2-6.fna&oh=910587ad77ac4f0f67a1c9d37c393fab&oe=5E8E9FEE',
            'https://scontent.fbkk2-5.fna.fbcdn.net/v/t31.0-0/c36.0.200.200a/p200x200/14352140_1025835940848210_772111150301797504_o.jpg?_nc_cat=110&_nc_sid=cdbe9c&_nc_ohc=iMtyoOKE7O4AX8Pb83G&_nc_ht=scontent.fbkk2-5.fna&oh=570db0a836fc51be5761b254b888ff24&oe=5E9974F6',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c53.0.200.200a/p200x200/14362449_1025836140848190_5441216761723762681_o.jpg?_nc_cat=106&_nc_sid=cdbe9c&_nc_ohc=4tTPsFxsiFoAX_K4F3c&_nc_ht=scontent.fbkk2-7.fna&oh=f6276eed5e6f88b9bb15e7722d33470f&oe=5E91166A',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c100.0.200.200a/p200x200/14445218_1025836430848161_3342879240495006392_o.jpg?_nc_cat=106&_nc_sid=cdbe9c&_nc_ohc=2MMU8VpRa58AX_jF8n-&_nc_ht=scontent.fbkk2-7.fna&oh=2fd00c3870a5571e1ed6d6372038682e&oe=5E95536C',
            'https://scontent.fbkk2-7.fna.fbcdn.net/v/t31.0-0/c54.0.200.200a/p200x200/14444641_1025836984181439_8808349409796662954_o.jpg?_nc_cat=108&_nc_sid=cdbe9c&_nc_ohc=6RNd8EOKz9oAX9WEO7h&_nc_ht=scontent.fbkk2-7.fna&oh=d976a23382f8ad02b631b7b915236356&oe=5E98E9330',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c49.0.200.200a/p200x200/14424727_1025837387514732_1358339369238814549_o.jpg?_nc_cat=105&_nc_sid=cdbe9c&_nc_ohc=m5t7Z9A-NSMAX9DzxQJ&_nc_ht=scontent.fbkk2-8.fna&oh=aaf13cfe09a0f900b1c184d19d7a45c9&oe=5E929318',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c55.0.200.200a/p200x200/14445159_1025837907514680_4422708166650316924_o.jpg?_nc_cat=103&_nc_sid=cdbe9c&_nc_ohc=3glQMk78DzcAX82gVVk&_nc_ht=scontent.fbkk2-8.fna&oh=f3ae744501055d57389dd851ee611bd9&oe=5E9323D8',
            'https://scontent.fbkk2-8.fna.fbcdn.net/v/t31.0-0/c53.0.200.200a/p200x200/14444806_1025838224181315_1956270792039579357_o.jpg?_nc_cat=102&_nc_sid=cdbe9c&_nc_ohc=sBRDvizddZcAX9FxMs4&_nc_ht=scontent.fbkk2-8.fna&oh=51fc6dcab2436f4d881024e50b209cec&oe=5E99498F'
        ]
    }
    return render_template('eventdetail.html', model = model)

@app.route('/editEvent/<int:id>')
def editEvent(id):
    return 'Edit Event' + str(id)

@app.route('/deleteEvent/<int:id>')
def deleteEvent(id):
    return 'delete event' + str(id)
# end

# Image Filter Page
@app.route('/ImageFilter')
def imageFilter():
    return render_template('imageFilter.html')

def uploadImage():
    pass

def returnResult():
    pass
# end

# Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return 'This page is not finished yet! GO BACK!!'

@app.errorhandler(500)
def internal_error(e):
    return 'Internal Error is occured'
# end

'''
@app.route('/test/<string:user>')
def test(user):
    pass
'''


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()