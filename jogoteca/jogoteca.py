from flask import Flask, render_template, request, redirect # Estas são funções helpers, que ajudam o flask a solucionar proclemas que ele sozinho não consegue

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

    def __str__(self):
        print(f'Nome do jogo: {self.name}; Categoria do jogo: {self.category}; Console do jogo: {self.console}')   


game1 = Game('Pokemom go', 'Adventure', 'mobile')
game2 = Game('Fortnite', 'Battle Roayale', 'ps4')
game3 = Game('Minecraft', 'Exploration', 'ps4')
games_array = [game1, game2, game3]


#Este dunder method "name" faz referência ao arquivo jogoteca.py(faz referência ao nome do módulo atual)
#Então este trecho de código cria uma instância de uma aplicação flask, indicando que o "index" desta aplicação é o arquivo em que o code está escrito
application = Flask(__name__)


@application.route('/')
def get_games():
    return render_template('lista.html', titulo='Jogos', jogos=games_array)#O flask tem uma padronização por "natureza", na qual ele sabe que os aqruivos HTML estão na pasta templates. Por causa disso, não preciso colocar o path do arquivo HTML, apenas o seu nome.



@application.route('/novo')
def new():
    return render_template('novo.html', titulo='Novo jogo')



@application.route('/criar', methods=['POST',])
def create_game():
    name = request.form['nome']#Este request que importamos na parte superior do script é responsável por capturar as informações dos formulários. O valor passado entre colchetes é o atributo do elemento HTML que ele quer pegar o conteudo 
    category = request.form['categoria']
    console = request.form['console']

    game = Game(name, category, console)
    games_array.append(game)
    return redirect('/')


application.run(debug=True)


application.run()