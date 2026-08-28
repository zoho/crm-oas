# Examples: updateWebhookById

**PUT /settings/automation/webhooks/{webhookId}**

## Request examples

### `application/json` — SamplePutRequest

Update a webhook with full configuration

```json
{
  "webhooks": [
    {
      "headers": {
        "module_parameters": [
          {
            "name": "lead_email",
            "value": "${!Leads.Email}"
          },
          {
            "name": "lead_id",
            "value": "${!Leads.Id}"
          },
          {
            "name": "lead_owner",
            "value": "${!Leads.Owner}"
          }
        ],
        "custom_parameters": [
          {
            "name": "source",
            "value": "website"
          },
          {
            "name": "version",
            "value": "1.0"
          }
        ]
      },
      "module": {
        "api_name": "Leads",
        "id": "5725767000000002175"
      },
      "description": "Protected Data",
      "body": {
        "raw_data_content": "{\n  \"lead_id\": \"${!Leads.Id}\",\n  \"email\": \"${!Leads.Email}\",\n  \"owner\": \"${!Leads.Owner}\",\n  \"source\": \"website\",\n  \"version\": \"1.0\"\n}",
        "format": "JSON",
        "type": "raw"
      },
      "url": "https://webhook.site/3588de27-e3bd-4237-894b-f140143f3d99",
      "feature_type": "workflow",
      "http_method": "POST",
      "name": "Zoho's Data",
      "authentication": {
        "type": "general"
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful webhook update response

```json
{
  "webhooks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "5725767000007098001"
      },
      "message": "webhook updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Module ID in request body is invalid

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.webhooks[0].module.id"
      },
      "message": "the module id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingResponse1

Module id and api_name refer to different modules

```json
{
  "webhooks": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.webhooks[0].module.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.webhooks[0].module.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Webhook name contains invalid characters

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name"
      },
      "message": "Special characters not allowed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Webhook name exceeds maximum allowed length

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 250,
        "api_name": "name",
        "json_path": "$.webhooks[0].name"
      },
      "message": "The lenght of name has exceeded the limit",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

HTTP method is not supported

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "http_method",
        "json_path": "$.webhooks[0].http_method"
      },
      "message": "The method type given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Webhook URL is not valid

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "url",
        "json_path": "$.webhooks[0].url"
      },
      "message": "please enter a valid URL",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Date format is invalid

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "date_format",
        "json_path": "$.webhooks[0].date_time_format.date_format"
      },
      "message": "The Date given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

Timezone identifier is not supported

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "time_zone",
        "json_path": "$.webhooks[0].date_time_format.time_zone"
      },
      "message": "The timezone given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

DateTime format is invalid

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "datetime_format",
        "json_path": "$.webhooks[0].date_time_format.datetime_format"
      },
      "message": "The date time format given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

Webhook ID in request body is invalid

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.webhooks[0].id"
      },
      "message": "The ID given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

Merge-field token references an unsupported field

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "value",
        "json_path": "$.webhooks[0].headers.module_parameters[0].value"
      },
      "message": "Unsupported fields are present",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse1

Duplicate parameter name in module or custom parameters.

```json
{
  "webhooks": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.webhooks[0].headers.module_parameters[1].name"
      },
      "message": "duplicate parameter name found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse1

Authentication type mismatch with connection name.

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "connection_name",
          "json_path": "$.webhooks[0].authentication.connetion_name"
        },
        "api_name": "type",
        "json_path": "$.webhooks[0].authentication.type"
      },
      "message": "provide appropriate authentication type",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Parameter entry missing name or value

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "value",
        "json_path": "$.webhooks[0].headers.custom_parameters[0].value"
      },
      "message": "the given parameter is invalid, specify both name and value",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Parameter entry missing name or value in webhook request.

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.webhooks[0].headers.module_parameters[0].name"
      },
      "message": "the given parameter is invalid, specify both name and value",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse3

HTTP method field is missing from request body

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "http_method",
        "json_path": "$.webhooks[0].http_method"
      },
      "message": "The method type is not given ",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

Connection name is invalid or does not exist

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "connection_name",
        "json_path": "$.webhooks[0].authentication.connetion_name"
      },
      "message": "Please provide valid connection name",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse2

HTTP method and request body fields are incompatible

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "headers",
          "json_path": "$.webhooks[0].headers"
        },
        "api_name": "http_method",
        "json_path": "$.webhooks[0].http_method"
      },
      "message": "Invalid value provided for the given http method",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse1

Editing a read-only webhook is not allowed

```json
{
  "webhooks": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.webhooks[0].id"
      },
      "message": "Insufficient privileges to edit Read only webhook",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse2

Webhook associated with a Marketplace extension cannot be modified

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "Webhook  is associated with MarketPlace",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse12

Field value has an incorrect data type

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "headers",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].headers"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

Field value is invalid

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "headers",
        "maximum_length": 2,
        "json_path": "$.webhooks[*].headers"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response1

Required field missing from request body

```json
{
  "webhooks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "module_parameters",
      "json_path": "$.webhooks[*].headers.module_parameters"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response2

Webhook field value has an incorrect data type

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "module_parameters",
      "expected_data_type": "jsonarray",
      "json_path": "$.webhooks[*].headers.module_parameters"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response3

Field value is invalid in webhook update request

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "module_parameters",
      "maximum_length": 3,
      "json_path": "$.webhooks[*].headers.module_parameters"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidDataResponse14

Field value has an incorrect data type

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].headers.module_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

