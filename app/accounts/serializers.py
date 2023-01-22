from rest_framework import serializers

from .models import Author, User


class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)
    password2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = Author
        exclude = ['user', ]

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        author = Author.objects.create(
            telegram_chat_id=validated_data['telegram_chat_id'],
            email=validated_data['email'],
            user=user
        )
        return author

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли должны совпадать!')
        return data