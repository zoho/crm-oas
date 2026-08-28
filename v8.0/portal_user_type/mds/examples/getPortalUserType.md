# Examples: getPortalUserType

**GET /settings/portals/{portal}/user_type/{userTypeId}**

## Response examples

### Status `200` — `application/json` — Success200

Portal user type retrieved successfully

```json
{
  "user_type": [
    {
      "default": true,
      "active_user_count": 1,
      "personality_module": {
        "plural_label": "Contacts",
        "api_name": "Contacts",
        "id": "111113000000002666"
      },
      "name": "Client Portal",
      "active": true,
      "invitation_field": {
        "api_name": "Email",
        "id": "111113000000004612"
      },
      "id": "111113000000158041",
      "deactive_user_count": 0,
      "modules": [
        {
          "plural_label": "Contacts",
          "shared_type": "private",
          "api_name": "Contacts",
          "permissions": {
            "view": true,
            "edit": true,
            "edit_shared_records": false,
            "create": true,
            "delete": true
          },
          "id": "111113000000002666",
          "filters": null,
          "fields": [
            {
              "read_only": false,
              "api_name": "Last_Name",
              "id": "111113000000004604"
            },
            {
              "read_only": false,
              "api_name": "Full_Name",
              "id": "111113000000004606"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000004660"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000004662"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000004668"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000004696"
            },
            {
              "read_only": false,
              "api_name": "Contact_X_CM01",
              "id": "111113000000131043"
            },
            {
              "read_only": false,
              "api_name": "Lookup_1",
              "id": "111113000000150048"
            },
            {
              "read_only": false,
              "api_name": "Last_Enriched_Time__s",
              "id": "111113000000006734"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003678",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003678",
                "type": "layout"
              }
            }
          ],
          "views": {
            "display_label": "Contacts - Custom List View",
            "name": "Contacts - Custom List View",
            "id": "111113000000070019",
            "type": "canvas_view"
          }
        },
        {
          "plural_label": "Deals",
          "shared_type": "private",
          "api_name": "Deals",
          "permissions": {
            "view": true,
            "edit": true,
            "edit_shared_records": true,
            "create": true,
            "delete": false
          },
          "id": "111113000000002670",
          "filters": [
            {
              "display_label": "Contact Name",
              "api_name": "Contact_Name",
              "id": "111113000000004774"
            }
          ],
          "fields": [
            {
              "read_only": false,
              "api_name": "Deal_Name",
              "id": "111113000000004750"
            },
            {
              "read_only": false,
              "api_name": "Closing_Date",
              "id": "111113000000004752"
            },
            {
              "read_only": false,
              "api_name": "Contact_Name",
              "id": "111113000000004774"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000004786"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000004788"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000004800"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000004826"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000004830"
            },
            {
              "read_only": false,
              "api_name": "Stage",
              "id": "111113000000004760"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003680",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003680",
                "type": "layout"
              }
            }
          ],
          "views": {
            "display_label": "Deals - Custom List View",
            "name": "Deals - Custom List View",
            "id": "111113000000070199",
            "type": "canvas_view"
          }
        },
        {
          "plural_label": "Products",
          "shared_type": "public",
          "api_name": "Products",
          "permissions": {
            "view": true
          },
          "id": "111113000000002768",
          "filters": null,
          "fields": [
            {
              "read_only": false,
              "api_name": "Product_Name",
              "id": "111113000000005278"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005308"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000005310"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005312"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000005332"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000005326"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003684",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003684",
                "type": "layout"
              }
            }
          ],
          "views": {
            "display_label": "Default List View",
            "name": "All_Products",
            "id": "111113000000053489",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Quotes",
          "shared_type": "private",
          "api_name": "Quotes",
          "permissions": {
            "view": true,
            "edit": false,
            "edit_shared_records": false,
            "create": false,
            "delete": false
          },
          "id": "111113000000002774",
          "filters": [
            {
              "display_label": "Contact Name",
              "api_name": "Contact_Name",
              "id": "111113000000005496"
            }
          ],
          "fields": [
            {
              "read_only": false,
              "api_name": "Subject",
              "id": "111113000000005488"
            },
            {
              "read_only": false,
              "api_name": "Deal_Name",
              "id": "111113000000005490"
            },
            {
              "read_only": false,
              "api_name": "Contact_Name",
              "id": "111113000000005496"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005514"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000005516"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005518"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000005536"
            },
            {
              "read_only": false,
              "api_name": "Quoted_Items",
              "permissions": [
                {
                  "iscustomizable": false,
                  "view": true
                },
                {
                  "iscustomizable": true,
                  "edit": true
                },
                {
                  "iscustomizable": false,
                  "create": true
                },
                {
                  "iscustomizable": true,
                  "delete": true
                }
              ],
              "id": "111113000000005566"
            },
            {
              "read_only": false,
              "api_name": "Grand_Total",
              "id": "111113000000005576"
            },
            {
              "read_only": true,
              "api_name": "Quote_Number",
              "id": "111113000000005486"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000005532"
            },
            {
              "read_only": false,
              "api_name": "Product_Details",
              "id": "111113000000005560"
            },
            {
              "read_only": false,
              "api_name": "Sub_Total",
              "id": "111113000000005568"
            },
            {
              "read_only": false,
              "api_name": "Discount_Type__s",
              "id": "111113000000005578"
            },
            {
              "read_only": false,
              "api_name": "Discount_Percentage__s",
              "id": "111113000000005580"
            },
            {
              "read_only": false,
              "api_name": "Discount",
              "id": "111113000000005570"
            },
            {
              "read_only": false,
              "api_name": "Tax",
              "id": "111113000000005572"
            },
            {
              "read_only": false,
              "api_name": "Adjustment",
              "id": "111113000000005574"
            },
            {
              "read_only": false,
              "api_name": "Sequence_Number",
              "id": "111113000000005582"
            },
            {
              "read_only": false,
              "api_name": "Name",
              "id": "111113000000005584"
            },
            {
              "read_only": false,
              "api_name": "Owner",
              "id": "111113000000005586"
            },
            {
              "read_only": false,
              "api_name": "Created_By",
              "id": "111113000000005588"
            },
            {
              "read_only": false,
              "api_name": "Modified_By",
              "id": "111113000000005590"
            },
            {
              "read_only": false,
              "api_name": "Created_Time",
              "id": "111113000000005592"
            },
            {
              "read_only": false,
              "api_name": "Modified_Time",
              "id": "111113000000005594"
            },
            {
              "read_only": false,
              "api_name": "Last_Activity_Time",
              "id": "111113000000005596"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005600"
            },
            {
              "read_only": false,
              "api_name": "Parent_Id",
              "id": "111113000000005602"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005604"
            },
            {
              "read_only": false,
              "api_name": "Exchange_Rate",
              "id": "111113000000005606"
            },
            {
              "read_only": false,
              "api_name": "Product_Name",
              "id": "111113000000005608"
            },
            {
              "read_only": false,
              "api_name": "Description",
              "id": "111113000000005610"
            },
            {
              "read_only": false,
              "api_name": "Quantity",
              "id": "111113000000005612"
            },
            {
              "read_only": false,
              "api_name": "Total_After_Discount",
              "id": "111113000000005622"
            },
            {
              "read_only": false,
              "api_name": "Line_Tax",
              "id": "111113000000005628"
            },
            {
              "read_only": false,
              "api_name": "Discount_Type__s",
              "id": "111113000000005632"
            },
            {
              "read_only": false,
              "api_name": "Total",
              "id": "111113000000005618"
            },
            {
              "read_only": false,
              "api_name": "List_Price",
              "id": "111113000000005616"
            },
            {
              "read_only": false,
              "api_name": "Discount",
              "id": "111113000000005620"
            },
            {
              "read_only": false,
              "api_name": "Net_Total",
              "id": "111113000000005626"
            },
            {
              "read_only": false,
              "api_name": "Discount_Percentage__s",
              "id": "111113000000005634"
            },
            {
              "read_only": false,
              "api_name": "Tax",
              "id": "111113000000005624"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003700",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003700",
                "type": "layout"
              }
            }
          ],
          "views": {
            "display_label": "Default List View",
            "name": "All_Quotes",
            "id": "111113000000053897",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Sales Orders",
          "shared_type": "private",
          "api_name": "Sales_Orders",
          "permissions": {
            "view": true,
            "edit": false,
            "edit_shared_records": false,
            "create": false,
            "delete": false
          },
          "id": "111113000000002778",
          "filters": [
            {
              "display_label": "Contact Name",
              "api_name": "Contact_Name",
              "id": "111113000000005652"
            }
          ],
          "fields": [
            {
              "read_only": false,
              "api_name": "Subject",
              "id": "111113000000005640"
            },
            {
              "read_only": false,
              "api_name": "Deal_Name",
              "id": "111113000000005642"
            },
            {
              "read_only": false,
              "api_name": "Contact_Name",
              "id": "111113000000005652"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005676"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000005678"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005680"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000005698"
            },
            {
              "read_only": false,
              "api_name": "Ordered_Items",
              "permissions": [
                {
                  "iscustomizable": false,
                  "view": true
                },
                {
                  "iscustomizable": true,
                  "edit": true
                },
                {
                  "iscustomizable": false,
                  "create": true
                },
                {
                  "iscustomizable": true,
                  "delete": true
                }
              ],
              "id": "111113000000005728"
            },
            {
              "read_only": false,
              "api_name": "Product_Details",
              "id": "111113000000005722"
            },
            {
              "read_only": false,
              "api_name": "Quote_Name",
              "id": "111113000000005646"
            },
            {
              "read_only": false,
              "api_name": "Grand_Total",
              "id": "111113000000005738"
            },
            {
              "read_only": true,
              "api_name": "SO_Number",
              "id": "111113000000005638"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000005694"
            },
            {
              "read_only": false,
              "api_name": "Sub_Total",
              "id": "111113000000005730"
            },
            {
              "read_only": false,
              "api_name": "Discount_Type__s",
              "id": "111113000000005740"
            },
            {
              "read_only": false,
              "api_name": "Discount_Percentage__s",
              "id": "111113000000005742"
            },
            {
              "read_only": false,
              "api_name": "Discount",
              "id": "111113000000005732"
            },
            {
              "read_only": false,
              "api_name": "Tax",
              "id": "111113000000005734"
            },
            {
              "read_only": false,
              "api_name": "Adjustment",
              "id": "111113000000005736"
            },
            {
              "read_only": false,
              "api_name": "Sequence_Number",
              "id": "111113000000005744"
            },
            {
              "read_only": false,
              "api_name": "Name",
              "id": "111113000000005746"
            },
            {
              "read_only": false,
              "api_name": "Owner",
              "id": "111113000000005748"
            },
            {
              "read_only": false,
              "api_name": "Created_By",
              "id": "111113000000005750"
            },
            {
              "read_only": false,
              "api_name": "Modified_By",
              "id": "111113000000005752"
            },
            {
              "read_only": false,
              "api_name": "Created_Time",
              "id": "111113000000005754"
            },
            {
              "read_only": false,
              "api_name": "Modified_Time",
              "id": "111113000000005756"
            },
            {
              "read_only": false,
              "api_name": "Last_Activity_Time",
              "id": "111113000000005758"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005762"
            },
            {
              "read_only": false,
              "api_name": "Parent_Id",
              "id": "111113000000005764"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005766"
            },
            {
              "read_only": false,
              "api_name": "Exchange_Rate",
              "id": "111113000000005768"
            },
            {
              "read_only": false,
              "api_name": "Product_Name",
              "id": "111113000000005770"
            },
            {
              "read_only": false,
              "api_name": "Description",
              "id": "111113000000005772"
            },
            {
              "read_only": false,
              "api_name": "Quantity",
              "id": "111113000000005774"
            },
            {
              "read_only": false,
              "api_name": "Total_After_Discount",
              "id": "111113000000005784"
            },
            {
              "read_only": false,
              "api_name": "Line_Tax",
              "id": "111113000000005790"
            },
            {
              "read_only": false,
              "api_name": "Total",
              "id": "111113000000005780"
            },
            {
              "read_only": false,
              "api_name": "Discount_Type__s",
              "id": "111113000000005794"
            },
            {
              "read_only": false,
              "api_name": "Discount_Percentage__s",
              "id": "111113000000005796"
            },
            {
              "read_only": false,
              "api_name": "List_Price",
              "id": "111113000000005778"
            },
            {
              "read_only": false,
              "api_name": "Discount",
              "id": "111113000000005782"
            },
            {
              "read_only": false,
              "api_name": "Tax",
              "id": "111113000000005786"
            },
            {
              "read_only": false,
              "api_name": "Net_Total",
              "id": "111113000000005788"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003686",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003686",
                "type": "layout"
              }
            }
          ],
          "views": {
            "display_label": "Default List View",
            "name": "All_SalesOrders",
            "id": "111113000000053903",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Purchase Orders",
          "shared_type": "private",
          "api_name": "Purchase_Orders",
          "permissions": {
            "view": true,
            "edit": false,
            "edit_shared_records": false,
            "create": false,
            "delete": false
          },
          "id": "111113000000002782",
          "filters": [
            {
              "display_label": "Contact Name",
              "api_name": "Contact_Name",
              "id": "111113000000005806"
            }
          ],
          "fields": [
            {
              "read_only": false,
              "api_name": "Subject",
              "id": "111113000000005802"
            },
            {
              "read_only": false,
              "api_name": "Contact_Name",
              "id": "111113000000005806"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005832"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000005834"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005836"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000005854"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000005850"
            },
            {
              "read_only": false,
              "api_name": "Purchase_Items",
              "permissions": [
                {
                  "iscustomizable": false,
                  "view": true
                },
                {
                  "iscustomizable": true,
                  "edit": true
                },
                {
                  "iscustomizable": false,
                  "create": true
                },
                {
                  "iscustomizable": true,
                  "delete": true
                }
              ],
              "id": "111113000000005886"
            },
            {
              "read_only": false,
              "api_name": "Sub_Total",
              "id": "111113000000005888"
            },
            {
              "read_only": false,
              "api_name": "Product_Details",
              "id": "111113000000005880"
            },
            {
              "read_only": false,
              "api_name": "Grand_Total",
              "id": "111113000000005896"
            },
            {
              "read_only": false,
              "api_name": "Discount_Type__s",
              "id": "111113000000005898"
            },
            {
              "read_only": false,
              "api_name": "Discount_Percentage__s",
              "id": "111113000000005900"
            },
            {
              "read_only": false,
              "api_name": "Discount",
              "id": "111113000000005890"
            },
            {
              "read_only": false,
              "api_name": "Tax",
              "id": "111113000000005892"
            },
            {
              "read_only": false,
              "api_name": "Adjustment",
              "id": "111113000000005894"
            },
            {
              "read_only": false,
              "api_name": "Sequence_Number",
              "id": "111113000000005902"
            },
            {
              "read_only": false,
              "api_name": "Name",
              "id": "111113000000005904"
            },
            {
              "read_only": false,
              "api_name": "Owner",
              "id": "111113000000005906"
            },
            {
              "read_only": false,
              "api_name": "Created_By",
              "id": "111113000000005908"
            },
            {
              "read_only": false,
              "api_name": "Modified_By",
              "id": "111113000000005910"
            },
            {
              "read_only": false,
              "api_name": "Created_Time",
              "id": "111113000000005912"
            },
            {
              "read_only": false,
              "api_name": "Modified_Time",
              "id": "111113000000005914"
            },
            {
              "read_only": false,
              "api_name": "Last_Activity_Time",
              "id": "111113000000005916"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005920"
            },
            {
              "read_only": false,
              "api_name": "Parent_Id",
              "id": "111113000000005922"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005924"
            },
            {
              "read_only": false,
              "api_name": "Exchange_Rate",
              "id": "111113000000005926"
            },
            {
              "read_only": false,
              "api_name": "Product_Name",
              "id": "111113000000005928"
            },
            {
              "read_only": false,
              "api_name": "Description",
              "id": "111113000000005930"
            },
            {
              "read_only": false,
              "api_name": "Quantity",
              "id": "111113000000005932"
            },
            {
              "read_only": false,
              "api_name": "List_Price",
              "id": "111113000000005936"
            },
            {
              "read_only": false,
              "api_name": "Discount",
              "id": "111113000000005940"
            },
            {
              "read_only": false,
              "api_name": "Total_After_Discount",
              "id": "111113000000005942"
            },
            {
              "read_only": false,
              "api_name": "Line_Tax",
              "id": "111113000000005948"
            },
            {
              "read_only": false,
              "api_name": "Net_Total",
              "id": "111113000000005946"
            },
            {
              "read_only": false,
              "api_name": "Tax",
              "id": "111113000000005944"
            },
            {
              "read_only": false,
              "api_name": "Total",
              "id": "111113000000005938"
            },
            {
              "read_only": false,
              "api_name": "Discount_Type__s",
              "id": "111113000000005952"
            },
            {
              "read_only": false,
              "api_name": "Discount_Percentage__s",
              "id": "111113000000005954"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003696",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003696",
                "type": "layout"
              }
            }
          ],
          "views": {
            "display_label": "Default List View",
            "name": "All_PurchaseOrders",
            "id": "111113000000053909",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Invoices",
          "shared_type": "private",
          "api_name": "Invoices",
          "permissions": {
            "view": true,
            "edit": false,
            "edit_shared_records": false,
            "create": false,
            "delete": false
          },
          "id": "111113000000002786",
          "filters": [
            {
              "display_label": "Contact Name",
              "api_name": "Contact_Name",
              "id": "111113000000005978"
            }
          ],
          "fields": [
            {
              "read_only": false,
              "api_name": "Subject",
              "id": "111113000000005960"
            },
            {
              "read_only": false,
              "api_name": "Contact_Name",
              "id": "111113000000005978"
            },
            {
              "read_only": false,
              "api_name": "Deal_Name__s",
              "id": "111113000000005984"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005992"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000005994"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005996"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000006014"
            },
            {
              "read_only": false,
              "api_name": "Invoiced_Items",
              "permissions": [
                {
                  "iscustomizable": false,
                  "view": true
                },
                {
                  "iscustomizable": true,
                  "edit": true
                },
                {
                  "iscustomizable": false,
                  "create": true
                },
                {
                  "iscustomizable": true,
                  "delete": true
                }
              ],
              "id": "111113000000006044"
            },
            {
              "read_only": false,
              "api_name": "Sales_Order",
              "id": "111113000000005962"
            },
            {
              "read_only": true,
              "api_name": "Invoice_Number",
              "id": "111113000000005958"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000006010"
            },
            {
              "read_only": false,
              "api_name": "Product_Details",
              "id": "111113000000006038"
            },
            {
              "read_only": false,
              "api_name": "Sub_Total",
              "id": "111113000000006046"
            },
            {
              "read_only": false,
              "api_name": "Grand_Total",
              "id": "111113000000006054"
            },
            {
              "read_only": false,
              "api_name": "Discount_Type__s",
              "id": "111113000000006056"
            },
            {
              "read_only": false,
              "api_name": "Discount_Percentage__s",
              "id": "111113000000006058"
            },
            {
              "read_only": false,
              "api_name": "Discount",
              "id": "111113000000006048"
            },
            {
              "read_only": false,
              "api_name": "Tax",
              "id": "111113000000006050"
            },
            {
              "read_only": false,
              "api_name": "Adjustment",
              "id": "111113000000006052"
            },
            {
              "read_only": false,
              "api_name": "Sequence_Number",
              "id": "111113000000006060"
            },
            {
              "read_only": false,
              "api_name": "Name",
              "id": "111113000000006062"
            },
            {
              "read_only": false,
              "api_name": "Owner",
              "id": "111113000000006064"
            },
            {
              "read_only": false,
              "api_name": "Created_By",
              "id": "111113000000006066"
            },
            {
              "read_only": false,
              "api_name": "Modified_By",
              "id": "111113000000006068"
            },
            {
              "read_only": false,
              "api_name": "Created_Time",
              "id": "111113000000006070"
            },
            {
              "read_only": false,
              "api_name": "Modified_Time",
              "id": "111113000000006072"
            },
            {
              "read_only": false,
              "api_name": "Last_Activity_Time",
              "id": "111113000000006074"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000006078"
            },
            {
              "read_only": false,
              "api_name": "Parent_Id",
              "id": "111113000000006080"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000006082"
            },
            {
              "read_only": false,
              "api_name": "Exchange_Rate",
              "id": "111113000000006084"
            },
            {
              "read_only": false,
              "api_name": "Product_Name",
              "id": "111113000000006086"
            },
            {
              "read_only": false,
              "api_name": "Description",
              "id": "111113000000006088"
            },
            {
              "read_only": false,
              "api_name": "Quantity",
              "id": "111113000000006090"
            },
            {
              "read_only": false,
              "api_name": "Total_After_Discount",
              "id": "111113000000006100"
            },
            {
              "read_only": false,
              "api_name": "Line_Tax",
              "id": "111113000000006106"
            },
            {
              "read_only": false,
              "api_name": "Discount_Type__s",
              "id": "111113000000006110"
            },
            {
              "read_only": false,
              "api_name": "List_Price",
              "id": "111113000000006094"
            },
            {
              "read_only": false,
              "api_name": "Discount",
              "id": "111113000000006098"
            },
            {
              "read_only": false,
              "api_name": "Tax",
              "id": "111113000000006102"
            },
            {
              "read_only": false,
              "api_name": "Total",
              "id": "111113000000006096"
            },
            {
              "read_only": false,
              "api_name": "Net_Total",
              "id": "111113000000006104"
            },
            {
              "read_only": false,
              "api_name": "Discount_Percentage__s",
              "id": "111113000000006112"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003692",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003692",
                "type": "layout"
              }
            }
          ],
          "views": {
            "display_label": "Default List View",
            "name": "All_Invoices",
            "id": "111113000000053924",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Cases",
          "shared_type": "private",
          "api_name": "Cases",
          "permissions": {
            "view": true,
            "edit": false,
            "edit_shared_records": false,
            "create": false,
            "delete": false
          },
          "id": "111113000000002760",
          "filters": [
            {
              "display_label": "Related To",
              "api_name": "Related_To",
              "id": "111113000000005092"
            }
          ],
          "fields": [
            {
              "read_only": false,
              "api_name": "Status",
              "id": "111113000000005080"
            },
            {
              "read_only": false,
              "api_name": "Case_Origin",
              "id": "111113000000005088"
            },
            {
              "read_only": false,
              "api_name": "Subject",
              "id": "111113000000005090"
            },
            {
              "read_only": false,
              "api_name": "Related_To",
              "id": "111113000000005092"
            },
            {
              "read_only": false,
              "api_name": "Deal_Name",
              "id": "111113000000005096"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005118"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000005120"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005122"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000005144"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000005140"
            },
            {
              "read_only": false,
              "api_name": "Product_Name",
              "id": "111113000000005082"
            },
            {
              "read_only": true,
              "api_name": "Case_Number",
              "id": "111113000000005076"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003688",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003688",
                "type": "layout"
              }
            }
          ],
          "views": {
            "display_label": "Default List View",
            "name": "All_Cases",
            "id": "111113000000053504",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Custom Module",
          "shared_type": "private",
          "api_name": "Custom_Module",
          "permissions": {
            "view": true,
            "edit": false,
            "edit_shared_records": false,
            "create": false,
            "delete": false
          },
          "id": "111113000000125002",
          "filters": [
            {
              "display_label": "Lookup 1",
              "api_name": "Lookup_1",
              "id": "111113000000127669"
            }
          ],
          "fields": [
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000125065"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000125067"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000125071"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000125093"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000125111"
            },
            {
              "read_only": false,
              "api_name": "Name",
              "id": "111113000000125047"
            },
            {
              "read_only": false,
              "api_name": "Lookup_1",
              "id": "111113000000127669"
            },
            {
              "read_only": false,
              "api_name": "Multi_Select_Lookup_1",
              "id": "111113000000131001"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000125001",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000125001",
                "type": "layout"
              }
            }
          ],
          "views": {
            "display_label": "Default List View",
            "name": "CustomModule_Default_CustomView",
            "id": "111113000000125014",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Notes",
          "shared_type": "private",
          "api_name": "Notes",
          "permissions": {
            "view": true,
            "delete_attachment": false,
            "edit": false,
            "create": false,
            "create_attachment": false,
            "delete": false
          },
          "id": "111113000000002694",
          "filters": null,
          "fields": [
            {
              "read_only": false,
              "api_name": "Owner",
              "id": "111113000000004322"
            },
            {
              "read_only": false,
              "api_name": "Note_Title",
              "id": "111113000000004324"
            },
            {
              "read_only": false,
              "api_name": "Parent_Id",
              "id": "111113000000004328"
            },
            {
              "read_only": false,
              "api_name": "Created_By",
              "id": "111113000000004330"
            },
            {
              "read_only": false,
              "api_name": "Modified_By",
              "id": "111113000000004332"
            },
            {
              "read_only": false,
              "api_name": "Created_Time",
              "id": "111113000000004334"
            },
            {
              "read_only": false,
              "api_name": "Modified_Time",
              "id": "111113000000004336"
            },
            {
              "read_only": false,
              "api_name": "id",
              "id": "111113000000004338"
            },
            {
              "read_only": false,
              "api_name": "Associated_Id__s",
              "id": "111113000000004340"
            },
            {
              "read_only": false,
              "api_name": "Record_Status__s",
              "id": "111113000000004342"
            },
            {
              "read_only": false,
              "api_name": "Note_Content",
              "id": "111113000000004326"
            }
          ],
          "layouts": null,
          "views": null
        }
      ]
    }
  ]
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse1

API not supported for client portal user (API_NOT_SUPPORTED)

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "unsupported_login_user_type": "Client Portal User"
  },
  "message": "api not supported for client portal user",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse2

API not supported in sandbox

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "unsupported_environment": "sandbox"
  },
  "message": "api not supported in sandbox",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse3

API not supported

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "supported_domains": [
      "eu",
      "com",
      "in",
      "au",
      "ca",
      "cn",
      "jp"
    ]
  },
  "message": "api not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidPortalNameResponse1

No portal exists with the given portal name

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "No portal exists with the given portal name.",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_ClientPortal"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse2

NO_PERMISSION

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "NO_PERMISSION",
  "status": "error"
}
```
