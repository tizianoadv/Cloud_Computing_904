from flask import Flask, request, jsonify, render_template
import redis

app = Flask(__name__)

# connect to Redis database
redis_host = "redis-service"
redis_port = 6379
redis_password = ""
redis_db = 0
redis_conn = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=redis_db)

@app.route('/flush', methods=['GET'])
def flush_db():
    redis_conn.flushdb()
    return jsonify({'message': 'DB flush successfully.'}), 200

# POST endpoint to receive data and store it to Redis database
@app.route('/data', methods=['POST'])
def post_data():
    payload = request.json
    data = {
        'temperature': str(payload['temperature']),
        'humidity': str(payload['humidity']),
        'luminosity': str(payload['luminosity']),
        'timestamp': str(payload['timestamp'])
    }
    redis_conn.hmset(data['timestamp'], data)
    return jsonify({'message': 'Data stored successfully.'}), 200   

# GET endpoint to fetch data from Redis database and transmit it to user's browser
@app.route('/data', methods=['GET'])
def get_data():
    data = {}
    for key in redis_conn.scan_iter():
        key_str = key.decode()
        data[key_str] = {k.decode(): v.decode() for k, v in redis_conn.hgetall(key).items()}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
