# Examples: postReplacePickListValues

**POST /settings/fields/{fieldId}/actions/replace_pick_list_values**

## Parameter examples

### `module` (query) — Leads

Leads module

```json
"Leads"
```

### `module` (query) — Contacts

Contacts module

```json
"Contacts"
```

### `module` (query) — Accounts

Accounts module

```json
"Accounts"
```

### `module` (query) — Deals

Deals module

```json
"Deals"
```

### `fieldId` (path) — StandardField

Example field ID

```json
"1629307000006596211"
```

## Request examples

### `application/json` — SamplePostRequest

Sample request body

```json
{
  "replace_pick_list_values": [
    {
      "old_value": {
        "id": "1111130000001470910",
        "display_value": "Option 1"
      },
      "new_value": {
        "id": "1111130000001470030",
        "display_value": "Option 2"
      },
      "delete_old_value": true
    }
  ]
}
```

## Response examples

### Status `202` — `application/json` — Success202

Success response for status 202

```json
{
  "replace_pick_list_values": [
    {
      "code": "SCHEDULED",
      "details": {
        "job_id": "2423488000000732044"
      },
      "message": "Picklist option replace operation scheduled successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: The Field Id is Invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "The Field Id is Invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: invalid data type replace_pick_list_values object (Field: replace_pick_list_values)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "replace_pick_list_values",
    "json_path": "$.replace_pick_list_values"
  },
  "message": "invalid data type replace_pick_list_values object",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response with code INVALID_DATA: The id given in old_value is invalid (Field: id)

```json
{
  "replace_pick_list_values": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.replace_pick_list_values[0].old_value.id"
      },
      "message": "The id given in old_value is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response with code INVALID_DATA: The id given in new_value is invalid (Field: id)

```json
{
  "replace_pick_list_values": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.replace_pick_list_values[0].new_value.id"
      },
      "message": "The id given in new_value is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

Error response with code INVALID_MODULE: the module name given seems to be invalid

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "param_name": "module"
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse1

Error response with code NOT_ALLOWED: The picklist option is used in features (Field: id)

```json
{
  "replace_pick_list_values": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.replace_pick_list_values[0].old_value.id",
        "_associations": [
          {
            "resources": [
              {
                "name": "Lead Nurturing blueprint",
                "id": "1560451000004719301",
                "_details": null
              }
            ],
            "type": "blueprint"
          },
          {
            "resources": [
              {
                "name": "CadenceTest1",
                "id": "1560451000004719986",
                "_details": null
              }
            ],
            "type": "cadences"
          }
        ]
      },
      "message": "The picklist option is used in features",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse2

Error response with code NOT_ALLOWED: Global picklist option cannot be replaced (Field: id)

```json
{
  "replace_pick_list_values": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.replace_pick_list_values[0].old_value.id"
      },
      "message": "Global picklist option cannot be replaced",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse3

Error response with code NOT_ALLOWED: Restricted Option cannot be replaced (Field: id)

```json
{
  "replace_pick_list_values": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.replace_pick_list_values[0].old_value.id"
      },
      "message": "Restricted Option cannot be replaced",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

Error response with code REQUIRED_PARAM_MISSING: One of the expected parameter is missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — ExpectedFieldMissingResponse1

Error response with code EXPECTED_FIELD_MISSING: specify atleast one field

```json
{
  "replace_pick_list_values": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.replace_pick_list_values[0].new_value.id"
          },
          {
            "api_name": "display_value",
            "json_path": "$.replace_pick_list_values[0].new_value.display_value"
          }
        ]
      },
      "message": "specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingResponse2

Error response with code EXPECTED_FIELD_MISSING: specify atleast one field

```json
{
  "replace_pick_list_values": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.replace_pick_list_values[0].old_value.id"
          },
          {
            "api_name": "display_value",
            "json_path": "$.replace_pick_list_values[0].old_value.display_value"
          }
        ]
      },
      "message": "specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingResponse1

