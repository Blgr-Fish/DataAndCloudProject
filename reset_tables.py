from google.cloud import datastore

client = datastore.Client()

TABLES = ["Post", "User"]

for table in TABLES:
    print(f"Suppression des entités pour {table}…")

    query = client.query(kind=table)
    query.keys_only()

    batch = []
    count = 0

    for entity in query.fetch():
        batch.append(entity.key)
        count += 1

        # delete par batch de 500 (limite GCP)
        if len(batch) == 500:
            client.delete_multi(batch)
            batch = []

    # delete le dernier batch
    if batch:
        client.delete_multi(batch)

    print(f"{count} entités supprimées de {table}.")
