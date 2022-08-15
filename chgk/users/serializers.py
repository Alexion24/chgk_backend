from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    age = serializers.IntegerField(required=True)
    pants_color = serializers.CharField(required=True)
    relationship_status = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'age',
            'pants_color',
            'relationship_status'
        ]

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            age=self.validated_data['age'],
            pants_color=self.validated_data['pants_color'],
            relationship_status=self.validated_data['relationship_status']
        )
        password = self.validated_data['password']

        user.set_password(password)
        user.save()
        return user
