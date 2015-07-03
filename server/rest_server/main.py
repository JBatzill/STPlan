from datetime import date
from database.sql_commands import SQL_READ_STD
from rest_server import app
from flask import request
from datetime import timedelta
from rest_server.definitions import *
from rest_server.rest_db import query_db
from logger import get_log_rest

#get schedule for given school and properties
@app.route('/getschedule', subdomain="<school>." + SUBDOMAIN)
def get_schedule(school):
    try:
        _days = int(request.args.get('days', DEFAULT_DAYS))
        _class = request.args.get('class', DEFAULT_CLASS)
    except ValueError:
        return create_error_message("Unable to convert given parameter!");

    if _days < 0:
        return create_error_message("days must be at least 0!")

    _today = date.today()

    get_log_rest().info("request#get_schedule: " + school + ", " + str(_days) + ", " + _class)
    res = query_db(SQL_READ_STD, [school, _today, _today + timedelta(days=_days), _class])

    return json_dic(res)


@app.route('/gettestdata', subdomain=SUBDOMAIN)
def get_testdata():
    return "<table class='subst' >\
            <tr class='list'><th class='list'>Datum</th><th class='list'>Tag</th><th class='list'>Klasse(n)</th><th class='list'>Stunde</th><th class='list'>Vertreter</th><th class='list'>Fach</th><th class='list'>Raum</th><th class='list'>(Fach)</th><th class='list'>(Lehrer)</th><th class='list'>Vertr. von</th><th class='list'>(Le.) nach</th></tr>\
            <tr class='list odd'><td class='list'>3.7.</td><td class='list'>Fr</td><td class='list'>5B</td><td class='list'>5</td><td class='list'>Faus</td><td class='list'>L</td><td class='list'>E201</td><td class='list'>L</td><td class='list'>Bads</td><td class='list'>&nbsp;</td><td class='list'>&nbsp;</td></tr>\
            <tr class='list even'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >5C</td><td class='list' >8</td><td class='list' >---</td><td class='list' >---</td><td class='list' >---</td><td class='list' >Mu</td><td class='list' >Bick</td><td class='list' >&nbsp;</td><td class='list' >Fr-26.6. / 3</td></tr>\
            <tr class='list odd'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >5C</td><td class='list' >9</td><td class='list' >---</td><td class='list' >---</td><td class='list' >---</td><td class='list' >Mu</td><td class='list' >Bick</td><td class='list' >&nbsp;</td><td class='list' >Fr-26.6. / 4</td></tr>\
            <tr class='list even'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >(6A)</td><td class='list' >3</td><td class='list' >&nbsp;</td><td class='list' >---</td><td class='list' >---</td><td class='list' >SV</td><td class='list' >Muetz</td><td class='list' >&nbsp;</td><td class='list' >Freis.</td></tr>\
            <tr class='list odd'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >(6A)</td><td class='list' >4</td><td class='list' >&nbsp;</td><td class='list' >---</td><td class='list' >---</td><td class='list' >B</td><td class='list' >Boehm</td><td class='list' >&nbsp;</td><td class='list' >Freis.</td></tr>\
            <tr class='list even'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >(6A)</td><td class='list' >5</td><td class='list' >&nbsp;</td><td class='list' >---</td><td class='list' >---</td><td class='list' >E</td><td class='list' >Semr</td><td class='list' >&nbsp;</td><td class='list' >Freis.</td></tr>\
            <tr class='list odd'><td class='list'>3.7.</td><td class='list'>Fr</td><td class='list'>6B</td><td class='list'>1 - 2</td><td class='list'>Brueg</td><td class='list'>kR</td><td class='list'>B107</td><td class='list'>kR</td><td class='list'>Merz</td><td class='list'>&nbsp;</td><td class='list'>&nbsp;</td></tr>\
            <tr class='list even'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >(6C)</td><td class='list' >3 - 4</td><td class='list' >&nbsp;</td><td class='list' >---</td><td class='list' >---</td><td class='list' >E</td><td class='list' >Dewo</td><td class='list' >&nbsp;</td><td class='list' >Freis.</td></tr>\
            <tr class='list odd'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >(6C)</td><td class='list' >5</td><td class='list' >&nbsp;</td><td class='list' >---</td><td class='list' >---</td><td class='list' >B</td><td class='list' >Faus</td><td class='list' >&nbsp;</td><td class='list' >Freis.</td></tr>\
            <tr class='list even'><td class='list' ><span>3.7.</span></td><td class='list' ><span>Fr</span></td><td class='list' ><span>6D</span></td><td class='list' ><span>5</span></td><td class='list' ><span>Fehs</span></td><td class='list' ><span>E</span></td><td class='list' ><span>B108</span></td><td class='list' ><span>D</span></td><td class='list' >\
            <span>Gril</span></td><td class='list' ><span>Fr-3.7. / 3</span></td><td class='list'>&nbsp;</td></tr>\
            <tr class='list odd'><td class='list' ><span>3.7.</span></td><td class='list' ><span>Fr</span></td><td class='list' ><span>6D</span></td><td class='list' ><span>3</span></td><td class='list' ><span>Semr</span></td><td class='list' ><span>E</span></td><td class='list' ><span>B108</span></td><td class='list' ><span>E</span></td>\
            <td class='list' ><span>Fehs</span></td><td class='list' >&nbsp;</td><td class='list' ><span>Fr-3.7. / 5</span></td></tr>\
            <tr class='list even'><td class='list'>3.7.</td><td class='list'>Fr</td><td class='list'>7A, 7D</td><td class='list'>4</td><td class='list'>Buer</td><td class='list'>Sw</td><td class='list'>A007</td><td class='list'>Sw</td><td class='list'>Krem</td><td class='list'>&nbsp;</td><td class='list'>&nbsp;</td></tr>\
            <tr class='list odd'><td class='list'>3.7.</td><td class='list'>Fr</td><td class='list'>7B, 7C</td><td class='list'>4</td><td class='list'>Buch</td><td class='list'>Sm</td><td class='list'>P002</td><td class='list'>Sm</td><td class='list'>RMoh</td><td class='list'>&nbsp;</td><td class='list'>&nbsp;</td></tr>\
            <tr class='list even'><td class='list' ><span>3.7.</span></td><td class='list' ><span>Fr</span></td><td class='list' ><span>7B</span></td><td class='list' ><span>8 - 9</span></td><td class='list' ><span>---</span></td><td class='list' ><span>---</span></td><td class='list' ><span>---</span></td><td class='list' ><span>D</span></td>\
            <td class='list' ><span>Gril</span></td><td class='list' >&nbsp;</td><td class='list' ><span>Entfall</span></td></tr>\
            <tr class='list odd'><td class='list'>3.7.</td><td class='list'>Fr</td><td class='list'>8A, 8B</td><td class='list'>3</td><td class='list'>Buer</td><td class='list'>Sw</td><td class='list'>A007</td><td class='list'>Sw</td><td class='list'>Krem</td><td class='list'>&nbsp;</td><td class='list'>&nbsp;</td></tr>\
            <tr class='list even'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >8A</td><td class='list' >2</td><td class='list' >Birk</td><td class='list' >Ph</td><td class='list' >F204</td><td class='list' >KLR</td><td class='list' >Hoelz</td><td class='list' >Do-2.7. / 8</td><td class='list'>&nbsp;</td></tr>\
            <tr class='list odd'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >8A</td><td class='list' >8 - 9</td><td class='list' >---</td><td class='list' >---</td><td class='list' >---</td><td class='list' >L</td><td class='list' >Hoelz</td><td class='list' >&nbsp;</td><td class='list' >Entfall</td></tr>\
            <tr class='list even'><td class='list'>3.7.</td><td class='list'>Fr</td><td class='list'>8A</td><td class='list'>1</td><td class='list'>Birk</td><td class='list'>Ph</td><td class='list'>F204</td><td class='list'>D</td><td class='list'>RTha</td><td class='list'>&nbsp;</td><td class='list'>&nbsp;</td></tr>\
            <tr class='list odd'><td class='list' ><span>3.7.</span></td><td class='list' ><span>Fr</span></td><td class='list' ><span>8A</span></td><td class='list' ><span>4</span></td><td class='list' ><span>Boehm</span></td><td class='list' ><span>B</span></td><td class='list' ><span>F101</span></td><td class='list' ><span>Gk</span></td>\
            <td class='list' ><span>Ping</span></td><td class='list' >&nbsp;</td><td class='list' ><span>Do-2.7. / 3</span></td></tr>\
            <tr class='list even'><td class='list' ><span>3.7.</span></td><td class='list' ><span>Fr</span></td><td class='list' ><span>8A</span></td><td class='list' ><span>4</span></td><td class='list' ><span>Boehm</span></td><td class='list' ><span>B</span></td><td class='list' ><span>F101</span></td><td class='list'>&nbsp;</td><td class='list'>&nbsp;</td><td class='list'>&nbsp;</td><td class='list'>&nbsp;</td></tr>\
            <tr class='list odd'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >8B</td><td class='list' >4</td><td class='list' >Gilg</td><td class='list' >F</td><td class='list' >E203</td><td class='list' >G</td><td class='list' >Hoelz</td><td class='list' >Fr-3.7. / 9</td><td class='list'>&nbsp;</td></tr>\
            <tr class='list even'><td class='list'>3.7.</td><td class='list'>Fr</td><td class='list'>8B</td><td class='list'>5</td><td class='list'>Puesh</td><td class='list'>G</td><td class='list'>F301</td><td class='list'>G</td><td class='list'>Hoelz</td><td class='list'>&nbsp;</td><td class='list'>&nbsp;</td></tr>\
            <tr class='list odd'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >8B</td><td class='list' >8</td><td class='list' >---</td><td class='list' >---</td><td class='list' >---</td><td class='list' >F</td><td class='list' >Gilg</td><td class='list' >&nbsp;</td><td class='list' >Mo-29.6. / 4</td></tr>\
            <tr class='list even'><td class='list' >3.7.</td><td class='list' >Fr</td><td class='list' >8B</td><td class='list' >9</td><td class='list' >---</td><td class='list' >---</td><td class='list' >---</td><td class='list' >F</td><td class='list' >Gilg</td><td class='list' >&nbsp;</td><td class='list' >Fr-3.7. / 4</td></tr>\
            <tr class='list odd'><td class='list'>3.7.</td><td class='list'>Fr</td><td class='list'>8C</td><td class='list'>2</td><td class='list'>Gilg</td><td class='list'>D</td><td class='list'>E205</td><td class='list'>L</td><td class='list'>Bads</td><td class='list'>&nbsp;</td><td class='list'>&nbsp;</td></tr>\
            <tr class='list even'><td class='list'>3.7.</td><td class='list'>Fr</td><td class='list'>8C</td><td class='list'>5</td><td class='list'>Shoee</td><td class='list'>Mu</td><td class='list'>G313</td><td class='list'>Ek</td><td class='list'>Doerf</td><td class='list'>Mi-17.6. / 5</td><td class='list'>Mi-17.6. / 5</td></tr></table>"