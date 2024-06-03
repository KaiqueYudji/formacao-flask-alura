# Estas são funções helpers, que ajudam o flask a solucionar proclemas que ele sozinho não consegue
from flask import Flask, render_template, request, redirect, session, flash, url_for 
# session = o session permite manter as informacoes por mais de um ciclo de request. 

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

    def __str__(self):
        print(f'Nome do jogo: {self.name}; Categoria do jogo: {self.category}; Console do jogo: {self.console}')   


game1 = Game('Pokemon go', 'Adventure', 'mobile')
game2 = Game('Fortnite', 'Battle Roayale', 'ps4')
game3 = Game('Minecraft', 'Exploration', 'ps4')
games_array = [game1, game2, game3]


class User:
    def __init__(self, name, nickname, password):
        self.name = name
        self.nickname = nickname
        self.password = password



user1 = User("Kaique Yudji", "Kikito", "kaique2909")
user2 = User("Isabelly Agustinho", "Isinha", "bellynha@2005")
user3 = User("Sueli Sayuri", "Su", "jesus75")
users_array = {
    user1.nickname: user1,
    user2.nickname: user2,
    user3.nickname: user3
}




#Este dunder method "name" faz referência ao arquivo jogoteca.py(faz referência ao nome do módulo atual)
#Então este trecho de código cria uma instância de uma aplicação flask, indicando que o "index" desta aplicação é o arquivo em que o code está escrito
application = Flask(__name__)
application.secret_key = 'alura'#Esta linha de code add uuma camada de criptografia ao sistema, pois, com um chave secreta não será possível alterar as informações que estão armazenadas nos cookies do site 
# e pelo fato de estarmos armazenando as informações do usuário nos cookies do navegador(atraves da funcao 'session'), é importante add uma camada de seguranca


@application.route('/')
def get_games():
    return render_template('lista.html', titulo='Jogos', jogos=games_array)#O flask tem uma padronização por "natureza", na qual ele sabe que os aqruivos HTML estão na pasta templates. Por causa disso, não preciso colocar o path do arquivo HTML, apenas o seu nome.



@application.route('/novo')
def new():
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', proxima=url_for('new')))#Estamos enviando a variavel proxima com o valoe de "novo"

    return render_template('novo.html', titulo='Novo jogo')



@application.route('/criar', methods=['POST',])
def create_game():
    name = request.form['nome']#Este request que importamos na parte superior do script é responsável por capturar as informações dos formulários. O valor passado entre colchetes é o atributo do elemento HTML que ele quer pegar o conteudo 
    category = request.form['categoria']
    console = request.form['console']

    game = Game(name, category, console)
    games_array.append(game)
    return redirect(url_for('get_games'))#A função url_for cria a rota de maneira automatica de acordo com o nome da função que está sendo executado atraves da rota



@application.route('/login')
def login():
    proxima = request.args.get('proxima')# Este code esta pegando as informacoes passadas na rota /login como query
    return render_template('login.html', proxima=proxima)



@application.route('/autenticar', methods=['POST',])
def autenticate():
    if request.form['usuario'] in users_array:

        user = users_array[request.form['usuario']]
        if request.form['senha'] == user.password:
            session['logged_user'] = user.nickname
            flash(user.nickname + ' logged succesfully!')#Esta função envia uma msg rápida e única para quem utiliza o sistema
        
            return redirect(url_for('new'))
        else:
            flash('User not logged in')
            return redirect(url_for('login'))



@application.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logout completed succesfully')
    return redirect(url_for('get_games'))


application.run(debug=True)


application.run()