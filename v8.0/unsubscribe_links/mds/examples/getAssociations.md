# Examples: getAssociations

**GET /settings/unsubscribe_link/actions/associations**

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "associations": [
    {
      "id": "111111000000116043",
      "associated_places": [
        {
          "resource": {
            "name": "Asd",
            "id": "111111000000116051"
          },
          "details": {
            "module": {
              "api_name": "Leads",
              "id": "111111000000002652"
            }
          },
          "type": "email_templates"
        }
      ]
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
