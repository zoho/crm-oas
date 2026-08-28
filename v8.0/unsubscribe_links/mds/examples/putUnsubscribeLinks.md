# Examples: putUnsubscribeLinks

**PUT /settings/unsubscribe_links**

## Request examples

### `application/json` — SamplePutRequest

Sample request body for bulk-updating an unsubscribe link

```json
{
  "unsubscribe_links": [
    {
      "name": "Unsubscribe",
      "custom_location_url": "https://www.zoho.com/crm/developer/docs/api/v8/create-unsubscribe-link.html",
      "standard_page_message": "standard message",
      "submission_redirect_url": "https://www.zoho.com/crm/developer/docs/api/v8/create-unsubscribe-link.html",
      "submission_message": "display message",
      "page_type": "standard",
      "submission_action_type": "display_message",
      "id": "123456789012345678"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "unsubscribe_links": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000115722"
      },
      "message": "Unsubscribe Link updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA error: invalid data (unsubscribe_links)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "unsubscribe_links",
    "json_path": "$.unsubscribe_links"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse2

INVALID_DATA error: unsupported page_type value - variant 1

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "page_type",
        "json_path": "$.unsubscribe_links[0].page_type",
        "supported_values": [
          "standard",
          "custom"
        ]
      },
      "message": "the given module is not supported in create or update",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

INVALID_DATA error: unsupported submission_action_type value - variant 1

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "submission_action_type",
        "json_path": "$.unsubscribe_links[0].submission_action_type",
        "supported_values": [
          "display_message",
          "redirect"
        ]
      },
      "message": "the given module is not supported in create or update",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

INVALID_DATA error: unsupported page_type value - variant 2

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "page_type",
        "json_path": "$.unsubscribe_links[0].page_type",
        "supported_values": [
          "standard",
          "custom"
        ]
      },
      "message": "the given module is not supported in create or update",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

INVALID_DATA error: unsupported submission_action_type value - variant 2

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "submission_action_type",
        "json_path": "$.unsubscribe_links[0].submission_action_type",
        "supported_values": [
          "display_message",
          "redirect"
        ]
      },
      "message": "the given module is not supported in create or update",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

DEPENDENT_FIELD_MISSING error: required field not found (submission_action_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "submission_redirect_url",
          "json_path": "$.unsubscribe_links[0].submission_redirect_url"
        },
        "api_name": "submission_action_type",
        "json_path": "$.unsubscribe_links[0].submission_action_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse2

DEPENDENT_FIELD_MISSING error: required field not found (submission_action_type) - variant

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "submission_message",
          "json_path": "$.unsubscribe_links[0].submission_message"
        },
        "api_name": "submission_action_type",
        "json_path": "$.unsubscribe_links[0].submission_action_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

INVALID_DATA error: invalid data (submission_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "api_name": "submission_message",
        "json_path": "$.unsubscribe_links[0].submission_message"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

INVALID_DATA error: Invalid data type (name)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.unsubscribe_links[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

INVALID_DATA error: Invalid data (name)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.unsubscribe_links[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

INVALID_DATA error: Invalid data (name) - empty string

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "name",
        "minimum_length": 1,
        "json_path": "$.unsubscribe_links[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

INVALID_DATA error: Invalid data type (custom_location_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "custom_location_url",
        "expected_data_type": "website",
        "json_path": "$.unsubscribe_links[*].custom_location_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

INVALID_DATA error: Invalid data (custom_location_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "custom_location_url",
        "maximum_length": 250,
        "json_path": "$.unsubscribe_links[*].custom_location_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse12

INVALID_DATA error: Invalid data type (standard_page_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "standard_page_message",
        "expected_data_type": "text",
        "json_path": "$.unsubscribe_links[*].standard_page_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

INVALID_DATA error: Invalid data (standard_page_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "standard_page_message",
        "maximum_length": 2000,
        "json_path": "$.unsubscribe_links[*].standard_page_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse14

INVALID_DATA error: Invalid data type (submission_redirect_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_redirect_url",
        "expected_data_type": "website",
        "json_path": "$.unsubscribe_links[*].submission_redirect_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

INVALID_DATA error: Invalid data (submission_redirect_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_redirect_url",
        "maximum_length": 250,
        "json_path": "$.unsubscribe_links[*].submission_redirect_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse16

INVALID_DATA error: Invalid data type (submission_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_message",
        "expected_data_type": "text",
        "json_path": "$.unsubscribe_links[*].submission_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse17

INVALID_DATA error: Invalid data (submission_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_message",
        "maximum_length": 2000,
        "json_path": "$.unsubscribe_links[*].submission_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse18

INVALID_DATA error: Invalid data type (page_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "page_type",
        "expected_data_type": "text",
        "json_path": "$.unsubscribe_links[*].page_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse20

INVALID_DATA error: unsupported page_type value

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "page_type",
        "supported_values": [
          "standard",
          "custom"
        ],
        "json_path": "$.unsubscribe_links[*].page_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse3

DEPENDENT_FIELD_MISSING error: Dependent field is missing (custom_location_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "page_type",
          "json_path": "$.unsubscribe_links[*].page_type"
        },
        "api_name": "custom_location_url",
        "json_path": "$.unsubscribe_links[*].unsubscribe_links.custom_location_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse4

DEPENDENT_FIELD_MISSING error: Dependent field is missing (standard_page_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "page_type",
          "json_path": "$.unsubscribe_links[*].page_type"
        },
        "api_name": "standard_page_message",
        "json_path": "$.unsubscribe_links[*].unsubscribe_links.standard_page_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse21

INVALID_DATA error: Invalid data type (submission_action_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_action_type",
        "expected_data_type": "text",
        "json_path": "$.unsubscribe_links[*].submission_action_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse22

INVALID_DATA error: Invalid data (submission_action_type)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_action_type",
        "maximum_length": 15,
        "json_path": "$.unsubscribe_links[*].submission_action_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse23

INVALID_DATA error: unsupported submission_action_type value

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_action_type",
        "supported_values": [
          "display_message",
          "redirect"
        ],
        "json_path": "$.unsubscribe_links[*].submission_action_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse5

DEPENDENT_FIELD_MISSING error: Dependent field is missing (submission_redirect_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "submission_action_type",
          "json_path": "$.unsubscribe_links[*].submission_action_type"
        },
        "api_name": "submission_redirect_url",
        "json_path": "$.unsubscribe_links[*].unsubscribe_links.submission_redirect_url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse6

DEPENDENT_FIELD_MISSING error: Dependent field is missing (submission_message)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "submission_action_type",
          "json_path": "$.unsubscribe_links[*].submission_action_type"
        },
        "api_name": "submission_message",
        "json_path": "$.unsubscribe_links[*].unsubscribe_links.submission_message"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

MANDATORY_NOT_FOUND error: Required field is missing (ID)

```json
{
  "unsubscribe_links": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "details": {
        "api_name": "id",
        "json_path": "$.unsubscribe_links[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse24

INVALID_DATA error: Invalid data type (ID field)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.unsubscribe_links[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse25

INVALID_DATA error: Invalid data (ID field)

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.unsubscribe_links[*].id"
      },
      "status": "error"
    }
  ]
}
```
