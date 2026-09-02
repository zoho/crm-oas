### `application/json` — BulkWriteRequest

Bulk write request with one resource and one field mapping

```json
{
  "operation": "insert",
  "callback": {
    "url": "http://requestbin.fullcontact.com/1fcimk51",
    "method": "post"
  },
  "resource": [
    {
      "type": "data",
      "file_names": [
        "data.csv"
      ],
      "module": {
        "api_name": "Contacts"
      },
      "file_id": "3524001000005697001",
      "find_by": "id",
      "field_mappings": [
        {
          "api_name": "Last_Name",
          "index": 0
        }
      ]
    }
  ]
}
```
