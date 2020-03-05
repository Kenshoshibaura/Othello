#server.py

from flask import Flask, request, render_template
import sys
import subprocess
#import urllib.parse
app = Flask(__name__)
#file_path = "./select_data.csv"
file_path = "./selectAI.csv"
file_path2 = "./selectPR.csv"
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
@app.route('/lux/01',methods=['GET'])
def get_lux01():
    print("01")
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
@app.route('/lux/02',methods=['GET'])
def get_lux02():
    print("02")
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
@app.route('/lux/03',methods=['GET'])
def get_lux03():
    print("03")
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
@app.route('/lux/04',methods=['GET'])
def get_lux04():
    print("04")
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
@app.route('/lux/05',methods=['GET'])
def get_lux05():
    print("05")
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
@app.route('/lux/06',methods=['GET'])
def get_lux06():
    print("06")
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
@app.route('/lux/07',methods=['GET'])
def get_lux07():
    print("07")
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

@app.route('/lux/10',methods=['GET'])
def get_lux10():
    print("10")
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
@app.route('/lux/11',methods=['GET'])
def get_lux11():
    print("11")
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
@app.route('/lux/12',methods=['GET'])
def get_lux12():
    print("12")
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
@app.route('/lux/13',methods=['GET'])
def get_lux13():
    print("13")
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
@app.route('/lux/14',methods=['GET'])
def get_lux14():
    print("14")
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
@app.route('/lux/15',methods=['GET'])
def get_lux15():
    print("15")
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
@app.route('/lux/16',methods=['GET'])
def get_lux16():
    print("16")
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
@app.route('/lux/17',methods=['GET'])
def get_lux17():
    print("17")
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

@app.route('/lux/20',methods=['GET'])
def get_lux20():
    print("20")
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
@app.route('/lux/21',methods=['GET'])
def get_lux21():
    print("21")
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
@app.route('/lux/22',methods=['GET'])
def get_lux22():
    print("22")
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
@app.route('/lux/23',methods=['GET'])
def get_lux23():
    print("23")
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
@app.route('/lux/24',methods=['GET'])
def get_lux24():
    print("24")
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
@app.route('/lux/25',methods=['GET'])
def get_lux25():
    print("25")
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
@app.route('/lux/26',methods=['GET'])
def get_lux26():
    print("26")
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
@app.route('/lux/27',methods=['GET'])
def get_lux27():
    print("27")
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

@app.route('/lux/30',methods=['GET'])
def get_lux30():
    print("30")
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
@app.route('/lux/31',methods=['GET'])
def get_lux31():
    print("31")
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
@app.route('/lux/32',methods=['GET'])
def get_lux32():
    print("32")
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
@app.route('/lux/33',methods=['GET'])
def get_lux33():
    print("33")
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
@app.route('/lux/34',methods=['GET'])
def get_lux34():
    print("34")
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
@app.route('/lux/35',methods=['GET'])
def get_lux35():
    print("35")
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
@app.route('/lux/36',methods=['GET'])
def get_lux36():
    print("36")
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
@app.route('/lux/37',methods=['GET'])
def get_lux37():
    print("37")
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

@app.route('/lux/40',methods=['GET'])
def get_lux40():
    print("40")
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
@app.route('/lux/41',methods=['GET'])
def get_lux41():
    print("41")
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
@app.route('/lux/42',methods=['GET'])
def get_lux42():
    select_player = 42
    print(select_player)
    print("42")
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
@app.route('/lux/43',methods=['GET'])
def get_lux43():
    print("43")
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
@app.route('/lux/44',methods=['GET'])
def get_lux44():
    print("44")
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
@app.route('/lux/45',methods=['GET'])
def get_lux45():
    print("45")
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
@app.route('/lux/46',methods=['GET'])
def get_lux46():
    print("46")
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
@app.route('/lux/47',methods=['GET'])
def get_lux47():
    print("47")
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

@app.route('/lux/50',methods=['GET'])
def get_lux50():
    print("50")
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
@app.route('/lux/51',methods=['GET'])
def get_lux51():
    print("51")
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
@app.route('/lux/52',methods=['GET'])
def get_lux52():
    print("52")
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
@app.route('/lux/53',methods=['GET'])
def get_lux53():
    print("53")
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
@app.route('/lux/54',methods=['GET'])
def get_lux54():
    print("54")
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
@app.route('/lux/55',methods=['GET'])
def get_lux55():
    print("55")
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
@app.route('/lux/56',methods=['GET'])
def get_lux56():
    print("56")
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
@app.route('/lux/57',methods=['GET'])
def get_lux57():
    print("57")
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

@app.route('/lux/60',methods=['GET'])
def get_lux60():
    print("60")
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
@app.route('/lux/61',methods=['GET'])
def get_lux61():
    print("61")
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
@app.route('/lux/62',methods=['GET'])
def get_lux62():
    print("62")
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
@app.route('/lux/63',methods=['GET'])
def get_lux63():
    print("63")
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
@app.route('/lux/64',methods=['GET'])
def get_lux64():
    print("64")
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
@app.route('/lux/65',methods=['GET'])
def get_lux65():
    print("65")
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
@app.route('/lux/66',methods=['GET'])
def get_lux66():
    print("66")
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
@app.route('/lux/67',methods=['GET'])
def get_lux67():
    print("67")
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

@app.route('/lux/70',methods=['GET'])
def get_lux70():
    print("70")
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
@app.route('/lux/71',methods=['GET'])
def get_lux71():
    print("71")
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
@app.route('/lux/72',methods=['GET'])
def get_lux72():
    print("72")
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
@app.route('/lux/73',methods=['GET'])
def get_lux73():
    print("73")
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
@app.route('/lux/74',methods=['GET'])
def get_lux74():
    print("74")
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
@app.route('/lux/75',methods=['GET'])
def get_lux75():
    print("75")
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
@app.route('/lux/76',methods=['GET'])
def get_lux76():
    print("76")
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
@app.route('/lux/77',methods=['GET'])
def get_lux77():
    select_player = 77
    print(select_player)
    print("77")
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
