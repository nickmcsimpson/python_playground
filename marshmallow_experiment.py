from datetime import date
from pprint import pprint

from marshmallow import Schema, fields, EXCLUDE, pre_load


class BirthdaySchema(Schema):
    day = fields.Str()
    month = fields.Str()
    year = fields.Str()


class ArtistSchema(Schema):
    name = fields.Str()
    birthday = fields.Nested(BirthdaySchema)


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())


class FamousSchema(Schema):
    name = fields.Str()
    artwork = fields.Str(data_key='title')
    birthyear = fields.Str()

    @pre_load
    def grab_name(self, data, **kwargs):
        artist = data.pop('artist')
        year = artist.get('history').get('year')
        data['name'] = artist.get('name')
        data['birthyear'] = year
        return data


birthday = dict(year='1996', month='4', day='18')
bowie = dict(name="David Bowie", birthday=birthday)
album = dict(artist=bowie, title="Hunky Dory", release_date=date(1971, 12, 17))


album_schema = AlbumSchema()
result = album_schema.dump(album)
pprint(result, indent=2)
# { 'artist': {'name': 'David Bowie'},
#   'release_date': '1971-12-17',
#   'title': 'Hunky Dory'}

famous_schema = FamousSchema()
result = famous_schema.load(album, unknown=EXCLUDE)
pprint(result, indent=2)

