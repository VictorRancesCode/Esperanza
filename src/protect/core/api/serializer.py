from rest_framework import serializers

from protect.core.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'email', 'first_name', 'last_name', 'nickname', 'place', 'date', 'photo', 'comment_photo',
                  'age', 'gender', 'detail', 'type_publication']

    def get_photo(self, person):
        request = self.context.get('request')
        photo = person.photo.url
        return request.build_absolute_uri(photo)
