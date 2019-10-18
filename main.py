from flask import Flask, escape, request, jsonify
from pypinyin import pinyin, lazy_pinyin, Style

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/api/pinyina', methods=['GET'])
def pa():
    v = request.args.get("var", "")
    if v == "":
        return jsonify({"code": 304, "message": "var empty"})
    return jsonify({"code": 200, "message": "success", "data":[{"var": v, "pinyin": lazy_pinyin(v, style=Style.FIRST_LETTER)}]})

@app.route('/api/pinyin', methods=['GET'])
def p():
    v = request.args.get("var", "")
    if v == "":
        return jsonify({"code": 304, "message": "var empty"})
    return jsonify({"code": 200, "message": "success", "data":[{"var": v, "pinyin": lazy_pinyin(v)}]})

if __name__ == '__main__':
    app.run(debug=True)
