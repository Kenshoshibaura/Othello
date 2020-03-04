from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./select_data.csv"
port_num = 17086

@app.route('/', methods=['GET'])
def get_html():
    return render_template('./index.html')

@app.route('/lux', methods=['POST'])
def update_lux():
    #time=request.form["time"]
    #lux=request.form["lux"]
    select=request.form["lux"]
    try:
        f = open(file_path,'w')
        f.write(select)
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()
@app.route('/lux',methods=['GET'])
def get_lux():
    try:
        f = open(file_path,'r')
        for row in f:
            select = row
    except Exception as e:
        print(e)
        return # -*- coding: utf-8 -*-
    finally:
        f.close()
        return select

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port_num)
