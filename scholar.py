from scholarly import scholarly

search_query = scholarly.search_author('Peirong Lin')
first_author_result = next(search_query)
n_citations = first_author_result['citedby']