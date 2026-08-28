# Examples: deleteTags

**DELETE /settings/tags/{id}**

## Response examples

### Status `200` — `application/json` — Success200

Successful response for tag deletion

```json
{
  "tags": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000071739"
      },
      "message": "tags deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRequestMethodResponse1

Error response for invalid HTTP method

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response for tag not found

```json
{
  "code": "INVALID_DATA",
  "details": {
    "id": "111111000000071739"
  },
  "message": "tags not found",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response for insufficient permissions

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Tags_Leads",
      "Crm_Implied_Edit_Leads"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidUrlPatternResponse1

Error response for invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```
