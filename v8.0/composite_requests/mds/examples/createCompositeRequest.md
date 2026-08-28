# Examples: createCompositeRequest

**POST /__composite_requests**

## Request examples

### `application/json` — LeadRecordOperations

Create and update Leads using chained sub-requests

```json
{
  "rollback_on_fail": false,
  "parallel_execution": false,
  "__composite_requests": [
    {
      "sub_request_id": "1",
      "method": "POST",
      "uri": "/crm/v3/Leads",
      "headers": {},
      "body": {
        "data": [
          {
            "Last_Name": "Boyle"
          }
        ]
      }
    },
    {
      "sub_request_id": "2",
      "method": "PUT",
      "uri": "/crm/v3/Leads/@{1:$.data[0].details.id}",
      "headers": {},
      "body": {
        "data": [
          {
            "Company": "Zylker"
          }
        ]
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

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

### Status `207` — `application/json` — PartialSuccessResponse

Response of a partial success composite request.



```json
{
  "__composite_requests": [
    {
      "code": "SUCCESS",
      "message": "Request processed successfully",
      "status": "success",
      "details": {
        "response": {
          "headers": {
            "Content-Type": "application/json"
          },
          "body": {
            "data": "response data"
          },
          "status_code": 200
        }
      }
    },
    {
      "code": "INVALID_DATA",
      "message": "Invalid input data",
      "status": "error",
      "details": {
        "api_name": "sub_request_2",
        "json_path": "$.body.data[0].field",
        "expected_data_type": "string"
      }
    }
  ]
}
```

### Status `400` — `application/json` — CompositeRequestError

Error response for composite request with invalid data.

```json
{
  "__composite_requests": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "regex": "/crm(/.*)?/v[0-9]+([.][0-9]+)?/.*",
        "api_name": "uri",
        "json_path": "$.__composite_requests[0].uri"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
