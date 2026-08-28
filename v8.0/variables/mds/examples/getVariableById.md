# Examples: getVariableById

**GET /settings/variables/{id}**

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "variables": [
    {
      "api_name": "Variable1",
      "name": "Variable1",
      "description": "This denotes variable 1 description",
      "id": "40000000047003",
      "type": "text",
      "variable_group": {
        "api_name": "Group1",
        "id": "40000000047001"
      },
      "value": "This denotes variable one value",
      "source": "crm"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: Invalid data

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": " group_id"
  },
  "message": "Invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidUrlPatternResponse1

Error response with code INVALID_URL_PATTERN: Please check if the URL trying to access is a correct one

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: Invalid ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "invalid data",
  "status": "error"
}
```
