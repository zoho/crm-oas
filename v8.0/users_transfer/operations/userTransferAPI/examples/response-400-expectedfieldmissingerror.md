An example error response of a missing required fields.

```json
{
  "transfer": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_data": [
          {
            "api_name": "transfer",
            "json_path": "$.transfer.transfer"
          },
          {
            "api_name": "move_subordinate",
            "json_path": "$.transfer.move_subordinate"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
