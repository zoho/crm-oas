# Examples: deleteCustomField

**DELETE /settings/fields/{fieldId}**

## Response examples

### Status `200` — `application/json` — FullExample

Successful deletion of a single custom field

```json
{
  "fields": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000067259"
      },
      "message": "field deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — ErrorExample

```json
{
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {},
  "status": "error"
}
```

### Status `400` — `application/json` — FieldUsedInIndex

Field is part of an active index and cannot be deleted

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "The custom field has already used in other places",
  "status": "error"
}
```

### Status `401` — `application/json` — ErrorExample

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `403` — `application/json` — ErrorExample

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Customize_Zoho_CRM"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```

### Status `404` — `application/json` — ErrorExample

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```

### Status `500` — `application/json` — ErrorExample

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Please check logs for internal error",
  "details": {},
  "status": "error"
}
```
