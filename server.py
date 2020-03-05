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

@app.route('/lux/00',methods=['GET'])
def get_lux00():
    #select_player = 00
    f = open(file_path2,'w')
    f.write("00")
    f.close()
    #print(select_player)
    #print("00")
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
    #select_player = 01
    f = open(file_path2,'w')
    f.write("01")
    f.close()
    #print(select_player)
    #print("01")
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
    #select_player = 02
    f = open(file_path2,'w')
    f.write("02")
    f.close()
    #print(select_player)
    #print("02")
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
    #select_player = 03
    f = open(file_path2,'w')
    f.write("03")
    f.close()
    #print(select_player)
    #print("03")
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
    #select_player = 04
    f = open(file_path2,'w')
    f.write("04")
    f.close()
    #print(select_player)
    #print("04")
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
    #select_player = 05
    f = open(file_path2,'w')
    f.write("05")
    f.close()
    #print(select_player)
    #print("05")
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
    #select_player = 06
    f = open(file_path2,'w')
    f.write("06")
    f.close()
    #print(select_player)
    #print("06")
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
    #select_player = 07
    f = open(file_path2,'w')
    f.write("07")
    f.close()
    #print(select_player)
    #print("07")
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
    select_player = 10
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("10")
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
    select_player = 11
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("11")
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
    select_player = 12
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("12")
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
    select_player = 13
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("13")
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
    select_player = 14
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("14")
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
    select_player = 15
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("15")
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
    select_player = 16
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("16")
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
    select_player = 17
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("17")
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
    select_player = 20
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("20")
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
    select_player = 21
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("21")
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
    select_player = 22
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("22")
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
    select_player = 23
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("23")
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
    select_player = 24
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("24")
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
    select_player = 25
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("25")
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
    select_player = 26
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("26")
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
    select_player = 27
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("27")
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
    select_player = 30
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("30")
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
    select_player = 31
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("31")
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
    select_player = 32
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("32")
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
    select_player = 33
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("33")
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
    select_player = 34
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("34")
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
    select_player = 35
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("35")
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
    select_player = 36
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("36")
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
    select_player = 37
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("37")
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
    select_player = 40
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("40")
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
    select_player = 41
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("41")
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
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("42")
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
    select_player = 43
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("43")
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
    select_player = 44
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("44")
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
    select_player = 45
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("45")
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
    select_player = 46
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("46")
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
    select_player = 47
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("47")
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
    select_player = 50
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("50")
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
    select_player = 51
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("51")
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
    select_player = 52
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("52")
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
    select_player = 53
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("53")
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
    select_player = 54
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("54")
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
    select_player = 55
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("55")
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
    select_player = 56
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("56")
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
    select_player = 57
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("57")
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
    select_player = 60
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("60")
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
    select_player = 61
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("61")
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
    select_player = 62
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("62")
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
    select_player = 63
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("63")
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
    select_player = 64
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("64")
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
    select_player = 65
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("65")
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
    select_player = 66
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("66")
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
    select_player = 67
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("67")
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
    select_player = 70
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("70")
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
    select_player = 71
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("71")
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
    select_player = 72
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("72")
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
    select_player = 73
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("73")
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
    select_player = 74
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("74")
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
    select_player = 75
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("75")
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
    select_player = 76
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("76")
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
    f = open(file_path2,'w')
    f.write(str(select_player))
    f.close()
    #print(select_player)
    #print("77")
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
