# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/test')
# def render():
#     return render_template('page.html')

# if __name__=='__main__':
#     app.run(debug=True, host='localhost', port=3123)


# from flask import Flask
# app = Flask(__name__)

# @app.route('/alpha')
# def alpha():
#     return "This is the alpha version"

# @app.route('/beta')
# def beta():
#     return "This is the beta version"

# if __name__=='__main__':
#     app.run(debug=True, port=3123)

# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def render():
#     return render_template('page.html')

# if __name__=='__main__':
#     app.run(debug=True, port=3123) 

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/input')
def render():
    if 'filename' in request.args:
        myfilename = request.args.get('filename')
        print(myfilename)
        return render_template(myfilename)
    else:
        return "No input file specified"

if __name__=='__main__':
    app.run(debug=True, port=3123) 
