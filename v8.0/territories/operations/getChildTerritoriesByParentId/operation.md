# GET /settings/territories/{id}/__child_territories
**Operation:** `getChildTerritoriesByParentId` — Get child territories by parent territory ID

> To retrieve the list of child territories for a specific parent territory in your Zoho CRM organization. Use the **ID** path parameter to specify the parent territory, and optional query parameters such as **filters**, **include**, **include_inner_details**, **page**, and **per_page** to narrow results and control pagination.


**Tags:** Territories

**Parameters:**
- `include` (query, string, optional) [maxLen=100, enum=[7 values]]: Include account_rule_criteria, lead_rule_criteria (or) deal_rule_criteria.
- `id` (path, string/int64, required): List of Territory Id
- `page` (query, integer/int32, optional) [min=1]: Page Numeber
- `per_page` (query, integer/int32, optional) [min=1, max=2000]: Per Page Number
- `filters` (query, object, optional): Filter Out the Territories based on Given Criteria
- `include_inner_details` (query, string, optional) [enum=['manager.zuid,manager.status', 'manager.zuid', 'manager.status']]: Include manager status & zuid

**Schemas:**
`BetweenFilterCriterionResponse`:
  > Represents the response for a filter criterion using the between and not_between comparators. The value is an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the range filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['between', 'not_between']] — Represents the range comparison operator returned for the criterion, indicating whether the field value falls within or outside the specified bounds.
Possible values:
between - Matches records where the field value falls within the specified range.
not_between - Matches records where the field value falls outside the specified range.
  - `value` (array of object) [minItems=2, maxItems=2] **REQ** — Contains the two boundary values — [lower_bound, upper_bound] — against which the field was evaluated for the between or not_between comparator.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the between filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`EqualFilterCriterionResponse`:
  > Represents the response for a filter criterion using the equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime; SimpleFilterCriterionValueNumber for integer, currency, or double; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup, ownerlookup, or userlookup; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the equal filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['equal']] — Represents the equal comparison operator returned for the criterion.
