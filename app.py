from flask import Flask, make_response, render_template, request

app = Flask(__name__)
app.secret_key="shhhhh"

@app.route('/')
def main():
    response = make_response(render_template('home.html'))
    response.headers['Decisión-cookies'] = 'cookies'
    return response

@app.route('/set_cookies')
def set_cookies():
    response = make_response("Cookie creada.")
    response.set_cookie('user', 'Juan', httponly=True, secure=True)
    return response

@app.route('/get_cookies')
def get_cookies():
    usuario = request.cookies.get('user')
    if usuario:
        return f"<h1>Hola {usuario}</h1>"
    return "No se encontró la cookie"

@app.route('/denegar_cookies')
def denegar_cookies():
    return "Cookie rechazada"

@app.route('/delete_cookies')
def delete_cookies():
    response = make_response("Cookie eliminada")
    response.delete_cookie('user')
    return response

if __name__ == '__main__':
    app.run()
