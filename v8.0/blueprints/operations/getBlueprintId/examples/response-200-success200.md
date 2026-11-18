Successful retrieval of a single Blueprint

```json
{
  "blueprints": [
    {
      "owner": null,
      "created_time": "2025-09-24T12:31:05+05:30",
      "chart_data": {
        "nodes": [
          {
            "position_x": -370,
            "position_y": 730,
            "state": {
              "id": "111111000000113091"
            }
          },
          {
            "position_x": 50,
            "position_y": 790,
            "state": {
              "id": "111111000000113081"
            }
          },
          {
            "position_x": 510,
            "position_y": 780,
            "state": {
              "id": "111111000000122003"
            }
          },
          {
            "position_x": 620,
            "position_y": 430,
            "state": {
              "id": "111111000000113075"
            }
          },
          {
            "position_x": 400,
            "position_y": 520,
            "state": {
              "id": "111111000000113077"
            }
          },
          {
            "position_x": 100,
            "position_y": 560,
            "state": {
              "id": "111111000000113071"
            }
          },
          {
            "position_x": -110,
            "position_y": 570,
            "state": {
              "id": "111111000000113073"
            }
          },
          {
            "position_x": -390,
            "position_y": 500,
            "state": {
              "id": "111111000000113089"
            }
          },
          {
            "position_x": 460,
            "position_y": 250,
            "state": {
              "id": "111111000000113093"
            }
          },
          {
            "position_x": -260,
            "position_y": 260,
            "state": {
              "id": "111111000000113083"
            }
          },
          {
            "position_x": 50,
            "position_y": 280,
            "state": {
              "id": "111111000000113087"
            }
          },
          {
            "position_x": 50,
            "position_y": 110,
            "state": {
              "id": "111111000000113079"
            }
          }
        ],
        "canvas_size": {
          "width": 502,
          "height": 907
        },
        "connections": [
          {
            "from": {
              "end_point": {
                "position_x": 0.5,
                "position_y": 1,
                "direction_x": 0,
                "direction_y": 1
              },
              "state": {
                "id": "111111000000085028"
              }
            },
            "id": "111111000000113049",
            "to": {
              "end_point": {
                "position_x": 0.5,
                "position_y": 0,
                "direction_x": 0,
                "direction_y": -1
              },
              "state": {
                "id": "111111000000085001"
              }
            },
            "transition": {
              "api_name": "T1",
              "name": "T1",
              "id": "111111000000113001"
            }
          },
          {
            "from": {
              "end_point": {
                "position_x": 0,
                "position_y": 0.5,
                "direction_x": 0,
                "direction_y": 0
              },
              "state": {
                "id": "111111000000085028"
              }
            },
            "id": "111111000000113051",
            "to": {
              "end_point": {
                "position_x": 0.5,
                "position_y": 0,
                "direction_x": 0,
                "direction_y": -1
              },
              "state": {
                "id": "111111000000085003"
              }
            },
            "transition": {
              "api_name": "T2",
              "name": "T2",
              "id": "111111000000113003"
            }
          },
          {
            "from": {
              "end_point": {
                "position_x": 0,
                "position_y": 0.5,
                "direction_x": 0,
                "direction_y": 0
              },
              "state": {
                "id": "111111000000085003"
              }
            },
            "id": "111111000000113053",
            "to": {
              "end_point": {
                "position_x": 0.3,
                "position_y": 0,
                "direction_x": 0,
                "direction_y": -1
              },
              "state": {
                "id": "111111000000085007"
              }
            },
            "transition": {
              "api_name": "T4",
              "name": "T4",
              "id": "111111000000113007"
            }
          },
          {
            "from": {
              "end_point": {
                "position_x": 1,
                "position_y": 0.5,
                "direction_x": 0,
                "direction_y": 0
              },
              "state": {
                "id": "111111000000085003"
              }
            },
            "id": "111111000000113055",
            "to": {
              "end_point": {
                "position_x": 0.3,
                "position_y": 0,
                "direction_x": 0,
                "direction_y": -1
              },
              "state": {
                "id": "111111000000085009"
              }
            },
            "transition": {
              "api_name": "T5",
              "name": "T5",
              "id": "111111000000113009"
            }
          },
          {
            "from": {
              "end_point": {
                "position_x": 0.6,
                "position_y": 1,
                "direction_x": 0,
                "direction_y": 1
              },
              "state": {
                "id": "111111000000085001"
              }
            },
            "id": "111111000000113057",
            "to": {
              "end_point": {
                "position_x": 0.5,
                "position_y": 0,
                "direction_x": 0,
                "direction_y": -1
              },
              "state": {
                "id": "111111000000085011"
              }
            },
            "transition": {
              "api_name": "T6",
              "name": "T6",
              "id": "111111000000113011"
            }
          },
          {
            "from": {
              "end_point": {
                "position_x": 1,
                "position_y": 0.5,
                "direction_x": 0,
                "direction_y": 0
              },
              "state": {
                "id": "111111000000085028"
              }
            },
            "id": "111111000000113059",
            "to": {
              "end_point": {
                "position_x": 0.4,
                "position_y": 0,
                "direction_x": 0,
                "direction_y": -1
              },
              "state": {
                "id": "111111000000085005"
              }
            },
            "transition": {
              "api_name": "T3",
              "name": "T3",
              "id": "111111000000113005"
            }
          },
          {
            "from": {
              "end_point": {
                "position_x": 0,
                "position_y": 0.5,
                "direction_x": 0,
                "direction_y": 0
              },
              "state": {
                "id": "111111000000085005"
              }
            },
            "id": "111111000000113061",
            "to": {
              "end_point": {
                "position_x": 0.5,
                "position_y": 0,
                "direction_x": 0,
                "direction_y": -1
              },
              "state": {
                "id": "111111000000085013"
              }
            },
            "transition": {
              "api_name": "T7",
              "name": "Updated Transition",
              "id": "111111000000113013"
            }
          },
          {
            "from": {
              "end_point": {
                "position_x": 1,
                "position_y": 0.5,
                "direction_x": 0,
                "direction_y": 0
              },
              "state": {
                "id": "111111000000085005"
              }
            },
            "id": "111111000000113063",
            "to": {
              "end_point": {
                "position_x": 0.3,
                "position_y": 0,
                "direction_x": 0,
                "direction_y": -1
              },
              "state": {
                "id": "111111000000085015"
              }
            },
            "transition": {
              "api_name": "T8",
              "name": "T8",
              "id": "111111000000113015"
            }
          },
          {
            "from": {
              "end_point": {
                "position_x": 0,
                "position_y": 0.5,
                "direction_x": 0,
                "direction_y": 0
              },
              "state": {
                "id": "111111000000085009"
              }
            },
            "id": "111111000000113065",
            "to": {
              "end_point": {
                "position_x": 0.5,
                "position_y": 0,
                "direction_x": 0,
                "direction_y": -1
              },
              "state": {
                "id": "111111000000085021"
              }
            },
            "transition": {
              "api_name": "T11",
              "name": "T11",
              "id": "111111000000113017"
            }
          },
          {
            "from": {
              "end_point": {
                "position_x": 0.6,
                "position_y": 1,
                "direction_x": 0,
                "direction_y": 1
              },
              "state": {
                "id": "111111000000085009"
              }
            },
            "id": "111111000000113067",
            "to": {
              "end_point": {
                "position_x": 0,
                "position_y": 0.5,
                "direction_x": 0,
                "direction_y": 0
              },
              "state": {
                "id": "111111000000085019"
              }
            },
            "transition": {
              "api_name": "T10",
              "name": "T10",
              "id": "111111000000113019"
            }
          },
          {
            "from": {
              "end_point": {
                "position_x": 0.5,
                "position_y": 1,
                "direction_x": 0,
                "direction_y": 1
              },
              "state": {
                "id": "111111000000085013"
              }
            },
            "id": "111111000000113069",
            "to": {
              "end_point": {
                "position_x": 0.5,
                "position_y": 0,
                "direction_x": 0,
                "direction_y": -1
              },
              "state": {
                "id": "111111000000085017"
              }
            },
            "transition": {
              "api_name": "T9",
              "name": "T9",
              "id": "111111000000113021"
            }
          }
        ]
      },
      "module": {
        "api_name": "Leads",
        "_precedence": 5,
        "id": "111111000000002624"
      },
      "description": "",
      "created_by": {
        "name": "Kandasamy",
        "id": "111111000000057846"
      },
      "layout": {
        "api_name": "Standard__s",
        "name": "Standard",
        "id": "111111000000003620"
      },
      "modified_time": "2025-09-26T01:57:24+05:30",
      "field": {
        "api_name": "CFPicklist",
        "field_label": "CFPicklist",
        "id": "111111000000085002"
      },
      "api_name": "Lead_Test_Bp_1",
      "continuous": false,
      "criteria": {
        "comparator": "greater_than",
        "field": {
          "api_name": "Annual_Revenue",
          "id": "111111000000005056"
        },
        "type": "value",
        "value": "100"
      },
      "pipeline": {
        "name": "Stage",
        "id": "111111000000128001"
      },
      "name": "Lead Test Bp 1",
      "modified_by": {
        "name": "Kandasamy",
        "id": "111111000000057846"
      },
      "id": "111111000000113045",
      "connections": [
        {
          "from_state": {
            "name": "-None-",
            "id": "111111000000113079"
          },
          "id": "111111000000113049",
          "transitions": {
            "api_name": "T1",
            "name": "T1",
            "id": "111111000000113001",
            "precedence": 1,
            "common": true
          },
          "to_state": {
            "name": "Option 1",
            "id": "111111000000113087"
          }
        },
        {
          "from_state": {
            "name": "-None-",
            "id": "111111000000113079"
          },
          "id": "111111000000113051",
          "transitions": {
            "api_name": "T2",
            "name": "T2",
            "id": "111111000000113003",
            "precedence": 2
          },
          "to_state": {
            "name": "Option 2",
            "id": "111111000000113083"
          }
        },
        {
          "from_state": {
            "name": "Option 2",
            "id": "111111000000113083"
          },
          "id": "111111000000113053",
          "transitions": {
            "api_name": "T4",
            "name": "T4",
            "id": "111111000000113007",
            "precedence": 1
          },
          "to_state": {
            "name": "Option 4",
            "id": "111111000000113089"
          }
        },
        {
          "from_state": {
            "name": "Option 2",
            "id": "111111000000113083"
          },
          "id": "111111000000113055",
          "transitions": {
            "api_name": "T5",
            "name": "T5",
            "id": "111111000000113009",
            "precedence": 2
          },
          "to_state": {
            "name": "Option 5",
            "id": "111111000000113073"
          }
        },
        {
          "from_state": {
            "name": "Option 1",
            "id": "111111000000113087"
          },
          "id": "111111000000113057",
          "transitions": {
            "api_name": "T6",
            "name": "T6",
            "id": "111111000000113011",
            "precedence": 1
          },
          "to_state": {
            "name": "Option 6",
            "id": "111111000000113071"
          }
        },
        {
          "from_state": {
            "name": "-None-",
            "id": "111111000000113079"
          },
          "id": "111111000000113059",
          "transitions": {
            "api_name": "T3",
            "name": "T3",
            "id": "111111000000113005",
            "precedence": 3
          },
          "to_state": {
            "name": "Option 3",
            "id": "111111000000113093"
          }
        },
        {
          "from_state": {
            "name": "Option 3",
            "id": "111111000000113093"
          },
          "id": "111111000000113061",
          "transitions": {
            "api_name": "T7",
            "name": "Updated Transition",
            "id": "111111000000113013",
            "precedence": 1
          },
          "to_state": {
            "name": "Option 7",
            "id": "111111000000113077"
          }
        },
        {
          "from_state": {
            "name": "Option 3",
            "id": "111111000000113093"
          },
          "id": "111111000000113063",
          "transitions": {
            "api_name": "T8",
            "name": "T8",
            "id": "111111000000113015",
            "precedence": 2
          },
          "to_state": {
            "name": "Option 8",
            "id": "111111000000113075"
          }
        },
        {
          "from_state": {
            "name": "Option 5",
            "id": "111111000000113073"
          },
          "id": "111111000000113065",
          "transitions": {
            "api_name": "T11",
            "name": "T11",
            "id": "111111000000113017",
            "precedence": 1
          },
          "to_state": {
            "name": "Option 11",
            "id": "111111000000113091"
          }
        },
        {
          "from_state": {
            "name": "Option 5",
            "id": "111111000000113073"
          },
          "id": "111111000000113067",
          "transitions": {
            "api_name": "T10",
            "name": "T10",
            "id": "111111000000113019",
            "precedence": 2
          },
          "to_state": {
            "name": "Option 10",
            "id": "111111000000113081"
          }
        },
        {
          "from_state": {
            "name": "Option 7",
            "id": "111111000000113077"
          },
          "id": "111111000000113069",
          "transitions": {
            "api_name": "T9",
            "name": "T9",
            "id": "111111000000113021",
            "precedence": 1
          },
          "to_state": {
            "name": "Option 9",
            "id": "111111000000122003"
          }
        }
      ]
    }
  ]
}
```
