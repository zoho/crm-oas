Partial success - first module succeeds, second fails with missing required ID

```json
{
  "modules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000002654"
      },
      "message": "module updated successfully",
      "status": "success"
    },
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.modules[1]"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```
