def query_splitting(query):
    main_query = query.split("and")[0]
    second_query = query.split("and")[1]
    print(main_query)
    print(second_query)
    return main_query, second_query


print(query_splitting("Open Youtube and Search Atif"))