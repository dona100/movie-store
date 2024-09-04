from rest_framework import serializers
from .models import Genre, Actor, Director, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'date_of_birth']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name', 'date_of_birth']

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actor.objects.all())
    director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all())

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'description', 'release_date',
            'genres', 'actors', 'director', 'price', 'stock'
        ]
    
    def create(self, validated_data):
        genres = validated_data.pop('genres')
        actors = validated_data.pop('actors')
        director = validated_data.pop('director')

        movie = Movie.objects.create(director=director, **validated_data)

        
        movie.genres.set(genres)
        movie.actors.set(actors)
        
        return movie

    def update(self, instance, validated_data):
        genres = validated_data.pop('genres', None)
        actors = validated_data.pop('actors', None)
        director = validated_data.pop('director', None)

        if director:
            instance.director = director
        
        if genres is not None:
            instance.genres.set(genres)

        if actors is not None:
            instance.actors.set(actors)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance


