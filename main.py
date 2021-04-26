from flask import *
import requests


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def return_sample_page():
    if request.method == 'GET':
        return render_template('page1.html')
    elif request.method == 'POST':
        if not request.form.get('koordinates'):
            return render_template('page1.html')
        else:
            try:
                a, b = request.form.get('koordinates').split()
                response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={b},{a}&spn=0.016457,0.00619&l=map')
                with open('static/img/1.jpg', 'wb') as f:
                    f.write(response.content)
                response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={b},{a}&spn=0.016457,0.00619&l=sat')
                with open('static/img/2.jpg', 'wb') as f:
                    f.write(response.content)
                return f'''<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <title>Ответ на запрос</title>
                        </head>
                        <body>
                            <h1>Сервис "Найти место"</h1>
                            <p style='font-size:20px;'>Здесь Вы можете найти нужное место, введя координаты</p>
                            <img src="{url_for('static', filename='img/1.jpg')}"
                                        alt="Ошибка">
                            <img src="{url_for('static', filename='img/2.jpg')}"
                                        alt="Ошибка">
                            <form class="login_form" method="post">
                                <button type="submit" class="btn btn-primary">Заново</button>
                            </form>
                        </body>
                        </html>'''
            except Exception:
                return render_template('page1.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
