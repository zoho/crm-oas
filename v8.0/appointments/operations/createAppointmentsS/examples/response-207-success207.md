207 with one MANDATORY_NOT_FOUND failure and one success.

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "data",
        "json_path": "$.data[0].data"
      },
      "message": "required field not found",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "generated_id_0"
      },
      "message": "Proper success message",
      "status": "success"
    }
  ]
}
```
