from flask import Flask
import random

app = Flask(__name__)


fatos = [ "A maioria das pessoas que sofre de dependência tecnológica sente um forte estresse quando fica fora da área de cobertura de rede ou não pode usar seus dispositivos",
         "De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.",
        "O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna",
        "Segundo um estudo de 2019, mais de 60% das pessoas respondem a mensagens de trabalho em seus smartphones dentro de 15 minutos após sair do trabalho",
        "Uma forma de combater a dependência tecnológica é buscar atividades que tragam prazer e melhorem o humor",
        "Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, fazendo com que passemos o máximo de tempo possível consumindo conteúdo",
        "Elon Musk também defende a regulamentação das redes sociais e a proteção dos dados pessoais dos usuários. Ele afirma que as redes sociais coletam uma enorme quantidade de informações sobre nós, que podem ser usadas para manipular nossos pensamentos e comportamentos",
        "As redes sociais têm pontos positivos e negativos, e devemos estar atentos a ambos ao utilizar essas plataformas"
]



@app.route("/") # Página inicial
def hello_world():
    return '''
        <h1>Olá! Você quer ver fatos aleatórios? Clique no link! E em cima de mim depois da barra '/' tem um jogo SECRETO, você deve descobrir o nome!</h1>
        <a href="/fatos">Veja um fato aleatório!</a>
        <a href="/senha">Veja uma senha segura!</a>
    '''
@app.route("/fatos") # Mostra fatos aleatórios
def ver_fatos(): 
    return f'<h1>{random.choice(fatos)}</h1><br><br><a href="/">Voltar</a>'

@app.route("/secreto") # Um jogo secreto de cara ou coroa
def jogar_moeda():
    resultado = random.choice(["Cara", "Coroa"])
    return f'''
        <h1> 🪙 Jogando moeda... </h1>
        <h1>🪙 Resultado: {resultado}</h1>
        <a href="/">Voltar para o início</a>
    '''

@app.route("/senha") # Gera uma senha super segura de 8 caracteres
def gerar_senha():
    caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    senha = ""
    for i in range(8):
        senha += random.choice(caracteres)
    return f'''
        <h1>🔐 Sua senha SUPER MEGA segura é:</h1>
        <code style="font-size: 24px; background: #eee; padding: 10px;">{senha}</code>
        <br><br><a href="/">Voltar</a>
    '''
 
app.run(debug=True)
