Dependent transfer_to_id missing error when territory has child territories

```json
{
  "territories": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "transfer_to_id",
        "json_path": "$.territories[0].transfer_to_id",
        "dependee": {
          "api_name": "id",
          "json_path": "$.territories[0].id"
        }
      },
      "message": "This territory has its child. Please Give the transfer_to_id field value",
      "status": "error"
    }
  ]
}
```
