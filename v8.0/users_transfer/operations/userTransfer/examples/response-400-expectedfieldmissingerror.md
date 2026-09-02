An example of missing required fields in the request.

```json
{
  "transfer_and_delete": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_data": [
          {
            "api_name": "transfer",
            "json_path": "$.transfer_and_delete.transfer"
          },
          {
            "api_name": "move_subordinate",
            "json_path": "$.transfer_and_delete.move_subordinate"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
