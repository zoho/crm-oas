### `application/json` — UpdateWizardExample

Minimal valid PATCH request example to update a wizard configuration.

```json
{
  "wizards": [
    {
      "module": {
        "api_name": "Leads",
        "id": "738294857293847561"
      },
      "name": "Updated_Lead_Wizard",
      "active": true,
      "profiles": [
        {
          "name": "Administrator",
          "id": "738294857293847562"
        }
      ],
      "containers": [
        {
          "layout": {
            "id": "738294857293847570"
          },
          "chart_data": {
            "nodes": [
              {
                "pos_x": 100,
                "pos_y": 40,
                "start_node": true,
                "screen": {
                  "reference_id": "{{screenref1}}",
                  "display_label": "Lead Information"
                }
              },
              {
                "pos_x": 300,
                "pos_y": 90,
                "start_node": false,
                "screen": {
                  "reference_id": "{{screenref2}}",
                  "display_label": "Additional Details"
                }
              }
            ],
            "connections": [
              {
                "source_button": {
                  "reference_id": "{{btnnext1}}",
                  "display_label": "Next"
                },
                "target_screen": {
                  "reference_id": "{{screenref2}}",
                  "display_label": "Additional Details"
                }
              }
            ],
            "color_palette": {
              "button_background": [
                "#123456",
                "#F5F5F5"
              ]
            }
          },
          "screens": [
            {
              "reference_id": "{{screenref1}}",
              "display_label": "Lead Information",
              "segments": [
                {
                  "sequence_number": 1,
                  "display_label": "Lead Basic Info",
                  "type": "composite",
                  "reference_id": "{{segref1}}",
                  "elements": [
                    {
                      "sequence_number": 1,
                      "type": "field",
                      "resource": {
                        "name": "Last_Name",
                        "id": "738294857293847580"
                      }
                    }
                  ]
                },
                {
                  "sequence_number": 2,
                  "display_label": "Actions",
                  "type": "buttons",
                  "reference_id": "{{segref2}}",
                  "buttons": [
                    {
                      "reference_id": "{{btnnext1}}",
                      "display_label": "Next",
                      "sequence_number": 1,
                      "shape": "capsule",
                      "background_color": "#009688",
                      "color": "#FFFFFF",
                      "type": "transition",
                      "category": "wizard_button",
                      "visibility": "show",
                      "target_screen": {
                        "reference_id": "{{screenref2}}",
                        "display_label": "Additional Details"
                      },
                      "profiles": [
                        {
                          "name": "Administrator",
                          "id": "738294857293847562"
                        }
                      ]
                    }
                  ]
                }
              ]
            },
            {
              "id": "738294857293847561",
              "display_label": "Additional Details"
            }
          ]
        }
      ]
    }
  ]
}
```
