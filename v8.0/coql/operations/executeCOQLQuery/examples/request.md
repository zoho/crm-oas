### `application/json` — GetLeads

COQL query to retrieve Leads records

```json
{
  "select_query": "select Last_Name, First_Name from Leads where Last_Name = 'Smith'"
}
```

### `application/json` — GetLeadsWithFieldMetadata

COQL query to retrieve Leads records with field metadata

```json
{
  "select_query": "select Last_Name from Leads where Last_Name = 'TestLead'",
  "include_meta": [
    "fields"
  ]
}
```
