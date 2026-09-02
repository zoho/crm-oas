```json
{
  "transfer_pipeline": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "from",
        "exists_in": {
          "json_path": "$.transfer_pipeline[0].stages[0].from"
        },
        "json_path": "$.transfer_pipeline[0].stages[1].from"
      },
      "message": "from id is mapped more than once",
      "status": "error"
    }
  ]
}
```
