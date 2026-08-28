# Examples: getDealContactRoleForContact

**GET /{module}/{dealId}/Contact_Roles/{contactId}**

## Parameter examples

### `fields` (query) — BasicFields

Basic contact fields

```json
"First_Name,Last_Name,Email"
```

## Response examples

### Status `200` — `application/json` — ContactRoleForContactResponse

```json
{
  "data": [
    {
      "Owner": {
        "name": "luffy",
        "id": "4408068000000623001",
        "email": "luffy@zohotest.com"
      },
      "Department": null,
      "Contact_Role": {
        "name": "Developer/Evaluator",
        "id": "4408068000000007170"
      },
      "Email": null,
      "id": "4408068000000963425"
    }
  ]
}
```

### Status `500` — `application/json` — ErrorExample

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
