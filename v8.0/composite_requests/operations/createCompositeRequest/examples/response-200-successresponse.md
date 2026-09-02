Response of a successful Composite Request.

```json
{
  "__composite_requests": [
    {
      "code": "SUCCESS",
      "message": "composite sub request executed successfully",
      "status": "success",
      "details": {
        "response": {
          "headers": {
            "content-type": "application/json;charset=UTF-8",
            "server": "ZGS",
            "date": "Tue, 25 Nov 2025 10:55:31 GMT"
          },
          "body": {
            "data": [
              {
                "code": "SUCCESS",
                "details": {
                  "Modified_Time": "2025-11-24T22:55:30-12:00",
                  "Modified_By": {
                    "name": "User",
                    "id": "2284048000000471001"
                  },
                  "Created_Time": "2025-11-24T22:55:30-12:00",
                  "id": "2284048000005238359",
                  "Created_By": {
                    "name": "User",
                    "id": "2284048000000471001"
                  }
                },
                "message": "record added",
                "status": "success"
              }
            ]
          },
          "status_code": 201
        }
      }
    }
  ]
}
```
