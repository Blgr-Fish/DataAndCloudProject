from google.cloud import datastore

client = datastore.Client()

query = client.query(kind='Post')
posts = list(query.fetch())
for p in posts:
    client.delete(p.key)

print(f"{len(posts)} posts supprimés.")


# On peut vérifier depuis la datastore console que les posts ont bien été supprimés.