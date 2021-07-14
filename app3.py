from flask import Flask, render_template

app=Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('homepage.html', name=name)

# if __name__=='__main__':
#     app.debug=True
#     app.run()

# @app.route('/looping/<int:number>')
# def looping(number):
#     return render_template('loopy.html', number=number)
#
# if __name__=='__main__':
#     app.debug=True
#     app.run()

# @app.route('/times/<int:number>')
# def looping(number):
#     return render_template('timestable.html', number=number)
#
# if __name__=='__main__':
#     app.debug=True
#     app.run()

@app.route('/my_picture')
def picture():
    return render_template('image.html')

if __name__=='__main__':
    app.debug=True
    app.run()


