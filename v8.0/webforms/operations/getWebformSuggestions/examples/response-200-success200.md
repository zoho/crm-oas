Successful retrieval of A/B testing variant suggestions for a webform

```json
{
  "webform_suggestions": [
    {
      "type": "abtesting/abtesting_variant",
      "suggestion_details": {
        "reason": {
          "conversion_rate": "low",
          "low_filled_rate_fields": [
            {
              "id": "123",
              "api_name": "Email",
              "field_label": "email edited"
            },
            {
              "id": "123",
              "api_name": "Annual_Revenue",
              "field_label": "Annual Revenue"
            }
          ]
        },
        "suggested_variant_info": {
          "button_attributes": [
            {
              "color": "#fff",
              "name": "Submit"
            },
            {
              "color": "#fff",
              "name": "Reset"
            }
          ],
          "form_attributes": {
            "color": "white",
            "width": 600,
            "font_attributes": {
              "size": 12,
              "color": "black",
              "family": "Arial"
            },
            "align": "left"
          },
          "fields": [
            {
              "help": {
                "text": "Your name",
                "url": null
              },
              "hidden": false,
              "advanced": false,
              "api_name": "Last_Name",
              "field_label": "Last Name",
              "id": "2349263000000002595",
              "required": true,
              "field_name": "Last Name"
            },
            {
              "help": null,
              "hidden": false,
              "advanced": false,
              "api_name": "Company",
              "field_label": "Company",
              "id": "2349263000000002591",
              "required": true,
              "field_name": "Company"
            }
          ]
        }
      }
    }
  ]
}
```
