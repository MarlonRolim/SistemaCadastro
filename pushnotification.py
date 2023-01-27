from app import *
from pywebpush import webpush, WebPushException 

import requests

    


@server.route('/')
def index():
    
    return redirect('/app')


@server.route('/notification')
def notification():
    if current_user.is_authenticated:
        
        return render_template('index.html')
    else:
        return redirect("/app/login")



@server.route("/subscription/", methods=["GET", "POST"])
def subscription():
    if request.method == "POST":
         # Obtem o token de inscricao enviado pelo Service Worker
        subscription_token = request.get_json()
        user = int(current_user.id)
        dados = json.loads(requests.get(f'https://appcadastro-rb-default-rtdb.firebaseio.com/notification_keys/.json?orderBy="/id_user"&equalTo={user}').text)
        if dados == {}:
            dados = {'id_user': user,
                    'key': subscription_token
                    }
            requests.post(f'https://appcadastro-rb-default-rtdb.firebaseio.com/notification_keys/.json', data=json.dumps(dados))
        else:
            for i in dados.keys(): id = i
            requests.patch(f'https://appcadastro-rb-default-rtdb.firebaseio.com/notification_keys/{id}/key/.json', data=json.dumps(subscription_token))
        
            
        return Response("deu certo")

    if request.method == "GET":
        
        
        return Response(response=json.dumps({"public_key": VAPID_PUBLIC_KEY}),
            headers={"Access-Control-Allow-Origin": "*"}, content_type="serverlication/json")

    subscription_token = request.get_json("subscription_token")
    user = current_user.id
    df = pd.DataFrame(columns=["id_user"])
    df['id_user'] = user
    df['key'] = subscription_token
    df.to_sql('log_alteracao', schema='public', if_exists='append', con=create_connection() )
    return Response(status=201, mimetype="serverlication/json")

@server.route("/push_v1/",methods=['POST'])
def push_v1():
    message = "Push Test v1"
    print("is_json",request.is_json)

    if not request.json or not request.json.get('sub_token'):
        return jsonify({'failed':1})

    print("request.json",request.json)

    token = request.json.get('sub_token')
    try:
        token = json.loads(token)
        send_web_push(token, message)
        return jsonify({'success':1})
    except Exception as e:
        print("error",e)
        return jsonify({'failed':str(e)})