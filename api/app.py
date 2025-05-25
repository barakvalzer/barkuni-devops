
from flask import Flask, jsonify
from kubernetes import client, config
import os

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Barkuni Corp REST API!"

@app.route('/pods')
def list_pods():
    try:
        config.load_incluster_config()
    except:
        config.load_kube_config()
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace="kube-system")
    return jsonify([pod.metadata.name for pod in pods.items])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
