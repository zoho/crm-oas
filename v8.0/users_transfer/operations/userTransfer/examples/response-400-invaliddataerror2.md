An example error response of deleted transfer target user request.

```json
{
  "transfer_and_delete": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.transfer_and_delete.transfer.id",
        "owner_status": "deleted"
      },
      "message": "The user to whom you are trying to transfer is deleted.",
      "status": "error"
    }
  ]
}
```
