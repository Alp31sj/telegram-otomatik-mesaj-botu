from pyrogram import Client

api_id = #my.telegrm.org tan aldıgınız apı id
api_hash = 'my.telegrm.org tan aldıgınız apı id'

with Client(":memory:", api_id, api_hash) as app:
    print(app.export_session_string())
