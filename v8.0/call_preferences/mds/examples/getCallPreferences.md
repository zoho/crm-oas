# Examples: getCallPreferences

**GET /settings/call_preferences**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Retrieved Call Preferences with both fields enabled

```json
{
  "call_preferences": {
    "show_from_number": true,
    "show_to_number": true
  }
}
```

### Status `403` — `application/json` — NoPermission

None

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
