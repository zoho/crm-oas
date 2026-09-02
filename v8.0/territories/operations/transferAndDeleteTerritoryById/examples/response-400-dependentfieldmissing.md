DEPENDENT_FIELD_MISSING error when transfer_to_id is absent

```json
{
  "territories": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "transfer_to_id",
        "json_path": "$.territories[0].transfer_to_id",
        "dependee": {
          "resource_path_index": 2
        }
      },
      "message": "This territory has its child. Please Give the transfer_to_id field value",
      "status": "error"
    }
  ]
}
```
