

from django.db import IntegrityError
from rest_framework import serializers

from .models import Post, Comment, StatusPost
from .telegramBot import bot


class PostSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField(source='get_rating')

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', ]

    def create(self, validated_data):
        user = self.context['request'].user
        chat_id = user.author.telegram_chat_id
        try:
            obj = Post.objects.create(**validated_data)
            obj.save(
                bot.sendMessage(chat_id, 'New post created!')
            )
        except IntegrityError:
            return obj


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'post']


class StatusPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusPost
        fields = '__all__'
        read_only_fields = ['author', 'post']

    # def create(self, validated_data):
    #     statusPostLastId = StatusPost.objects.latest('id')
    #     penultimate = StatusPost.objects.get(id=str(statusPostLastId.id-1))
    #     if penultimate:
    #         last = validated_data.pop('rating')
    #         if last < penultimate.rating:
    #             res = math.floor(penultimate.rating/last)
    #             validated_data['rating'] = penultimate.rating-res
    #         if penultimate.rating < last:
    #             res = math.floor(last/penultimate.rating)
    #             validated_data['rating'] = last-res
    #     # if not penultimate:
    #     #     StatusPost.objects.create(**validated_data)
    #     try:
    #         instance = super().create(validated_data)
    #     except Exception as e:
    #         raise serializers.ValidationError(f'Не удалось оценить по причине: {e}')
    #     return instance