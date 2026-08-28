# Examples: deleteUnsubscribeLinksById

**DELETE /settings/unsubscribe_links/{id}**

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "unsubscribe_links": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000116037"
      },
      "message": "Unsubscribe Link deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA error: The given Unsubscribe Link ID is not part of Org

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "The given Unsubscribe Link id is not part of Org",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

NO_PERMISSION error: permission denied

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Unsubscribe_Form"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
