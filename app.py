#set FLASK_APP=app.py - nazwa pliku do uruchomienia przez flask(zmianna środowiskowa)
#set FLASK_ENV=development

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/mypage/parent')
def website_p():
    return render_template("parent_website.html")


@app.route('/mypage/me')
def website1():
    return render_template("NEW_my_website_1.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def website2():
    if request.method == 'GET':
        return render_template("NEW_my_website_2.html")
    elif request.method == 'POST':
        print(request.form)
        return 'wiadomość wysłana'

if __name__ == "__main__":
    app.run(debug=True)