# Examples: createBulkWriteJob

**POST /write**

## Request examples

### `application/json` — BulkWriteRequest

Bulk write request with one resource and one field mapping

```json
{
  "operation": "insert",
  "callback": {
    "url": "http://requestbin.fullcontact.com/1fcimk51",
    "method": "post"
  },
  "resource": [
    {
      "type": "data",
      "file_names": [
        "data.csv"
      ],
      "module": {
        "api_name": "Contacts"
      },
      "file_id": "3524001000005697001",
      "find_by": "id",
      "field_mappings": [
        {
          "api_name": "Last_Name",
          "index": 0
        }
      ]
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — SuccessResponse

Successful bulk write job creation

```json
{
  "status": "success",
  "code": "SUCCESS",
  "message": "success",
  "details": {
    "id": "3524001000005697001",
    "created_by": {
      "id": "3524001000000186003"
    }
  }
}
```

### Status `400` — `application/json` — InvalidCallbackUrlError

INVALID_CALLBACK_URL error for an unreachable callback

```json
{
  "code": "INVALID_CALLBACK_URL",
  "details": {},
  "message": "Invalid callback URL provided",
  "status": "error"
}
```
