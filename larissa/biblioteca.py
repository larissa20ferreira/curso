from flask import Flask

app = Flask(__name__)

@app.route("/inicio")
def inicio():
    return ("<h1> Título do meu Site</h1><p>Este é um parágrafro</p>")

@app.route("/lista")
def listar_livros():
    return """
    <!DOCTYPE html>
<html lang="pt-br">
<head>
    <link rel="stylesheet" href="./bootstrap.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Biblioteca Senai </title>
</head>
<body>
    <h1>Lista de livros</h1>
    <p>Página para listar os Livros da <br/>Biblioteca do Senai
        <br><br><br><br>

    <table class="table table-striped table-hover">
        <thead class="thead-default">
        <tr>
            <th>Livros</th>
            <th>Autor</th>
            <th>Ano</th>
            <th>Categoria</th>
            <th>Ativo</th>
        </tr>
        <tr>
            <td>Caçadora de estrelas</td>
            <td>Um Lugar Para o Amor</td>
            <td>Todo Dia</td>
            <td>Tudo e Todas as Coisas</td>
            <td>Sim</td>
        </tr>
        <tr>
            <td>Caçadora de estrelas</td>
            <td>Um Lugar Para o Amor</td>
            <td>Todo Dia</td>
            <td>Tudo e Todas as Coisas</td>
            <td>Sim</td>
        </tr>
        <tr>
            <td>Caçadora de estrelas</td>
            <td>Um Lugar Para o Amor</td>
            <td>Todo Dia</td>
            <td>Tudo e Todas as Coisas</td>
            <td>Sim</td>
        </tr>
        <tr>
            <td>Caçadora de estrelas</td>
            <td>Um Lugar Para o Amor</td>
            <td>Todo Dia</td>
            <td>Tudo e Todas as Coisas</td>
            <td>Sim</td>
        </tr>

    </table>

    
</body>
</html>
"""

@app.route("/teste")
def teste():
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Site Exemplo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #333;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        nav {
            display: flex;
            justify-content: center;
            background-color: #444;
            padding: 10px;
        }
        nav a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            padding: 8px;
        }
        nav a:hover {
            background-color: #555;
            border-radius: 5px;
        }
        main {
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        section {
            margin-bottom: 20px;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
            position: relative;
            bottom: 0;
            width: 100%;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Meu Site Exemplo</h1>
    </header>

    <nav>
        <a href="#home">Início</a>
        <a href="#about">Sobre</a>
        <a href="#services">Serviços</a>
        <a href="#contact">Contato</a>
    </nav>

    <main>
        <section id="home">
            <h2>Bem-vindo ao Meu Site</h2>
            <p>Este é um exemplo de um site básico criado com HTML e CSS. Aqui você pode adicionar qualquer conteúdo que desejar.</p>
            <img src="https://via.placeholder.com/1200x500" alt="Imagem de exemplo">
        </section>

        <section id="about">
            <h2>Sobre Nós</h2>
            <p>Somos uma empresa fictícia criada para demonstrar como estruturar um site HTML básico. Oferecemos uma variedade de serviços para atender suas necessidades.</p>
        </section>

        <section id="services">
            <h2>Serviços</h2>
            <ul>
                <li>Consultoria em Tecnologia</li>
                <li>Desenvolvimento Web</li>
                <li>Design Gráfico</li>
            </ul>
        </section>

        <section id="contact">
            <h2>Contato</h2>
            <p>Para entrar em contato conosco, envie um e-mail para <a href="mailto:contato@exemplo.com">contato@exemplo.com</a>.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Meu Site Exemplo. Todos os direitos reservados.</p>
    </footer>
</body>
</html>"""


app.run()