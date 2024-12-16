from rest_framework import serializers

from tattoos.models import Style, Tattoo, Price, TattooArtist, TattooStudio
class TattooStudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooStudio
        fields = "__all__"

class TattooArtistSerializer(serializers.ModelSerializer):
    tattooStudio= TattooStudioSerializer(read_only = True)
    

    class Meta:
        model = TattooArtist
        fields = ['id','name',"tattooStudio","picture"]

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"

class TattooSerializer(serializers.ModelSerializer):
    style = StyleSerializer(read_only = True)
    price = PriceSerializer(read_only = True)
    tattooArtist = TattooArtistSerializer(read_only = True)
    def create(self, validated_data): 
        # когда в api создается сериалайзер, 
        # то заполняется специальное поле сериалайзера которое называется context
        # в него добавляется инфомрация по запросе, и доступна эта инфа
        # через self.context['request'], в частности там есть информация о пользовате
        if 'request' in self.context:
            # заполняем validated_data который используется для создания сущности в БД
            # данными из запроса
            validated_data['user'] = self.context['request'].user
            
        return super().create(validated_data)

    class Meta:
        model = Tattoo
        fields = ['id','name',"style","price","tattooArtist","picture"]

class TattooCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tattoo
        fields = "__all__"

class TattooArtistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooArtist
        fields = "__all__"