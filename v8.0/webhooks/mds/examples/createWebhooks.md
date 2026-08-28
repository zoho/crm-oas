# Examples: createWebhooks

**POST /settings/automation/webhooks**

## Request examples

### `application/json` — SamplePostRequest

Webhook creation request with module parameters, custom headers, and body configuration.

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

### Status `201` — `application/json` — Success201

Success response for webhook creation with new webhook ID

```json
{
  "webhooks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "5725767000007186002"
      },
      "message": "webhook created successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response when the name key is missing.

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.webhooks[0].name"
      },
      "message": "mandatory param missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response when invalid ID given for module.

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

Error response for module ID and API name conflict

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

Error response when special characters are used in name.

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

Error response when the name exceeds maximum length.

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

Error response when http_method has invalid data type.

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

Error response for invalid URL.

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

Error response for invalid values in date_format.

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

Error response for invalid value in time_zone.

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

Error response for invalid values in datetime_format.

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

Error response for unsupported fields.

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

Error response for duplicate parameter name in module_parameters.

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

Error response when authentication type is incompatible with connection_name.

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

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Error response for value missing.

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

### Status `400` — `application/json` — MandatoryNotFoundResponse3

Error response when name is missing.

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

### Status `400` — `application/json` — MandatoryNotFoundResponse4

Shows the error response when http_method missing.

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

### Status `400` — `application/json` — InvalidDataResponse10

Error response for invalid connection_name.

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

Error response when request fields are incompatible with the chosen http_method.

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

### Status `400` — `application/json` — InvalidDataResponse11

Error response when the headers have invalid data type in webhooks.

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

### Status `400` — `application/json` — InvalidDataResponse12

Error response when headers exceeds maximum length in webhooks.

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

Error response when module_parameters is missing from the headers object

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

Error response for invalid data type in module_parameters.

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

Error response when module_parameters exceeds the maximum allowed count in headers.

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

### Status `400` — `application/json` — InvalidDataResponse13

Error response when the name key has invalid data type in module_parameters.

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

### Status `400` — `application/json` — InvalidDataResponse14

Error response when name value exceeds maximum length in module_parameters.

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

### Status `400` — `application/json` — InvalidDataResponse15

Error response when the invalid value is provided in module_parameters.

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

### Status `400` — `application/json` — InvalidDataResponse16

Error response when value exceeds maximum length for module_parameters.

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

Error response for invalid data type in custom_parameters.

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

Error response when custom_parameters exceeds the maximum allowed count.

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

### Status `400` — `application/json` — InvalidDataResponse17

Error response when the name has invalid value in custom_parameters.

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

### Status `400` — `application/json` — InvalidDataResponse18

Error response when the value of name exceeds maximum length in custom_parameters.

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

### Status `400` — `application/json` — InvalidDataResponse19

Error response when the value has wrong data type in custom_parameters.

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

### Status `400` — `application/json` — InvalidDataResponse20

Error response when the value exceeds maximum length in custom_parameters.

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

### Status `400` — `application/json` — MandatoryNotFoundResponse5

Error response when module is missing.

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

### Status `400` — `application/json` — InvalidDataResponse21

Error response when the module has invalid data type in webhooks.

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

### Status `400` — `application/json` — InvalidDataResponse22

Error response when the module exceeds maximum length in webhooks.

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

Error response for invalid data type in api_name.

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

Error response when api_name exceeds the maximum allowed length.

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

Error response for invalid data type in module ID.

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

Error response when module ID exceeds the maximum allowed length.

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

### Status `400` — `application/json` — InvalidDataResponse23

Error response when description has wrong data type in webhooks.

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

### Status `400` — `application/json` — InvalidDataResponse24

Error response when description exceeds maximum length in webhooks.

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

### Status `400` — `application/json` — InvalidDataResponse25

Error response when body has invalid data type in webhooks.

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

### Status `400` — `application/json` — InvalidDataResponse26

Error response when the body exceeds maximum length in webhooks.

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

Error response for invalid data type in raw_data_content.

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

Error response when raw_data_content exceeds the maximum allowed length.

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

Error response when format is missing in body.

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

Error response for invalid data type in body format

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

Error response when format value exceeds the maximum allowed length

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

Error response when format value is not among the accepted values.

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

Error response when type is missing in body.

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

Error response for invalid data type in body type.

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

Error response when type value exceeds the maximum allowed length.

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

Error response when type value is not among the accepted values.

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

### Status `400` — `application/json` — MandatoryNotFoundResponse6

Error response when url key is missing.

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

### Status `400` — `application/json` — InvalidDataResponse27

Error response when URL has invalid data type in webhooks.

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

### Status `400` — `application/json` — InvalidDataResponse28

Shows the error response when URL exceeds maximum length.

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

### Status `400` — `application/json` — MandatoryNotFoundResponse7

Error response when the feature_type is missing.

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

### Status `400` — `application/json` — InvalidDataResponse29

Error response when feature_type has invalid data type.

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

### Status `400` — `application/json` — InvalidDataResponse30

Error response when the feature_type exceeds maximum length.

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

### Status `400` — `application/json` — MandatoryNotFoundResponse8

Error response when the http_method is missing.

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

### Status `400` — `application/json` — InvalidDataResponse31

Error response when http_method has invalid data type.

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

### Status `400` — `application/json` — InvalidDataResponse32

Error response when http_method exceeds maximum length.

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

### Status `400` — `application/json` — MandatoryNotFoundResponse9

Error response when the name key is missing.

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

### Status `400` — `application/json` — InvalidDataResponse33

Error response when name has invalid data type.

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

### Status `400` — `application/json` — InvalidDataResponse34

Error response when name exceeds maximum length.

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

### Status `400` — `application/json` — MandatoryNotFoundResponse10

Error response when the authentication is missing.

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

### Status `400` — `application/json` — InvalidDataResponse35

Error response when authentication data type is invalid.

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

### Status `400` — `application/json` — InvalidDataResponse36

Error response when the authentication exceeds maximum length.

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

Error response when type is missing in authentication.

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

Error response for invalid data type in authentication type.

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

Error response when type value exceeds the maximum allowed length in authentication.

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

Error response when type value is not among the accepted values in authentication.

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

### Status `400` — `application/json` — ExpectedFieldMissing

Error response when module is missing both ID and api_name.

```json
{
  "webhooks": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.webhooks[0].module.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.webhooks[0].module.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingRawContent

Error response for missing raw_data_content when body type is raw

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "format",
          "json_path": "$.webhooks[0].body.format"
        },
        "api_name": "raw_data_content",
        "json_path": "$.webhooks[0].body.raw_data_content"
      },
      "message": "raw data content key is mandatory for raw body type",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingFormData

