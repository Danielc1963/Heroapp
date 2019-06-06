from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'DanielC'}
    return '''
<html>
    <head>
        <h1>ようこそ、ターミナルサービスへ。</h1>
    </head>
    <body>
        <h>''' + user['username'] + ''' って名前か。新人ですね。アイラAlterと申します。今日からお前の新しい相棒だ、よろしくね！</h>
    </body>
</html>'''