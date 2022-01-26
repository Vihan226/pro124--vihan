from flask import Flask,jsonify,request

app = Flask(__name__)
tasks= [{
            'id': 1, 
            'Contact':'90238490238',
            'Name':'someone',
            'done':False
        },   
        
        {

            'id': 2, 
            'Contact':u'90482309',
            'Name':u'someoneanother',
            'done':False
        }]
@app.route('/add-data', methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({

            'status':'error',
            'message':'please please please provide the data',

        }, 400)

    contact ={
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact', ""),
        'done':False
    }

    tasks.append(contact)

    return jsonify({
        
            'status':'success',
            'message':'task added successfully',


    })

@app.route('/get-data')

def get_tasks():
    return jsonify({

        'data':tasks
    })

if (__name__=='__main__'):
    app.run(debug= True)

