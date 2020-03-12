#server.py

from flask import Flask, request, render_template
import sys
import subprocess
import time
#import urllib.parse
app = Flask(__name__)
#file_path = "./select_data.csv"
file_path = "./selectAI.csv"
file_path2 = "./selectPR.txt"

port_num = 17086

@app.route('/', methods=['GET'])
def get_html():
    print("get_html")
    subprocess.Popen([sys.executable,'ss.py'])
    return render_template('./index.html')

@app.route('/lux', methods=['POST'])
def update_lux():
    print("update_lux")
    time=request.form["time"]
    lux=request.form["lux"]
    try:
        print(str(time)+","+str(lux))
        f = open(file_path,'w')
        f.write(time+","+lux)
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()
@app.route('/lux',methods=['GET'])
def get_lux():
    #print("get_lux")
    time.sleep(1)
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

@app.route('/lux/<select>',methods=['GET'])
def get_lux_select(select):
    f = open(file_path2,'w')
    f.write(select)
    f.close()
    #print(select)
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
