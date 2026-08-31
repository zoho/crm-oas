Missing required parameter during single role deletion

```json
{
  "roles": [
    {
      "status": "error",
      "code": "INVALID_DATA",
      "message": "invalid transferToId",
      "details": {
        "maximum_length": 200,
        "api_name": "name",
        "json_path": "$.roles[0].transfer_to_id"
      }
    }
  ]
}
```
