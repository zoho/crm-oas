# Examples: deleteContactRoleRelation

**DELETE /{module}/{dealId}/Contact_Roles/{contactId}**

## Response examples

### Status `200` — `application/json` — DeleteSingleRelationSuccess

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4408068000000963455"
      },
      "message": "relation removed",
      "status": "success"
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