Field value is not valid for webhook configuration

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 10,
        "json_path": "$.webhooks[*].headers.module_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse16

Field value has an incorrect data type in webhook configuration

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].headers.module_parameters[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse17

Field value fails validation in webhook configuration

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 15,
        "json_path": "$.webhooks[*].headers.module_parameters[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response4

Field value has an incorrect data type

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "custom_parameters",
      "expected_data_type": "jsonarray",
      "json_path": "$.webhooks[*].headers.custom_parameters"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response5

Field value is not valid

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "custom_parameters",
      "maximum_length": 2,
      "json_path": "$.webhooks[*].headers.custom_parameters"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidDataResponse18

Field value is not valid for its schema type

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].headers.custom_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse19

Field value fails schema validation

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 6,
        "json_path": "$.webhooks[*].headers.custom_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse20

Field value has an incorrect data type in webhook schema

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].headers.custom_parameters[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse21

Field value is not valid for the specified field type

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 7,
        "json_path": "$.webhooks[*].headers.custom_parameters[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse4

Required webhook configuration field is missing

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "module",
        "json_path": "$.webhooks[*].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse22

Field value has an incorrect data type

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse23

Field value fails validation

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "module",
        "maximum_length": 2,
        "json_path": "$.webhooks[*].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response6

Field value fails validation

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "api_name",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].module.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response7

Field value is not valid in webhook update

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "api_name",
      "maximum_length": 5,
      "json_path": "$.webhooks[*].module.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response8

Webhook field value has an incorrect data type

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "id",
      "expected_data_type": "bigint",
      "json_path": "$.webhooks[*].module.id"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response9

Webhook field value fails validation

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "id",
      "maximum_length": 19,
      "json_path": "$.webhooks[*].module.id"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidDataResponse24

Field value has an incorrect data type for webhook configuration

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].description"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse25

Field value is not valid for the specified field type

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 250,
        "json_path": "$.webhooks[*].description"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse26

Field value has an incorrect data type for a webhook property

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "body",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].body"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse27

Field value fails validation for a webhook property

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "body",
        "maximum_length": 3,
        "json_path": "$.webhooks[*].body"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response10

Field value has an incorrect data type

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "raw_data_content",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].body.raw_data_content"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response11

Field value is invalid

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "raw_data_content",
      "maximum_length": 500,
      "json_path": "$.webhooks[*].body.raw_data_content"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response12

Required field missing from webhook request

```json
{
  "webhooks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "format",
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response13

Field value has an incorrect data type in webhook request

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "format",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response14

Field value fails validation in webhook request

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "format",
      "maximum_length": 4,
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response15

Field value is not valid

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "format",
      "supported_values": [
        "JSON",
        "XML",
        "Text",
        "HTML"
      ],
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response16

Required field missing from webhook request

```json
{
  "webhooks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "type",
      "json_path": "$.webhooks[*].body.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response17

Field value has an incorrect data type

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "type",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].body.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response18

Field value fails validation

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "maximum_length": 10,
      "json_path": "$.webhooks[*].body.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response19

Field value is not valid for its schema type

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "supported_values": [
        "form_data",
        "raw"
      ],
      "json_path": "$.webhooks[*].body.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse5

Required field is absent from request body

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "url",
        "json_path": "$.webhooks[*].url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse28

Field value has an incorrect data type in webhook configuration

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "url",
        "expected_data_type": "website",
        "json_path": "$.webhooks[*].url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse29

Field value is not valid for a webhook configuration property

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "url",
        "maximum_length": 57,
        "json_path": "$.webhooks[*].url"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse6

Required field missing from webhook update request.

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "feature_type",
        "json_path": "$.webhooks[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse30

Field value has an incorrect data type in request body

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "feature_type",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse31

Field value is not valid in webhook update request

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "feature_type",
        "maximum_length": 20,
        "json_path": "$.webhooks[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse7

Required field absent from webhook update

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "http_method",
        "json_path": "$.webhooks[*].http_method"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse32

Field value has an incorrect data type for webhook update

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "http_method",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].http_method"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse33

Field value is not valid in request body

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "http_method",
        "maximum_length": 4,
        "json_path": "$.webhooks[*].http_method"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse8

Required webhook configuration field is missing

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.webhooks[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse34

Field value has an incorrect data type in a webhook property

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse35

Field value fails validation for the specified webhook property

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 11,
        "json_path": "$.webhooks[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse9

Required field absent from webhook request

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "authentication",
        "json_path": "$.webhooks[*].authentication"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse36

Field value has an incorrect data type for the specified webhook property

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "authentication",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].authentication"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse37

Field value is not valid for the specified webhook property

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "authentication",
        "maximum_length": 1,
        "json_path": "$.webhooks[*].authentication"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response20

Required webhook field is missing

```json
{
  "webhooks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "type",
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response21

Field value has an incorrect data type

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "type",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response22

Field value is invalid

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "maximum_length": 7,
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response23

Field value is not valid

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "supported_values": [
        "general"
      ],
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidWebhookIdPathResponse1

Webhook ID in URL path is invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

User lacks Manage Workflow permission to update webhooks

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
