# Examples: createGlobalPicklist

**POST /settings/global_picklists**

## Request examples

### `application/json` — CreateGlobalPicklistExample

Example request to create a global picklist

```json
{
  "global_picklists": [
    {
      "display_label": "Priority Level",
      "api_name": "priority_level__s",
      "description": "Priority levels for tasks and activities",
      "pick_list_values_sorted_lexically": false,
      "pick_list_values": [
        {
          "display_value": "High",
          "type": "used"
        },
        {
          "display_value": "Medium",
          "type": "used"
        },
        {
          "display_value": "Low",
          "type": "unused"
        }
      ]
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — SuccessExample

Successful creation response

```json
{
  "global_picklists": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4793076000000560088"
      },
      "message": "global picklist added successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDisplayLabel

Duplicate display_label error

```json
{
  "global_picklists": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "display_label",
        "json_path": "$.global_picklists[0].display_label"
      },
      "message": "Duplicate name found, enter a unique name.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryPickListValues

Missing pick_list_values

```json
{
  "global_picklists": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "pick_list_values",
        "json_path": "$.global_picklists[0].pick_list_values"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SpecialCharactersDisplayLabel

Special characters in display_label

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "display_label",
        "json_path": "$.global_picklists[0].display_label"
      },
      "message": "Special characters in name",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DisplayLabelMaxLength

display_label exceeds 50 characters

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 50,
        "api_name": "display_label",
        "json_path": "$.global_picklists[0].display_label"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DescriptionMaxLength

description exceeds 1000 characters

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 1000,
        "api_name": "description",
        "json_path": "$.global_picklists[0].description"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DisplayValueMaxLength

display_value exceeds 120 characters

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 120,
        "api_name": "display_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].display_value"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReferenceValueMaxLength

reference_value exceeds 120 characters

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 120,
        "api_name": "reference_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].reference_value"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SpecialCharactersDisplayValue

Special characters in display_value

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "display_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].display_value"
      },
      "message": "Special characters are not allowed in Options",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SpecialCharactersReferenceValue

Special characters in reference_value

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "reference_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].reference_value"
      },
      "message": "Special characters are not allowed in Options",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NoUsedOption

No used option in picklist values

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "pick_list_values",
        "json_path": "$.global_picklists[0].pick_list_values"
      },
      "message": "Values in the pick list field cannot be empty.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDisplayValue

Duplicate display_value in pick_list_values

```json
{
  "global_picklists": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "pick_list_values",
        "json_path": "$.global_picklists[0].pick_list_values"
      },
      "message": "Duplicate option found. Enter a unique option.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateReferenceValue

Duplicate reference_value in pick_list_values

```json
{
  "global_picklists": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "pick_list_values",
        "json_path": "$.global_picklists[0].pick_list_values"
      },
      "message": "Duplicate reference option found. Enter a unique reference option.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidType

Invalid type value

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "regex": "used|unused",
        "api_name": "type",
        "json_path": "$.global_picklists[0].pick_list_values[1].type"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReferenceValueEmpty

reference_value is empty or null

```json
{
  "global_picklists": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "reference_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].reference_value"
      },
      "message": "Reference value in pick list values cannot be empty or null",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DisplayValueEmpty

display_value is empty or null

```json
{
  "global_picklists": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "display_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].display_value"
      },
      "message": "Display value in pick list values cannot be empty or null",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryDisplayLabel

display_label not provided

```json
{
  "global_picklists": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "display_label",
        "json_path": "$.global_picklists[0].display_label"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryDisplayValueInPickList

display_value not provided in first pick_list_values

```json
{
  "global_picklists": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "display_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].display_value"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — EmojiInDisplayLabel

Emoji in display_label

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "display_label",
        "json_path": "$.global_picklists[0].display_label"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NoneInDisplayValue

-None- in display_value

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "display_value",
        "json_path": "$.global_picklists[0].pick_list_values.display_value"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UsedOptionsLimitExceeded

Used options limit exceeded (1000)

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": [
          {
            "api_name": "pick_list_values",
            "json_path": "$.global_picklists[0].pick_list_values"
          }
        ],
        "limit": 1000
      },
      "message": "Sorry, you have reached the limit of 1000 values added for this pick list field.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UnusedOptionsLimitExceeded

Unused options limit exceeded (500)

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": [
          {
            "api_name": "pick_list_values",
            "json_path": "$.global_picklists[0].pick_list_values"
          }
        ],
        "limit": 500
      },
      "message": "Sorry, you have reached the limit of 500 unused values added for this pick list field.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LargeGlobalPicklistsLimitExceeded

Large global picklists limit exceeded

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": [
          {
            "api_name": "global_picklists",
            "json_path": "$.global_picklists[0]"
          }
        ],
        "limit": 10
      },
      "message": "Large global picklists limit exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — GlobalPicklistsLimitExceeded

Global picklists limit exceeded

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": [
          {
            "api_name": "global_picklists",
            "json_path": "$.global_picklists[0]"
          }
        ],
        "limit": 10
      },
      "message": "global picklists limit exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReservedKeyword

System keyword not allowed in global set label

```json
{
  "global_picklists": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "display_label",
        "json_path": "$.global_picklists[0].display_label"
      },
      "message": "System keyword not allowed in global set label",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — ErrorExample

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "details": {
    "permissions": [
      "Crm_Implied_Customize_Zoho_CRM"
    ]
  },
  "status": "error"
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
