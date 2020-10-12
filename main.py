'Getting Information from IMDb library '
import imdb
ia = imdb.IMDb()
name = 'the mummy'
search = ia.search_movie(name)
# print(search)
# for i in search:
#     print(i)

the_mummy = ia.get_movie('0120616')
# for director in the_mummy['directors']:
#     print(director['name'])


# print('Genre:')
# for genre in the_mummy['genres']:
#     print(genre)

people = ia.search_person('Will Smith')
for person in people:
    print(person.personID, person['name'])
