# O Flask é um framework micro para Python usado para desenvolver aplicações web.
# from flask import Flask: Esta linha importa a classe Flask do módulo flask. 
# Com esta classe, você pode criar uma aplicação web.
from flask import Flask

# Flask(__name__) cria uma instância da aplicação Flask. O __name__ é uma variável especial que, 
# em um contexto de aplicativo Flask, ajuda o framework a determinar o local da aplicação 
# (para procurar arquivos estáticos e templates).
# app é a variável que vai armazenar a instância da aplicação Flask.
app = Flask(__name__)

# @app.route('/'): Este é um "decorador" que associa a função home() à URL raiz (/) da aplicação. 
# Ou seja, quando um usuário acessa o endereço principal da aplicação (geralmente http://localhost:5000/), 
# a função home() será executada.
# def home():: A função home() é definida para responder à solicitação HTTP na URL raiz.
# return "Hello, Flask!": A função home() retorna uma string simples, que será exibida na página web. 
# Isso significa que, quando a rota / for acessada, a página mostrará "Hello, Flask!".
@app.route('/')
def home():
    return "Hello, Flask! - Criado pelo Eduardo Popovici"

# if __name__ == '__main__':: Esta condição verifica se o script está sendo 
# executado diretamente ou importado como um módulo em outro script.
# Se o script for executado diretamente (não importado), o Flask vai rodar a aplicação.
# Se for importado, o código dentro do if não será executado, evitando que o 
# servidor Flask seja iniciado automaticamente.
# app.run(debug=True): Essa linha inicia o servidor web. O debug=True habilita o modo de depuração, 
# o que significa que o servidor reiniciará automaticamente toda vez que você fizer uma alteração no código e 
# mostrará erros detalhados no navegador.
if __name__ == '__main__':
    app.run(debug=True)
