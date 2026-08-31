# GET /settings/custom_views
**Operation:** `getCustomViews` — Get All Custom Views
> To retrieve the list of all Custom Views configured for a specified module in your Zoho CRM organization.

**Tags:** Custom Views

**Parameters:**
- `module` (query, string, required) [maxLen=25]: Specify the API name of the module for which to manage Custom Views. Refer to the Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module IDs.resource for valid values.
- `filters` (query, object, optional): Specify the filter criteria for retrieving specific Custom Views. Accepts a filter object to narrow down results based on Custom View properties.
- `page` (query, integer/int32, optional) [min=1]: Specify the page number for pagination.
- `per_page` (query, integer/int32, optional) [min=1, max=200]: Specify the number of Custom Views to return per page.
- `ids` (query, array, required) [minItems=1, maxItems=100, uniqueItems] {style=form, explode=False}: Specify the comma-separated list of unique IDs of the Custom Views to delete. Accepts up to 100 IDs. Use the [Get Custom Views API](custom_views.yaml#$.paths./settings/custom_views.get) to retrieve the custom view IDs.
- `scope` (query, string, optional) [enum=['created_by_me', 'shared_with_me', 'public_views', 'other_users_views']]: Represents the category of custom views to fetch. Allowed values are 'created_by_me', 'shared_with_me', 'public_views', 'other_users_views'.
- `favourite` (query, boolean, optional): Filter custom views by favourite status. Set to true to fetch only favourite custom views.

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
`FilterCriterionResponse`:
  oneOf:
    - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
    - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
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
`UserReference`:
  > Represents a user reference containing the user ID and display name.
  - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique ID of the user.
  - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user.

**Responses:**

- **200**: Returns the list of Custom Views for the specified module, along with pagination metadata. — Schema: `GetAllCustomViewsResponse` [application/json]
    > Get all custom views of a module
    schema: `GetAllCustomViewsResponse`
    - `custom_views` (array of object) [maxItems=200] **REQ** — List of custom views
      schema: `CustomViewGetItem`
      - `name` (string) **REQ** [maxLen=50] — Represents the name of the Custom View.
      - `display_value` (string) **REQ** [maxLen=50] — Represents the display label of the Custom View as shown to users.
      - `$modified_criteria` (boolean) — Indicates whether the filter criteria of the Custom View has been modified since it was originally created.
Possible values:
**true** - The criteria has been modified.
**false** - The criteria has not been modified.
      - `access_type` (string) [enum=['shared', 'public', 'only_to_me']] — Represents the access type of the Custom View.
Possible values:
**shared** - The view is shared with selected users, roles, groups, or territories.
**public** - The view is accessible to all users in the organization.
**only_to_me** - The view is private and accessible only to the creator.
      - `created_time` (string/date-time) **REQ** [nullable] — Represents the date and time when the Custom View creation occurred.
      - `modified_time` (string/date-time) **REQ** [nullable] — Modification Time of the Custom View
      - `last_accessed_time` (string/date-time) **REQ** [nullable] — Represents the date and time when the Custom View was last accessed. A null value indicates the view has not been accessed.
      - `system_name` (string) **REQ** [maxLen=50, nullable] — Represents the system-defined name of the Custom View. A null value indicates the view does not have a system name.
      - `category` (string) [enum=['public_views', 'other_users_views', 'shared_with_me', 'created_by_me']] — Represents the category of the Custom View.
Possible values:
**public_views** - Views accessible to all users in the organization.
**other_users_views** - Views created by other users in the organization.
**shared_with_me** - Views shared with the current user.
**created_by_me** - Views created by the current user.
      - `default` (boolean) **REQ** — Indicates whether the Custom View is set as the default view for the module.
Possible values:
**true** - This is the default view.
**false** - This is not the default view.
      - `system_defined` (boolean) **REQ** — Indicates whether the Custom View is a system-defined view created by Zoho CRM.
Possible values:
**true** - The view is system-defined.
**false** - The view is user-defined.
      - `locked` (boolean) **REQ** — Indicates whether the Custom View is locked and cannot be modified by users.
Possible values:
**true** - The view is locked.
**false** - The view is not locked.
      - `favorite` (integer/int32) [nullable] — Represents the favorite order of the Custom View. A null value indicates the view is not marked as a favorite.
      - `offline` (boolean) — Indicates whether the Custom View is available in offline mode.
Possible values:
**true** - The view is available offline.
**false** - The view is not available offline.
      - `criteria` (object `CustomViewCriterionResponse`) — Represents the filter criteria of the Custom View
        oneOf:
          - `FilterCriterionResponse` — Represents the top-level filter criterion returned in the response, supporting both simple field-based filters and complex grouped filters with logical operators.
            type: null — No criteria is applied. The custom view returns all records.
      - `cross_filters` (object `CustomViewCrossFilterCriterionResponse`) — Cross-filter criteria of the Custom View
        oneOf:
          - `CrossFiltersResponse` — Represents the list of cross-filter objects returned in the response, applied to the Custom View.
            type: array of object [minItems=0, maxItems=3]
              - `include_objects` (boolean) **REQ** — Indicates whether records with matching related records were included in the filtered results.
              - `relation` (object) **REQ**
                schema: `ChildRelationshipReference`
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the child relationship module used to identify the relationship.
                - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique ID of the child relationship module record.
                - `$disrupted` (boolean) **REQ** — Indicates whether the related module relationship referenced by this criterion is in a disrupted state, typically due to an unresolvable or deleted relationship definition.
              - `criteria` (object `FilterCriterionResponse`) **REQ** — Represents the top-level filter criterion returned in the response, supporting both simple field-based filters and complex grouped filters with logical operators.
            type: null — No cross-filter criteria is applied.
      - `shared_to` (array of object) [maxItems=250, nullable] — Represents the list of users, roles, groups, or territories the Custom View is shared with.
        - `name` (string) [maxLen=255] — Name of the user/group
        - `id` (string/int64) **REQ** [maxLen=25] — ID of the user/group
        - `type` (string) **REQ** [enum=['territories', 'roles', 'groups', 'users']] — Represents the type of the shared-to entity.
Possible values:
**territories** - The view is shared with a territory.
**roles** - The view is shared with a role.
**groups** - The view is shared with a group.
**users** - The view is shared with a specific user.
        - `subordinates` (boolean) [nullable] — Specify true if subordinates are included, false otherwise
      - `modified_by` (object) **REQ**
        oneOf:
          - `UserReference` — Represents a user reference containing the user ID and display name.
            type: null — No user associated
      - `created_by` (object) **REQ**
        oneOf:
          - `UserReference` — Represents a user reference containing the user ID and display name.
            type: null — No user associated
      - `fields` (array of object) [maxItems=250] — Represents the list of fields included in the Custom View, each with display and pin configuration details.
        - `api_name` (string) [maxLen=255, nullable] — Represents the API name of the field included in the Custom View.
        - `id` (string/int64) [maxLen=25, nullable] — Represents the unique ID of the field included in the Custom View.
        - `_pin` (boolean) — Indicates whether the field is pinned in the Custom View.
Possible values:
**true** - The field is pinned.
**false** - The field is not pinned.
        - `_width` (integer/int32) — Represents the display width of the field in pixels.
        - `_pin_order` (integer/int32) — Represents the order of the pinned field within the Custom View.
      - `sort_by` (object) — Represents the field used to sort the records in the Custom View.
        oneOf:
          - `FieldReference` — Represents a reference to a field in the Custom View, identified by its API name and unique ID.
            - `api_name` (string) [maxLen=255, nullable] — Represents the API name of the field. A null value indicates no field is selected.
            - `id` (string/int64) [maxLen=25, nullable] — Represents the unique ID of the field. A null value indicates no field is selected.
            type: null — No sort is applied
      - `sort_order` (object) — Represents the sort order applied to the records in the Custom View.
        oneOf:
            type: string [enum=['asc', 'desc']] — Represents the sort order applied to the Custom View.
Possible values:
**asc** - Ascending order.
**desc** - Descending order.
            type: null — Represents no sort order applied to the Custom View.
      - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique ID of the Custom View.
    - `info` (object) **REQ** — Pagination info for the response
      schema: `CustomViewInfo`
      - `per_page` (integer/int32) **REQ** — Represents the number of Custom Views returned per page.
      - `count` (integer/int32) **REQ** — Represents the total number of Custom Views available for the specified module.
      - `page` (integer/int32) **REQ** — Represents the current page number of the paginated response.
      - `more_records` (boolean) **REQ** — Indicates whether more records are available beyond the current page.
Possible values:
**true** - More records are available.
**false** - No more records are available.
      - `default` (string/int64) [maxLen=255] — Represents the ID of the default Custom View for the module.
      - `translation` (object) — Represents the localized display labels for the Custom View category names.
        - `public_views` (string) **REQ** [maxLen=255] — Represents the display label for the public views category of Custom Views.
        - `other_users_views` (string) **REQ** [maxLen=255] — Represents the display label for the other users' views category of Custom Views.
        - `shared_with_me` (string) **REQ** [maxLen=255] — Represents the display label for the shared with me category of Custom Views.
        - `created_by_me` (string) **REQ** [maxLen=255] — Represents the display label for the created by me category of Custom Views.

- **400**: The request URL or module is invalid. Resolution: A valid module API name must be provided in the **module** query parameter. [application/json]
    > Represents the error response for an invalid get Custom Views request.
    oneOf:
      - `UrlErrorResponseForCustomView` — Flat error: URL/module validation failures
        oneOf:
          - `UnableToParseDataTypeError` — Data type could not be parsed from the request
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
            - `code` (string) **REQ** [enum=['UNABLE_TO_PARSE_DATA_TYPE']] — Represents the error code for the data type parse failure.
Possible values:
**UNABLE_TO_PARSE_DATA_TYPE** - The server could not parse the data type from the request.
            - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the data type parse failure.
            - `details` (object) **REQ** — Represents the additional details about the data type parse failure.
          - `InvalidUrlPatternError` — Request URL does not match any known pattern
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
            - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code for the invalid URL pattern.
Possible values:
**INVALID_URL_PATTERN** - The request URL does not match any known pattern.
            - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the URL pattern issue.
            - `details` (object) **REQ** — Represents the additional details about the URL pattern error.
          - `InvalidModuleError` — The specified module is invalid or does not exist
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
            - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for the invalid module error.
Possible values:
**INVALID_MODULE** - The specified module does not exist or is invalid.
            - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid module.
            - `details` (object) **REQ** — Represents the additional details about the invalid module error.
              - `param_name` (string) [maxLen=255] — Name of the invalid parameter
      - `RequiredParameterMissingResponse` — Flat error: required query parameter missing
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for the missing required parameter.
Possible values:
**REQUIRED_PARAM_MISSING** - A required query parameter is absent from the request.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing parameter.
        - `details` (object) **REQ** — Represents the details of the missing parameter.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the missing required parameter.
      - `FilterInvalidParamDataType` — Filter criteria error: invalid filter param data type
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error classification code for this response.
Possible values:
**INVALID_DATA** - The filter parameter was supplied with an incorrect data type.
        - `details` (object) **REQ** — Contains structured details about the data type mismatch, including the name of the offending filter parameter and the data type it is expected to carry.
          - `expected_data_type` (string) **REQ** [maxLen=256] — Represents the data type that the filter parameter is required to carry for the request to be valid.
          - `param_name` (string) **REQ** [maxLen=256] — Represents the name of the query or body parameter — such as `filters` — that carries the filter criteria and was supplied with an invalid data type.
        - `message` (string) **REQ** [maxLen=512] — Represents a descriptive message explaining the data type error encountered for the filter parameter.
        - `status` (string) **REQ** [enum=['error']] — Represents the outcome of the request.
Possible values:
**error** - The request failed due to an invalid filter parameter data type.
      - `FilterNotSupportedApiName` — Filter criteria error: unsupported API name
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Indicates the error classification assigned to this response.
Possible values:
**NOT_SUPPORTED** - The referenced field API name is not permitted for use in filter criteria.
        - `details` (object) **REQ** — Contains the contextual details identifying the unsupported field that caused the error, including its API name, its location within the filter expression, and the name of the filter parameter involved.
          - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the field that is not supported for use in filter criteria and triggered this error.
          - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSONPath location of the unsupported field within the filter expression.
          - `param_name` (string) **REQ** [maxLen=256] — Represents the name of the filter request parameter that carried the unsupported field API name.
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive message summarizing the nature of the error returned by the API.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome status of the API response.
Possible values:
**error** - The request failed because an unsupported field API name was used in the filter criteria.
      - `FilterFieldComparatorValueMissing` — Filter criteria error: field comparator value missing
        - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Indicates the error classification assigned to this response.
Possible values:
**DEPENDENT_FIELD_MISSING** - A filter field's required comparator value is absent because its upstream dependee field was not supplied in the filter criteria.
        - `details` (object) **REQ** — Contains structured details about the missing comparator value error, identifying the field in error, the upstream dependee field that constrains it, and the filter parameter context in which the violation occurred.
          - `dependee` (object) **REQ** — Represents the upstream field whose value constrains the comparator requirements of the field currently in error. Contains the API name and JSONPath location of that upstream dependee field within the filter expression.
            - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the upstream dependee field whose value constrains the comparator requirements of the field currently in error.
            - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSONPath location of the upstream dependee field within the filter expression.
          - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the filter field whose comparator value is absent, identifying which field in the filter expression triggered the error.
          - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSONPath location of the field in error within the filter expression, pinpointing where the missing comparator value was detected.
          - `param_name` (string) **REQ** [maxLen=256] — Indicates the name of the filter parameter that carries the filter criteria in which the missing comparator value was detected.
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive message summarizing the missing comparator value error.
        - `status` (string) **REQ** [enum=['error']] — Represents the outcome status of the response.
Possible values:
**error** - The request failed because a required comparator value was absent from the filter criteria.
      - `FilterFieldComparatorMismatch` — Filter criteria error: field comparator mismatch
        - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Indicates the error type for this response.
Possible values:
**DEPENDENT_MISMATCH** - The comparator supplied for the field does not match the set of comparators permitted given the current value of the dependee field.
        - `details` (object) **REQ** — Contains structured details about the comparator mismatch, identifying the field in error, the upstream dependee field whose value constrains valid comparators, and the set of comparator values that are permitted.
          - `dependee` (object) **REQ** — Represents the upstream field whose current value determines which comparators are valid for the field identified in `api_name`. Contains the upstream field's API name and its location within the filter expression.
            - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the upstream dependee field whose value constrains the set of comparators permitted for the field currently in error.
            - `json_path` (string) **REQ** [maxLen=512] — Contains the JSONPath expression locating the dependee field within the filter expression submitted in the request.
          - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the field whose supplied comparator value does not match the comparators permitted given the current value of the dependee field.
          - `json_path` (string) **REQ** [maxLen=512] — Contains the JSONPath expression locating the field in error within the filter expression submitted in the request.
          - `supported_values` (array of string) [minItems=1, maxItems=100, uniqueItems] **REQ** — Contains the complete set of comparator values that are permitted for the field in error, as determined by the current value of the dependee field.
            items: [maxLen=256]
          - `param_name` (string) **REQ** [maxLen=256] — Indicates the name of the filter query parameter that carries the filter expression containing the comparator mismatch.
        - `message` (string) **REQ** [maxLen=512] — Represents a short, descriptive summary of the comparator-field dependency violation.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the request.
Possible values:
**error** - The request failed due to a comparator value mismatch in the filter criteria.
      - `FilterFieldValueMismatch` — Filter criteria error: field value mismatch
        - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Indicates the category of error associated with this response.
Possible values:
**DEPENDENT_MISMATCH** - A filter field's value has a data type that conflicts with the requirement set by the dependee field.
        - `details` (object) **REQ** — Contains diagnostic details identifying the offending filter field, its expected data type, the dependee field that governs that expectation, and the filter parameter in which the mismatch was detected.
          - `dependee` (object) **REQ** — Represents the field whose current value dictates the required data type for the offending filter field.
            - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the dependee field whose value drives the data type requirement for the offending filter field.
            - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSON path locating the dependee field within the request payload.
          - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the filter field whose supplied value does not match the data type required by the dependee field.
          - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSON path locating the filter field whose value carries the data type mismatch within the request payload.
          - `expected_data_type` (string) **REQ** [maxLen=256] — Indicates the data type expected by the dependee field against which the submitted filter value was validated.
          - `param_name` (string) **REQ** [maxLen=256] — Represents the filter-specific query parameter name associated with the field that failed value validation.
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive explanation of the filter field value mismatch error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome status of the response.
Possible values:
**error** - The request failed because a filter field value did not match the type required by the dependee field.
      - `FilterComparatorValueMismatch` — Filter criteria error: comparator value mismatch
        - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Indicates the classification of the error.
Possible values:
**DEPENDENT_MISMATCH** - The comparator-driven value failed validation due to constraints imposed by the dependee field.
        - `details` (object) **REQ** — Contains structured diagnostic details identifying the filter field whose comparator-driven value failed dependency validation, including the controlling dependee field reference.
          - `dependee` (object) **REQ** — Represents the dependee field whose state or constraints govern the validation rules applied to the comparator value of the current filter field.
            - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the dependee field whose constraints triggered the comparator value validation failure.
            - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the dependee field within the request structure whose constraints govern the comparator value validation.
          - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the filter field whose supplied value does not match the requirements of the comparator operator in use.
          - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the specific filter field whose value is incompatible with the comparator operator applied to it.
          - `param_name` (string) **REQ** [maxLen=256] — Represents the filter-specific parameter name identifying the request parameter associated with the comparator value mismatch.
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive error message summarizing the comparator-value mismatch encountered in the filter request.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome status of the response.
Possible values:
**error** - The request failed because the comparator-driven value did not satisfy dependency validation rules.
      - `FilterInvalidComparator` — Filter criteria error: invalid comparator
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Indicates the category of error associated with this response.
Possible values:
**INVALID_DATA** - An unsupported comparator operator was provided for the filter field.
        - `details` (object) **REQ** — Contains structured details identifying the filter field that received an unsupported comparator, including its location, parameter name, and the list of valid comparator values accepted for that field.
          - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the filter field to which an unsupported comparator operator was applied.
          - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the specific filter field within the request payload that carries the unsupported comparator operator.
          - `param_name` (string) **REQ** [maxLen=256] — Indicates the name of the filter parameter whose comparator was rejected, scoped as a filter-specific extension to the standard error detail.
          - `supported_values` (array of string) [minItems=1, maxItems=100, uniqueItems] **REQ** — Contains the list of comparator values that are valid for the offending filter field.
            items: [maxLen=256]
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive summary of the invalid-comparator error, identifying the rejected operator and the affected filter parameter.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall outcome of the request.
Possible values:
**error** - The request failed due to an invalid filter comparator.
      - `FilterEmptyFilterObject` — Filter criteria error: empty filter object
        - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Indicates the error classification for this failure.
Possible values:
**EXPECTED_FIELD_MISSING** - None of the expected filter fields were present in the submitted filter object.
        - `details` (object) **REQ** — Contains structured diagnostic detail about the empty filter object, including the parameter name and the list of fields that were expected but entirely absent from the filter expression.
          - `expected_fields` (array of object) [minItems=1, maxItems=100, uniqueItems] **REQ** — Contains the collection of fields that the filter object was expected to include, of which at least one must be present for the request to be valid. Each entry identifies the field by its API name and JSON path.
            - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of a field expected to be present in the filter object.
            - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSON path at which the expected field should be present within the filter object.
          - `param_name` (string) **REQ** [maxLen=256] — Indicates the name of the filter parameter associated with the empty filter object error. This field is a filter-specific extension to the standard error detail structure.
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive message summarizing the empty filter object error.
        - `status` (string) **REQ** [enum=['error']] — Represents the outcome status of the API response.
Possible values:
**error** - The request failed because the filter object did not contain any of the expected fields.
      - `FilterMandatoryNotFound` — Filter criteria error: mandatory field not found
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Indicates the error code identifying the category of failure.
Possible values:
**MANDATORY_NOT_FOUND** - A mandatory field was absent from the filter criteria.
        - `details` (object) **REQ** — Contains detailed information identifying the mandatory field that is absent from the request, including its API name, JSON path location, and, as a filter-specific extension, its parameter name.
          - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the mandatory field that was not found in the filter criteria.
          - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the mandatory field that is missing from the filter criteria.
          - `param_name` (string) **REQ** [maxLen=256] — Represents the parameter name associated with the missing mandatory field, as a filter-specific extension to the standard error detail.
        - `message` (string) **REQ** [maxLen=512] — Contains a brief error message describing which mandatory field was not found in the filter criteria.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome status of the response.
Possible values:
**error** - The request failed because a mandatory field was absent from the filter criteria.

- **401**: Authentication failed or the OAuth access token does not include the required scope. Resolution: A new access token must be generated with the ZohoCRM.settings.custom_views.READ scope. [application/json]
    > Represents the error response for an unauthorized get Custom Views request.
    oneOf:
      - `AuthenticationError` — Represents the error response returned when the authentication ticket is invalid or missing.
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the authentication failure.
Possible values:
**AUTHENTICATION_FAILURE** - The authentication ticket is invalid or missing.
        - `details` (object) **REQ** — Represents the error details containing validation information about the authentication failure.
        - `message` (string) **REQ** [enum=['Authentication failed']] — Represents the error message for the authentication failure.
Possible values:
**Authentication failed** - The provided authentication credentials are invalid or missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an authentication error.
      - `UnauthorizedResponse` — Represents the error response returned when the request is unauthorized due to an OAuth scope mismatch.
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code for the OAuth scope mismatch.
Possible values:
**OAUTH_SCOPE_MISMATCH** - The access token does not include the required scope for this operation.
        - `message` (string) **REQ** [maxLen=1024] — Represents the error message indicating the request is unauthorized due to an OAuth scope mismatch.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an authorization error.
        - `details` (object) **REQ** [maxProperties=0] — Represents the additional details for this error. An empty object indicates no additional details are available.

- **403**: Permission denied to retrieve Custom Views for this module. Resolution: The CRM administrator must grant the required permission to the user's profile. — Schema: `ModuleForbiddenErrorResponse` [application/json]
    > Represents the error response returned when the user does not have the required permissions for the specified module.
    schema: `ModuleForbiddenErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the permission error.
Possible values:
**NO_PERMISSION** - The user does not have the required permission for this module.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the permission denial.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered a permission error.
    - `details` (object) **REQ** — Represents the additional details about the permission error, including the required permissions.
      - `permissions` (array of string) [maxItems=50] **REQ** — Represents the list of permissions required to perform the action on this module.
        items: [maxLen=255]

**Scopes:** ZohoCRM.settings.custom_views.READ
