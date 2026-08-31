Batch response with both successful and failed draft updates

```json
{
  "__email_drafts": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "bb08599ae908a3fc514349239ebd0dbf82a1fd0b60a7902244cf0ee6b52a88d1"
      },
      "message": "Draft updated Successfully",
      "status": "success"
    },
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "from",
        "json_path": "$.__email_drafts[1].from"
      },
      "message": "required field not found",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "bb08599ae908a3fc514349239ebd0dbf82a1fd0b60a7902244cf0ee6b52a88d1"
      },
      "message": "Draft updated Successfully",
      "status": "success"
    }
  ]
}
```
