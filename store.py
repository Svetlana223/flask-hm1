'''
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда»,
«Обувь» и «Куртка», используя базовый шаблон.
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/clothing')
def clothing():
    return render_template('clothing.html', category='Одежда')


@app.route('/shoes')
def shoes():
    return render_template('shoes.html', category='Обувь')



if __name__ == '__main__':
    app.run(debug=True)