Possible values:
equal - Matches records where the field value equals the specified filter value.
  - `value` (object) **REQ** — Represents the filter value returned for the equal comparator. Contains a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueGeneralPredefined` (string) [enum=['${EMPTY}', '${NOTEMPTY}']] — Represents a predefined placeholder value applicable to any field data_type with the equal comparator.
Possible values:
${EMPTY} - Matches records where the field has no value.
${NOTEMPTY} - Matches records where the field has any non-empty value.
      - `SimpleFilterCriterionValueDateTimePredefined` (string) [enum=[22 values]] — Represents a predefined placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator.
      - `SimpleFilterCriterionValueNDaysPredefined` (string) [maxLen=255, pattern=^\$\{(LAST_N_|NEXT_N_)(DAYS|WEEKS|MONTHS|YEARS):([0-9]+)\}$] — Represents a predefined N-period range placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator. Follows the pattern ${NEXT_N_<PERIOD>:<n>} or ${LAST_N_<PERIOD>:<n>}, where PERIOD is DAYS, WEEKS, MONTHS, or YEARS and n is a positive integer. The current period is always excluded from the range.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'value', 'pre_defined', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the equal filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`EqualityFilterCriterionResponse`:
  oneOf:
    - `EqualFilterCriterionResponse` — Represents the response for a filter criterion using the equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime; SimpleFilterCriterionValueNumber for integer, currency, or double; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup, ownerlookup, or userlookup; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
    - `NotEqualFilterCriterionResponse` — Represents the response for a filter criterion using the not_equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text-based types; SimpleFilterCriterionValueNumber for numeric types; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup types; and SimpleFilterCriterionValueObjectPredefined for predefined user or role placeholders.
`FilterFieldBase`:
  > Represents the base field reference used in filter operations, containing minimal required properties. The field's data_type is not part of this object; resolve it from the corresponding FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `id` (string/int64) — Represents the unique ID of the field used for filter operations.
  - `api_name` (string) **REQ** — Represents the API name of the field used for filter application. Supports relationship notation, for example, Deals__r.Stage.
  additionalProperties: any
`GroupedFilterCriterionResponse`:
  > Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group` (array of object) [minItems=2, maxItems=25] **REQ** — Contains an array of filter conditions grouped together and evaluated with the specified logical operator.
    oneOf:
      - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
      - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group_operator` (string) **REQ** [enum=['AND', 'OR', 'and', 'or']] — Represents the logical operator applied between the filter conditions in the group.
Possible values:
AND - All conditions in the group must be satisfied.
OR - At least one condition in the group must be satisfied.
and - Equivalent to AND; all conditions in the group must be satisfied.
or - Equivalent to OR; at least one condition in the group must be satisfied.
  - `$disrupted` (boolean) — Indicates whether the grouped filter criterion is in a disrupted state, typically due to an invalid or unresolvable condition within the group.
`MultiSelectLookupFilterCriterionResponse`:
  > Represents the response for a filter criterion using the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
  - `field` (object) **REQ** — Represents the target field definition to which the multi-select lookup filter criterion was applied. The field has a data_type of multiuserlookup or multiselectlookup.
  - `comparator` (string) **REQ** [enum=['include_all', 'include_any', 'exclude_all', 'exclude_any']] — Represents the multi-select lookup comparison operator returned for the criterion. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
Possible values:
include_all - Matches records that include all specified lookup values.
include_any - Matches records that include at least one of the specified lookup values.
exclude_all - Matches records that exclude all specified lookup values.
exclude_any - Matches records that exclude at least one of the specified lookup values.
  - `value` (array of object `SimpleFilterCriterionValueObjectResponse`) [minItems=1, maxItems=500] **REQ** — Contains an array of lookup object references returned for the multi-select comparison.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the multi-select lookup filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`NotEqualFilterCriterionResponse`:
  > Represents the response for a filter criterion using the not_equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text-based types; SimpleFilterCriterionValueNumber for numeric types; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup types; and SimpleFilterCriterionValueObjectPredefined for predefined user or role placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the not-equal filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['not_equal']] — Represents the not-equal comparison operator returned for the criterion.
Possible values:
not_equal - Matches records where the field value does not equal the specified filter value.
  - `value` (object) **REQ** — Represents the filter value returned for the not_equal comparator. Contains a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'value', 'pre_defined', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the not-equal filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`OrderingFilterCriterionResponse`:
  > Represents the response for a filter criterion using the less_than, less_equal, greater_than, and greater_equal comparators. The value is a scalar; arrays and objects are not valid.
  - `field` (object) **REQ** — Represents the target field definition to which the ordering filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['less_than', 'less_equal', 'greater_than', 'greater_equal']] — Represents the ordering comparison operator returned for the criterion.
Possible values:
less_than - Matches records where the field value is less than the specified filter value.
less_equal - Matches records where the field value is less than or equal to the specified filter value.
greater_than - Matches records where the field value is greater than the specified filter value.
greater_equal - Matches records where the field value is greater than or equal to the specified filter value.
  - `value` (object) **REQ** — Represents the scalar filter value returned for the ordering comparator.
    anyOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the ordering filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`SetFilterCriterionResponse`:
  > Represents the response for a filter criterion using the in and not_in comparators. The value is an array of primitive values.
  - `field` (object) **REQ** — Represents the target field definition to which the set filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['in', 'not_in']] — Represents the set membership comparison operator returned for the criterion.
Possible values:
in - Matches records where the field value is in the specified set of values.
not_in - Matches records where the field value is not in the specified set of values.
  - `value` (array of object) [minItems=1, maxItems=500] **REQ** — Contains an array of primitive filter values returned for the set comparison.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the set filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`SimpleFilterCriterionResponse`:
  oneOf:
    - `EqualityFilterCriterionResponse` — Represents the response for an equality filter criterion that dispatches to either the EqualFilterCriterionResponse or NotEqualFilterCriterionResponse schema based on the comparator value.
    - `TextFilterCriterionResponse` — Represents the response for a filter criterion using the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value is a string scalar or array; SimpleFilterCriterionValueString applies to text-based field types.
    - `OrderingFilterCriterionResponse` — Represents the response for a filter criterion using the less_than, less_equal, greater_than, and greater_equal comparators. The value is a scalar; arrays and objects are not valid.
    - `BetweenFilterCriterionResponse` — Represents the response for a filter criterion using the between and not_between comparators. The value is an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `SetFilterCriterionResponse` — Represents the response for a filter criterion using the in and not_in comparators. The value is an array of primitive values.
    - `MultiSelectLookupFilterCriterionResponse` — Represents the response for a filter criterion using the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
`SimpleFilterCriterionValueObjectBase`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (string/int64) — Represents the unique ID of the lookup module record.
  - `name` (string) [maxLen=255] — Represents the display name of the lookup module record.
  additionalProperties: any
`SimpleFilterCriterionValueObjectPredefined`:
  oneOf:
      - `name` (string) **REQ** [enum=['${CURRENTUSER}']] — Represents the predefined placeholder for the currently logged-in user.
Possible values:
${CURRENTUSER} - Represents the currently logged-in user.
      - `id` (string) **REQ** [enum=['${CURRENTUSERROLE}']] — Represents the predefined placeholder for the logged-in user's role record ID.
Possible values:
${CURRENTUSERROLE} - Represents the role of the currently logged-in user.
      - `name` (string) [maxLen=255] — Represents an optional display label for the predefined role, such as Logged in User Role.
      additionalProperties: any
`SimpleFilterCriterionValueObjectResponse`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (object) **REQ**
  - `name` (object) **REQ**
  additionalProperties: any
`TextFilterCriterionResponse`:
  > Represents the response for a filter criterion using the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value is a string scalar or array; SimpleFilterCriterionValueString applies to text-based field types.
  - `field` (object) **REQ** — Represents the target field definition to which the text filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['like', 'not_like', 'starts_with', 'ends_with', 'contains', 'not_contains']] — Represents the text comparison operator returned for the criterion.
Possible values:
like - Matches records where the field value contains the specified pattern.
not_like - Matches records where the field value does not contain the specified pattern.
starts_with - Matches records where the field value begins with the specified string.
ends_with - Matches records where the field value ends with the specified string.
contains - Matches records where the field value contains the specified string.
not_contains - Matches records where the field value does not contain the specified string.
  - `value` (object) **REQ** — Represents the string filter value returned for the text comparator. Contains a scalar string or an array of string values.
    oneOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the text filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.

**Responses:**

- **200**: Returns the list of child territories for the specified territory. Use the **info** object to navigate through paginated results.
 — Schema: `TerritoryChildListResponse` [application/json]
    > Represents the response containing child territories with pagination details.
    schema: `TerritoryChildListResponse`
    - `territories` (array of object `TerritoryGETSchema`) [minItems=1, maxItems=200] **REQ** — Represents the list of child territory objects.
      schema: `TerritoryGETSchema`
      - `created_time` (string/date-time) **REQ** — Represents the date and time the territory record took effect, in ISO 8601 format.
      - `modified_time` (string/date-time) **REQ** — Represents the date and time when the territory was last modified, in ISO 8601 format.
      - `manager` (object) **REQ**
        oneOf:
            - `name` (string) **REQ** [maxLen=100] — Represents the display name of the territory manager.
            - `id` (string/int64) **REQ** — Represents the unique identifier of the territory manager.
            - `zuid` (string/int32) — Represents the Zoho User ID (ZUID) of the territory manager.
            - `status` (string) [enum=['deleted', 'rejected', 'active', 'closed', 'disabled']] — Represents the current status of the territory manager. Possible values: **deleted**, **rejected**, **active**, **closed**, **disabled**.
            type: null [const=None] — Represents the absence of a territory manager.
      - `reporting_to` (object) **REQ**
        oneOf:
            - `name` (string) **REQ** [maxLen=100] — Represents the display name of the parent territory.
            - `id` (string/int64) **REQ** — Represents the unique identifier of the parent territory.
            type: null [const=None] — Represents the absence of a parent territory for this territory.
      - `permission_type` (string) **REQ** [enum=['read_write_delete', 'read_only']] — Represents the access permission for users in this territory. Possible values: **read_write_delete**, **read_only**.
      - `modified_by` (object) **REQ** — Represents the user who last modified the territory.
        - `name` (string) **REQ** [maxLen=100] — Represents the display name of the user who last modified the territory.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the user who last modified the territory.
      - `description` (object) **REQ**
        oneOf:
            type: null [const=None] — Represents the absence of a description for the territory.
            type: string [maxLen=250] — Represents the description of the territory.
      - `id` (string/int64) **REQ** — Represents the unique identifier of the territory.
      - `created_by` (object) **REQ** — Represents the user who created the territory.
        - `name` (string) **REQ** [maxLen=100] — Represents the display name of the user who created the territory.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the user who created the territory.
      - `account_rule_criteria` (object) — Represents the criteria used to auto-assign accounts to the territory.
        oneOf:
          - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
          - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
            type: null [const=None] — Represents the absence of an account rule criteria for the territory.
      - `deal_rule_criteria` (object) — Represents the criteria used to auto-assign deals to the territory.
        oneOf:
          - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
          - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
            type: null [const=None] — Represents the absence of a deal rule criteria for the territory.
      - `lead_rule_criteria` (object) — Represents the criteria used to auto-assign leads to the territory.
        oneOf:
          - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
          - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
            type: null [const=None] — Represents the absence of a lead rule criteria for the territory.
      - `name` (string) **REQ** [maxLen=50] — Represents the display name of the territory.
      - `api_name` (string) **REQ** [maxLen=100] — Represents the unique API name of the territory used in API requests.
    - `info` (object `InfoSchema`) **REQ** — Pagination metadata for the response.
      schema: `InfoSchema`
      - `per_page` (integer/int32) **REQ** [min=1, max=2000] — Represents the number of records returned per page.
      - `count` (integer/int32) **REQ** [min=0] — Represents the total number of records returned in the current page.
      - `page` (integer/int32) **REQ** [min=1] — Represents the current page number of the paginated results.
      - `more_records` (boolean) **REQ** — Indicates whether more records are available in subsequent pages.

- **204**: No child territories exist for the specified territory. The response body is empty.


- **400**: The territory ID in the request URL is invalid, or the territory management feature is not enabled for this organization.
**Resolution:** The territory ID in the URL must be a valid, existing territory identifier, and the territory management feature must be enabled in the organization settings.
 [application/json]
    > Represents the error response returned when the request to retrieve child territories fails due to an invalid territory ID in the URL or because the territory management feature is not enabled.

    oneOf:
      - `TerritoryInvalidUrlPathErrorSchema` — Represents the error response when an invalid value is provided in the URL path of a territory request.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request. Possible values: **INVALID_DATA**.
        - `details` (object) **REQ** — Represents additional details about the error, including the index of the invalid URL path segment.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the index of the URL path segment where the invalid value was found.
        - `message` (string) **REQ** [maxLen=100, enum=[4 values]] — Represents the error message returned when an invalid value is provided in the URL path. Possible values: **The given territory id is invalid**, **the id given seems to be invalid**, **The record Id given seems to be invalid**, **Invalid Territory Id**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryFeatureNotEnabledError` — Represents the error response when the territory feature is not enabled for the organization.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **401**: Authentication failure due to missing, expired, or invalid OAuth token.
**Resolution:** A new access token must be generated with the required scope for this API.
 — Schema: `UnauthorizedError` [application/json]
    > Represents the error response when authentication fails for the request.
    schema: `UnauthorizedError`
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the request. Possible values: **AUTHENTICATION_FAILURE**.
    - `details` (object) **REQ** — Represents additional details about the authentication error.
    - `message` (string) **REQ** [maxLen=100, enum=['Authentication failed']] — Represents the error message returned when authentication fails. Possible values: **Authentication failed**.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

**Scopes:** ZohoCRM.settings.territories.READ
