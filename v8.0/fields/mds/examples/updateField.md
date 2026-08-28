# Examples: updateField

**PATCH /settings/fields**

## Request examples

### `application/json` — FullExample

Bulk update of multiple field configurations

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
    },
    {
      "id": "2276164000002053013",
      "field_label": "Updated Field Label",
      "length": 255,
      "association_details": {
        "related_field": {
          "id": "4832675000000710341",
          "api_name": "City"
        },
        "lookup_field": {
          "id": "4832675000000710334",
          "api_name": "Lookup_Field"
        }
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — FullExample

All requested fields updated successfully

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
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "11111200000006724"
      },
      "message": "field updated",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000067239"
      },
      "message": "field updated",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccess

Partial success - one field updated, one failed

```json
{
  "fields": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "1947368000002460003"
      },
      "message": "field updated",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "data_type",
        "json_path": "$.fields[1].data_type"
      },
      "message": "invalid data",
      "status": "error"
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
      "message": "invalid data",
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
