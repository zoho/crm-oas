# Examples: putFieldsWithId

**PATCH /settings/fields/{fieldId}**

## Request examples

### `application/json` — FullExample

Example of a field update for the Leads module

```json
{
  "fields": [
    {
      "history_tracking_enabled": true,
      "history_tracking": {
        "related_list_name": "Region Tracker",
        "duration_configuration": "time",
        "followed_fields": [
          {
            "api_name": "Owner",
            "_delete": null
          },
          {
            "api_name": "Company",
            "id": "5725767000000002591"
          }
        ]
      }
    },
    {
      "id": "2276164000002053013",
      "pick_list_values": [
        {
          "id": "2276164000002053012",
          "_global_picklist_value": {
            "id": "2276164000002053039"
          }
        },
        {
          "id": "2276164000002053014",
          "_global_picklist_value": {
            "id": "2276164000002053041"
          }
        }
      ],
      "global_picklist": {
        "api_name": "Market",
        "id": "2276164000002053035"
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — FullExample

Example response of a text field update for the Leads module

```json
{
  "fields": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000067259"
      },
      "message": "field updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — SingleError

Invalid module

```json
{
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {},
  "status": "error"
}
```

### Status `400` — `application/json` — FieldErrors

Invalid field data

```json
{
  "fields": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "expected_data_type": "ArrayList",
        "api_name": "group",
        "json_path": "$.fields[0].lookup.query_details.criteria.group"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FieldIndexedEncryptNotAllowed

Indexed field cannot be encrypted

```json
{
  "fields": [
    {
      "code": "NOT_ALLOWED",
      "message": "Indexed field cannot be encrypted",
      "details": {
        "api_name": "crypt",
        "json_path": "$.fields[0].crypt"
      },
      "status": "error"
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
