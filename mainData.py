from flask import Flask
from flask import request, after_this_request,make_response

app = Flask(__name__)


@app.route("/main", methods=['POST', 'GET'])
def getData():
    return f'''
            <p>Ingresa los datos</p>
            '''

@app.route("/", methods=['POST', 'GET'])
def login():
    print(request.cookies.get('ingresar'))
    sesion = request.cookies.get('ingresar')
    
    if(sesion is not None and sesion =='True'):
        daCookie = make_response()
        daCookie.set_cookie('ingresar', 'False')
        return app.redirect('/main')
    return f''' 
    
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="{app.url_for('static', filename='style.css')}">
    </head>
    
    <form action="" method="post"> 
        <div class="login">
            <fieldset>
                <legend>Login</legend>
                <label>Usuario
                    <input type="text">
                </label><br />
                <label>Contraseña
                    <input type="text">
                </label><br /><br />
                <label>
                    <button>Ingresar</button>
                </label><br />
            </fieldset>
        </div> 
    </form>
    '''
def resetCookie():
    daCookie = make_response()
    daCookie.set_cookie('ingresar', 'True')
    return daCookie

@app.before_request
def checkButton():
    check = request.cookies.get("ingresar")
    if(check is None or check == 'False'):
        @after_this_request
        def defineCheck(value):
            value.set_cookie('ingresar', 'True')
            return value
        
def changeURL():
    app.redirect(app.url_for('getData'))

#Nice, por el momento todo lo de html funciona, y todo se puede programar como si fuera html/php