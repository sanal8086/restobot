import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from firebase_client import get_db

db_ref = get_db()
res = db_ref.child('restaurants').get()
if res:
    res_id = list(res.keys())[0]
    items = db_ref.child(f'restaurants/{res_id}/items').get()
    rolls = [v for k, v in items.items() if 'Roll' in v['name']]
    for r in rolls:
        print(f"Item: {r['name']}, Image: {r.get('image_url')}")
