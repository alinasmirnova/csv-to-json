# Fields combination rule
To create a mapping rule to combine multiple fields into a new field use this syntax:
    ```commandline
    ;;sourse_type1|souce_type2;destination
    ```
  You can find an example in ```./tests/integration_tests/test_data/mappings.csv```

# Article number
There are two ways to calculate article number according to the task:
1. Take field ```article_number```
2. Take combination of fields ```article_number_{N}```

I've chosen the first option as a more straightforward one. But there are ways to switch to the second option:
1. Use the fields combination rule to combine article numbers into one entity
2. Change method ```Variation.get_article_number``` logic to combine all articles number only for grouping variations (they'll still be separate article fields) 