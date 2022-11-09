from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'draft', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)


    # реализовано следующее поведение при валидации:
    # если пользователь не обладает статусом админа - is_staff == True то
    # пользователь не может создать объявление со статусом 'OPEN' ни по умолчанию, ни указав 'OPEN' явно
    # если у него есть 10 и боолее(*) объявлений со статусом 'OPEN'
    # пользователь не может изменить статус объявления на 'OPEN' если у него есть 10 и боолее(*) объявлений со статусом 'OPEN'
    # пользователь всегда может создать объявление указав явно статус 'CLOSED'
    # если пользователь is_staff == True, он может менять статус объявления на 'OPEN' у любого пользователя,
    # даже если в этом случае их станет больше 10 (*)
    # пользователь админ - is_staff == True может иметь больше 10 открытых собственных объявлений


    def validate(self, data):

        if self.context["request"].user.is_staff == False:
            count = Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN').count()
        else:
            count = 1
        if 'status' in data and data['status'] == 'CLOSED':
            return data
        else:
            if count < 10:
                return data
            else:
                raise serializers.ValidationError(f'Количество открытых объявлений {count} удалите одно или несколько объявлений или измените их статус на CLOSED')

