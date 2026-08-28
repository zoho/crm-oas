# Examples: getUnsubscribeLinks

**GET /settings/unsubscribe_links**

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "unsubscribe_links": [
    {
      "created_time": "2025-11-18T20:18:40+05:30",
      "submission_message": "",
      "modified_time": "2025-11-18T20:18:40+05:30",
      "submission_redirect_url": "",
      "page_type": "standard",
      "custom_location_url": "",
      "modified_by": {
        "name": "Kk",
        "id": "111111000000057843"
      },
      "name": "Default",
      "id": "111111000000115014",
      "created_by": {
        "name": "Kk",
        "id": "111111000000057843"
      },
      "standard_page_message": null,
      "submission_action_type": "display_message"
    }
  ]
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
