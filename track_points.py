"""Fetch Rewards Points server.

Tracking points to use per payer/partner in each user's profile based on following rules:
1. Spend the oldest points first
2.No payer's points to go negative

"""
import json
from datetime import datetime
from flask import request, render_template,redirect
from flask import Flask
import json

app = Flask(__name__)

all_trans=[] # a list map {'payer': xx, 'points': yy, 'timestamp':zz}
tx_by_payer = {} # a map of list of map {'payer' : [{tx},{tx},{tx}]}
pts_by_payer ={} # a map of pts {'payer' : pts }

@app.route('/')
def homepage():
    """View homepage."""

    return render_template("homepage.html")

@app.route('/add_points',methods=['POST'])
def add_transaction(): 
    payer=request.form['payer']
    pts=int(request.form['points'])
    ts=request.form['timestamp']

    transaction = {'payer':payer,'points':pts,'timestamp':ts}
    if pts > 0:
        if payer not in pts_by_payer: 
            pts_by_payer[payer]=pts
        else:
            pts_by_payer[payer]+=pts
        all_trans.append(transaction)
    # if negative points, subtract points from payer txs
    elif pts < 0:
        # if no existing pts by this payer or insufficient pts, return unsuccessful add tx
        if payer not in pts_by_payer or pts_by_payer[payer]+pts<0:
            print("error: cannot add this transaction, payer insufficient balance")
            return homepage()
        else:
            all_trans.sort(key=lambda x:x['timestamp'])
            print(pts_by_payer)
            for tx in all_trans[:]:
                if(tx['payer']!=payer):
                    continue
                else:
                    if tx['points']+pts > 0:
                        tx.update({'points':tx['points']+pts})
                        pts_by_payer[payer]+=pts
                        break
                    elif tx['points']+pts <= 0:
                        pts+=tx['points']
                        pts_by_payer[payer]-=tx['points']
                        all_trans.remove(tx)
    print(all_trans, f'Points have added to account')
    return (pts_by_payer)
   
@app.route('/spend_points',methods=['POST'])
def spend_points_in_account():
    points_to_spend = int(request.form['points'])
    pts_total = 0
    for payer,pts in pts_by_payer.items():
        pts_total += pts
    if pts_total < points_to_spend:
        print('insufficient points')
        return redirect("/")
    all_trans.sort(key=lambda x:x['timestamp'])
    print(all_trans)
    result_lst=[]
    for tx in all_trans[:]:
        payer=tx['payer']
        if points_to_spend ==0:
            break
        if tx['points']-points_to_spend > 0:
            tx.update({'points':tx['points']-points_to_spend})
            pts_by_payer[payer]-=points_to_spend
            result_lst.append({'payer':tx['payer'], 'points':-1*points_to_spend})
            points_to_spend=0
        elif tx['points']-points_to_spend <= 0:
            points_to_spend-=tx['points']
            pts_by_payer[payer]-=tx['points']
            result_lst.append({'payer':tx['payer'], 'points':-1*tx['points']})
            all_trans.remove(tx)
    print(result_lst)
    return json.dumps(result_lst)
        
           
@app.route('/show_balance', methods=['POST'])
def show_balance_lst():
    
    total_pts=0
    for k,v in pts_by_payer.items():
        total_pts+=v
    print(pts_by_payer)
    return json.dumps(pts_by_payer)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
