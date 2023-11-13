# Fields combination rule
To create a mapping rule to combine multiple fields into a new field use this syntax:
    ```
    ;;sourse_type1|souce_type2;destination
    ```
  You can find an example in ```./tests/integration_tests/test_data/mappings.csv```

# Article number
There are two ways to calculate article number according to the task:
1. Take field ```article_number```
2. Take combination of fields ```article_number_{N}```

I've chosen the first option as a more straightforward one. But there are ways to switch to the second option:
1. Use the fields combination rule to combine article numbers into one entity
2. Change method ```Variation.get_article_number``` logic to combine all articles number only for grouping variations 
(they'll still be separate article fields)

# Output
Main entry point for creating catalog is ```CatalogBuilder.build_catalog```. Method returns catalog as a dictionary 
that can be converted to json or used as a field for another data contract

# Run tests
To run unit tests run ```py -m unittest discover``` in the project root directory (csv-to-json)