# Examples: deleteVariables

**DELETE /settings/variables**

## Response examples

### Status `207` — `application/json` — Success207

Success response for status 207

```json
{
  "variables": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111114000000454011"
      },
      "message": "variable deleted",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111114000000454008"
      },
      "message": "variable deleted",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "234576960"
      },
      "message": "variable not deleted",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: invalid data (Field: variables)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "variables",
    "json_path": "$.variables"
  },
  "message": "invalid data",
  "status": "error"
}
```
