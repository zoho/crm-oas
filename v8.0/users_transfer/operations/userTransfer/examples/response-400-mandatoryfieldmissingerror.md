An example of a missing id field inside the transfer object.

```json
{
  "transfer_and_delete": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.transfer_and_delete.transfer.id",
        "parent_api_name": "transfer"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```