Error response for missing form_data_content when type is form_data

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.webhooks[0].body.type"
        },
        "api_name": "form_data_content",
        "json_path": "$.webhooks[0].body.form_data_content"
      },
      "message": "form data content key is mandatory for form body type",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingRelatedModule

Error response for missing related_module when feature_type is kiosk

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "feature_type",
          "json_path": "$.webhooks[0].feature_type"
        },
        "api_name": "related_module",
        "json_path": "$.webhooks[0].related_module"
      },
      "message": "Webhook action related module missing for kiosk feature",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — EmptyUrl

Error response for an empty URL field.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "url",
        "json_path": "$.webhooks[0].url"
      },
      "message": "Empty value is not allowed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SsrfUrl

Error response when url key value fails SSRF validation.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "url",
        "json_path": "$.webhooks[0].url"
      },
      "message": "Url you've configured is not secure",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidFeatureType

Error response when the feature_type value is not recognized.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "feature_type",
        "json_path": "$.webhooks[0].feature_type"
      },
      "message": "the given feature name is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidBodyType

Error response when body.type value is not accepted.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.webhooks[0].body.type"
      },
      "message": "invalid body type passed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidBodyFormat

Error respons when body.format value is not accepted.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "format",
        "json_path": "$.webhooks[0].body.format"
      },
      "message": "invalid format passed in body",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidFormDataContent

Error response for invalid values in body.form_data_content.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "form_data_content",
        "json_path": "$.webhooks[0].body.form_data_content"
      },
      "message": "inavlid form data content passed in body",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response when user lacks Manage Workflow permission.

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

### Status `403` — `application/json` — FeatureNotSupported

Error response when webhooks is not available in current edition.

```json
{
  "code": "FEATURE_NOT_SUPPORTED",
  "details": {},
  "message": "feature not available in this edition",
  "status": "error"
}
```
