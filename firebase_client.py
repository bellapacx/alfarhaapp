import os, json
import firebase_admin
from firebase_admin import credentials, firestore

print(">>> firebase_admin_setup.py loaded")

# Load from environment variable
service_json = json.loads(os.environ["FIREBASE_SERVICE_JSON"])
cred = credentials.Certificate(service_json)
firebase_admin.initialize_app(cred)

db = firestore.client()
