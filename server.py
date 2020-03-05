#server.py

from flask import Flask, request, render_template
import sys
import subprocess
#import urllib.parse
app = Flask(__name__)
#file_path = "./select_data.csv"
file_path = "./selectAI.csv"
#file_path2 = "./selectPR.csv"
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
    print("get_lux")
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

@app.route('/lux/00',methods=['GET'])
def get_lux00():
    print("00")
@app.route('/lux/01',methods=['GET'])
def get_lux01():
    print("01")
@app.route('/lux/02',methods=['GET'])
def get_lux02():
    print("02")
@app.route('/lux/03',methods=['GET'])
def get_lux03():
    print("03")
@app.route('/lux/04',methods=['GET'])
def get_lux04():
    print("04")
@app.route('/lux/05',methods=['GET'])
def get_lux05():
    print("05")
@app.route('/lux/06',methods=['GET'])
def get_lux06():
    print("06")
@app.route('/lux/07',methods=['GET'])
def get_lux07():
    print("07")

@app.route('/lux/10',methods=['GET'])
def get_lux10():
    print("10")
@app.route('/lux/11',methods=['GET'])
def get_lux11():
    print("11")
@app.route('/lux/12',methods=['GET'])
def get_lux12():
    print("12")
@app.route('/lux/13',methods=['GET'])
def get_lux1():
    print("13")
@app.route('/lux/14',methods=['GET'])
def get_lux1():
    print("14")
@app.route('/lux/15',methods=['GET'])
def get_lux1():
    print("15")
@app.route('/lux/16',methods=['GET'])
def get_lux1():
    print("16")
@app.route('/lux/17',methods=['GET'])
def get_lux1():
    print("17")

@app.route('/lux/20',methods=['GET'])
def get_lux2():
    print("20")
@app.route('/lux/21',methods=['GET'])
def get_lux2():
    print("21")
@app.route('/lux/22',methods=['GET'])
def get_lux2():
    print("22")
@app.route('/lux/23',methods=['GET'])
def get_lux2():
    print("23")
@app.route('/lux/24',methods=['GET'])
def get_lux2():
    print("24")
@app.route('/lux/25',methods=['GET'])
def get_lux2():
    print("25")
@app.route('/lux/26',methods=['GET'])
def get_lux2():
    print("26")
@app.route('/lux/27',methods=['GET'])
def get_lux2():
    print("27")

@app.route('/lux/30',methods=['GET'])
def get_lux3():
    print("30")
@app.route('/lux/31',methods=['GET'])
def get_lux3():
    print("31")
@app.route('/lux/32',methods=['GET'])
def get_lux3():
    print("32")
@app.route('/lux/33',methods=['GET'])
def get_lux3():
    print("33")
@app.route('/lux/34',methods=['GET'])
def get_lux3():
    print("34")
@app.route('/lux/35',methods=['GET'])
def get_lux3():
    print("35")
@app.route('/lux/36',methods=['GET'])
def get_lux3():
    print("36")
@app.route('/lux/37',methods=['GET'])
def get_lux3():
    print("37")

@app.route('/lux/40',methods=['GET'])
def get_lux4():
    print("40")
@app.route('/lux/41',methods=['GET'])
def get_lux4():
    print("41")
@app.route('/lux/42',methods=['GET'])
def get_lux4():
    print("42")
@app.route('/lux/43',methods=['GET'])
def get_lux4():
    print("43")
@app.route('/lux/44',methods=['GET'])
def get_lux4():
    print("44")
@app.route('/lux/45',methods=['GET'])
def get_lux4():
    print("45")
@app.route('/lux/46',methods=['GET'])
def get_lux4():
    print("46")
@app.route('/lux/47',methods=['GET'])
def get_lux4():
    print("47")

@app.route('/lux/50',methods=['GET'])
def get_lux5():
    print("50")
@app.route('/lux/51',methods=['GET'])
def get_lux5():
    print("51")
@app.route('/lux/52',methods=['GET'])
def get_lux5():
    print("52")
@app.route('/lux/53',methods=['GET'])
def get_lux5():
    print("53")
@app.route('/lux/54',methods=['GET'])
def get_lux5():
    print("54")
@app.route('/lux/55',methods=['GET'])
def get_lux5():
    print("55")
@app.route('/lux/56',methods=['GET'])
def get_lux5():
    print("56")
@app.route('/lux/57',methods=['GET'])
def get_lux5():
    print("57")

@app.route('/lux/60',methods=['GET'])
def get_lux6():
    print("60")
@app.route('/lux/61',methods=['GET'])
def get_lux6():
    print("61")
@app.route('/lux/62',methods=['GET'])
def get_lux6():
    print("62")
@app.route('/lux/63',methods=['GET'])
def get_lux6():
    print("63")
@app.route('/lux/64',methods=['GET'])
def get_lux6():
    print("64")
@app.route('/lux/65',methods=['GET'])
def get_lux6():
    print("65")
@app.route('/lux/66',methods=['GET'])
def get_lux6():
    print("66")
@app.route('/lux/67',methods=['GET'])
def get_lux6():
    print("67")

@app.route('/lux/70',methods=['GET'])
def get_lux70():
    print("70")
@app.route('/lux/71',methods=['GET'])
def get_lux71():
    print("71")
@app.route('/lux/72',methods=['GET'])
def get_lux72():
    print("72")
@app.route('/lux/73',methods=['GET'])
def get_lux73():
    print("73")
@app.route('/lux/74',methods=['GET'])
def get_lux74():
    print("74")
@app.route('/lux/75',methods=['GET'])
def get_lux75():
    print("75")
@app.route('/lux/76',methods=['GET'])
def get_lux76():
    print("76")
@app.route('/lux/77',methods=['GET'])
def get_lux77():
    print("77")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port_num)
