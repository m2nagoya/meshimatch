import pyrebase
import flask

config = {
    apiKey: "AIzaSyCY2xmJQmxKVtV0kcyS9UccAWBDYAHMCv4",
    authDomain: "meshimatch-47632.firebaseapp.com",
    databaseURL: "https://meshimatch-47632.firebaseio.com",
    projectId: "meshimatch-47632",
    storageBucket: "meshimatch-47632.appspot.com",
    messagingSenderId: "7175435560",
    appId: "1:7175435560:web:32d216284133908a8ccc1d",
    measurementId: "G-PKSJ0GG52X"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
# db.child("names").push({"name":"kota"})
# db.child("names").push({"name":"take"})


# ルートを指定、メソッドはGET、POST
@app.route('/', methods=['GET', 'POST'])

# basic関数を定義
def basic():
    # POSTでリクエストされたら
    if request.method == 'POST':
        # form['submit']のvalueが'add'であれば
        if request.form['submit'] == 'add':
            # formから値を取得
            name = request.form['name']
            # 値をfirebase上のtodoに書き込む
            db.child("todo").push(name)
            # firebaseから値を取得
            todo = db.child("todo").get()
            # toに値を代入
            to = todo.val()
            # index.htmlに 値toを返す
            return render_template('index.html', t=to.values())
        # form['submit']のvalueが'delete'であれば
        elif request.form['submit'] == 'delete':
            # firebaseのdbであるtodoを削除
            db.child("todo").remove()
            # 元のindex.htmlを返す
            return render_template('index.html',)
    # それ以外は、index.htmlを返す
    return render_template('index.html')

if __name__ == '__main__':
    #処理の実行
    app.run(debug=True)
