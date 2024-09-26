from flask import Flask, render_template

app = Flask(__name__)


# Главная страница с миссией
@app.route('/')
def home():
    return render_template('index.html')


# Страница с целью и девизом
@app.route('/index')
def mission():
    return render_template('index.html')


# Страница с помощниками
@app.route('/assistant')
def assistants():
    return render_template('assistant.html')


# Страница о Фродо
@app.route('/hero')
def hero():
    return render_template('hero.html')


# Страница с советами Фродо
@app.route('/my_guide')
def guide():
    return render_template('my_guide.html')


# Страница волонтеров
@app.route('/volunteers')
def volunteers():
    return render_template('volunteers.html')


# Страница 1 (пример путеводитель)
@app.route('/page1')
def page1():
    return render_template('page1.html')


# Страница 2 (пример карта)
@app.route('/page2')
def page2():
    return render_template('page2.html')


# Страница 3 (пример достопримечательности)
@app.route('/page3')
def page3():
    return render_template('page3.html')


# Страница об авторе
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
