from rest_framework import serializers

from accounts.models import Articles, User


class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, use_url=True)

    class Meta:
        model = Articles
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        user = self.context["request"].user
        article = Articles.objects.create(
            title=validated_data["title"],
            content=validated_data["content"],
            user=user,
        )
        if "image" in validated_data:
            article.image = validated_data["image"]
        article.save()
        return article
