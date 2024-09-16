import requests
from google.cloud import bigquery
from google.oauth2 import service_account
import json
from google.cloud.exceptions import NotFound  # 追加

# リフレッシュトークンを用いてIDトークンを取得する関数
def get_id_token(refresh_token):
    url = "https://api.jquants.com/v1/token/auth_refresh"
    params = {"refreshtoken": refresh_token}
    response = requests.post(url, params=params)
    return response.json().get("idToken")

# IDトークンを取得
refresh_token = "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.pfhg0PRRgQ7YQkPVXhkABM3KW_Xlex4T6OUSrvlpotPnuGc3mMiMow52muJHzHncnZkqtcwUQXh5iCelAdeG96xZ08_DygHAwOnV-wx1Msdra8um7NAgfeLOmcOAxriSia6aZhSuOERfe5dvlLBg_vJS2EOZqm8gIkQzonn-NfXEBrfvidTFaWoFsm02-4rI3EgagS9MqSyjr0XCltBAqp0EPz1ACZ49Sl5P3MCHeRwZATwfcJMVjVbjVPUCtioPhyO862cEM1vwc3VnC7u4WjUBvCqbA-mmGFf3m7vzYrAT0Fv6xh7ycJJ473h9CXES9tHuFo3vuWs2gonyYI_tPw.iafhHNPXi-LrHozl.QlwxbL3n9N5j9Tk0xf8-sXhNIqBhbbwliVJTNtYFGueuyVIPR3YGvJs9JLiZ-1fXQS3eDBgUObACPUkOVH62CTDJ_sZ6jhIoVluvSY_LOEPv2oq1LMGIeB1DI069jdSTlHxG1n_antbb0g1pVE73q8s39nS_1oJ621OB-A00QG-Suv3qkTdgRifuMgOWNGon-q7Xx0xC0QWjzBetM3fi89GmE20t3uwDahg9tlxhmrfV_6cjSux6ZiSceR0fi3WyvvknavmhiROw6D1e4tEUmOd1ApSejZ0ytusDTmqv0Jsuqqnmfzoiu2Ne-qFRT6VmLTY0teRpBKNNW9cQNyS_WmcXTCCJ7uihThepQdIHWfXk1f3Hc3DR8di8gusgg_ZcMo2wPibU0feTtDeUFJAiFmGYWc3lRe0z_Kpn1N6XlGRdnyQcQyVXSznphRdMuB0lzxNTGqarYrLMgQ9Q18vIapMYnsPZCd-PeCBBlTWtyBJdXzZHJqMwIF884faBI8nDe32Y_0OknQc3lj7xdl6ty4XuOVMGj5QbSrOYhh1EKrmtp9COvcOrvaRjRiUVSXLQu2PFGAi8WbUk9WwBTXFUhfNRVODLCiM8UeLBWNoCKKxYY-5hNZtkCrJfAbFPSUKef8YgF7ooNn-4tJhNXkQPTqxDuPrF_i_ZZgRyXzRyNr2zLACvsmEgZAl1CBW9v3uOH2fXFy1iDnjZCMYpVpThsD3ZQSFnXbsgTnWi1J-5m07CxVW56tME08MJEGYXWCOpmqHDUuDS-Wqr7P1xBp_NwuSr5QGuWa0yXgKOK5GMPdfuYUmQvwxkMxkMCBlc9hE0_T_-4QXsZWHzOFyR9N2LbSTMdTZUFTEXPAEiBjPO8z48bYyJLkEgdEiDQAX6-65lzPXbg_JfdjnVufowiprhDgL291zrLu_rWNrNjGLDh2Xy8PXyu1PycE6_9XTdZJKofgpsqWBj1RuhxLi9gdZFIeLyBnR5y2HUiKXD5VjeKEBet_JdJ7Cb-fpyU_t5QmH1qxyCG5U2mF_qeT2diPQ_vLQt-X4egIe2xbw-_-uAdy1js9FOhQu3jOaMWlvA-ZyW6W6qwAp4M25p1d7xSZzBZUGFHpNwbyriDajubQeKSDJi-DhvhBSg-KxyJf5Ly3GjqlzaPMvtguzh9fIZHOaNSjfEIV3ga961zP-1igXp45hRf6Z6ztEOULpUoANhQva2lVBbhYjD6_2V4seej119SSo1kS_iPvurP1t28cq7yraICzE4AiQb2aakIHdRSlDTF7In-5aF9Ius2g6g_yrjcf7FUlByuBjv5mRUk0R8u9ZEzK2Ps6irlVKp1i-prHWTMK4ZCEAf-9fixw.MvlxHaEKUP5n09i2QRbI1g"
id_token = get_id_token(refresh_token)

# J-Quants APIのエンドポイント
url = "https://api.jquants.com/v1/fins/announcement"

# 認証情報
headers = {
    "Authorization": "Bearer {}".format(id_token)
}

# APIリクエストを送信
response = requests.get(url, headers=headers)
data = response.json()

# デバッグメッセージ
print(f"Initial fetch: {len(data['announcement'])} announcements")

# ページネーション対応
while "pagination_key" in response.json():
    pagination_key = response.json()["pagination_key"]
    response = requests.get(f"{url}?pagination_key={pagination_key}", headers=headers)
    data['announcement'] += response.json()["announcement"]
    # デバッグメッセージ
    print(f"Fetched {len(response.json()['announcement'])} more announcements")

# 総件数をデバッグメッセージとして出力
print(f"Total announcements fetched: {len(data['announcement'])}")

# BigQueryのクライアントを作成
from google.auth import default
credentials, project = default()
client = bigquery.Client(credentials=credentials, project='ynquant')

# データセットとテーブルの参照を作成
dataset_id = 'jquants'
table_id = 'announcement'
dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)

# スキーマの定義を動的に取得
schema = []
for field in data['announcement'][0].keys():
    schema.append(bigquery.SchemaField(field, "STRING"))

# テーブルが存在するか確認し、存在しない場合は作成
try:
    client.get_table(table_ref)  # テーブルが存在するか確認
    print(f"Table {table_ref} already exists. Deleting and recreating the table.")
    client.delete_table(table_ref, not_found_ok=True)  # テーブルを削除
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)  # 新しいテーブルを作成
    print(f"Recreated table {table.project}.{table.dataset_id}.{table.table_id}")
except NotFound:
    print(f"Table {table_ref} not found. Creating new table.")
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)  # 新しいテーブルを作成
    print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}")

# テーブルが存在するか確認するコードを追加
try:
    client.get_table(table_ref)
    print("Table exists.")
except NotFound:
    print("Table not found.")

# デバッグ用にテーブル名を出力
print(f"Inserting into table: {table_ref}")

# データを挿入
rows_to_insert = data['announcement']
errors = client.insert_rows_json(table_ref, rows_to_insert)

if errors == []:
    print("New rows have been added.")
    # デバッグメッセージ
    print(f"Total {len(rows_to_insert)} announcements inserted")
else:
    print("Encountered errors while inserting rows: {}".format(errors))