Error response with code AMBIGUITY_DURING_PROCESSING: ambiguity while processing the old_value

```json
{
  "replace_pick_list_values": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.replace_pick_list_values[0].old_value.id"
          },
          {
            "api_name": "display_value",
            "json_path": "$.replace_pick_list_values[0].old_value.display_value"
          }
        ]
      },
      "message": "ambiguity while processing the old_value",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingResponse2

Error response with code AMBIGUITY_DURING_PROCESSING: ambiguity while processing the new_value

```json
{
  "replace_pick_list_values": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.replace_pick_list_values[0].new_value.id"
          },
          {
            "api_name": "display_value",
            "json_path": "$.replace_pick_list_values[0].new_value.display_value"
          }
        ]
      },
      "message": "ambiguity while processing the new_value",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse1

Error response with code DEPENDENT_MISMATCH: old_value and new_value should not be the same (Field: new_value)

```json
{
  "replace_pick_list_values": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "old_value",
          "json_path": "$.replace_pick_list_values[0].old_value"
        },
        "api_name": "new_value",
        "json_path": "$.replace_pick_list_values[0].new_value"
      },
      "message": "old_value and new_value should not be the same",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response with code MANDATORY_NOT_FOUND: old_value is mandatory (Field: old_value)

```json
{
  "replace_pick_list_values": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "old_value",
        "json_path": "$.replace_pick_list_values[0].old_value"
      },
      "message": "old_value is mandatory",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Error response with code MANDATORY_NOT_FOUND: new_value is mandatory (Field: new_value)

```json
{
  "replace_pick_list_values": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "new_value",
        "json_path": "$.replace_pick_list_values[0].new_value"
      },
      "message": "new_value is mandatory",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Error response with code INVALID_DATA: The display_value given in new_value is invalid (Field: display_value)

```json
{
  "replace_pick_list_values": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "display_value",
        "json_path": "$.replace_pick_list_values[0].new_value.display_value"
      },
      "message": "The display_value given in new_value is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Error response with code INVALID_DATA: The delete_old_value boolean field type mismatch (Field: delete_old_value)

```json
{
  "replace_pick_list_values": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "boolean",
        "api_name": "delete_old_value",
        "json_path": "$.replace_pick_list_values[0].delete_old_value"
      },
      "message": "The delete_old_value boolean field type mismatch",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

Error response with code INVALID_DATA: old_value expected data type invalid (Field: old_value)

```json
{
  "replace_pick_list_values": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "jsonobject",
        "api_name": "old_value",
        "json_path": "$.replace_pick_list_values[0].old_value"
      },
      "message": "old_value expected data type invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

Error response with code INVALID_DATA: new_value expected data type invalid (Field: new_value)

```json
{
  "replace_pick_list_values": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "jsonobject",
        "api_name": "new_value",
        "json_path": "$.replace_pick_list_values[0].new_value"
      },
      "message": "new_value expected data type invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FeatureNotSupportedResponse1

Error response with code FEATURE_NOT_SUPPORTED: Your License does not support this feature

```json
{
  "code": "FEATURE_NOT_SUPPORTED",
  "details": {},
  "message": "Your License does not support this feature",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse5

Error response with code NOT_ALLOWED: Cannot delete old_value for a picklist field

```json
{
  "replace_pick_list_values": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "delete_old_value",
        "json_path": "$.replace_pick_list_values[0].delete_old_value"
      },
      "message": "Cannot delete old_value for a picklist field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

Error response with code INVALID_DATA: invalid data type replace_pick_list_values object (Field: replace_pick_list_values)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "minimum_length": 1,
    "api_name": "replace_pick_list_values",
    "json_path": "$.replace_pick_list_values"
  },
  "message": "invalid data type replace_pick_list_values object",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse4

Error response with code NOT_ALLOWED: PickList option replace not allowed

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "PickList option replace not allowed",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response with code NO_PERMISSION: permission denied

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
