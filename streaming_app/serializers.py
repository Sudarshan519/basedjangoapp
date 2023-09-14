import json
from rest_framework import serializers
import mimetypes

from streaming_app.file_upload import  download_blob, upload_to_gcs
from userr.models import CustomUser
from .models import *
class MovieSerializer(serializers.ModelSerializer):
    # download_path = serializers.CharField(read_only=True )
    # file = serializers.FileField()
    def create(self, validated_data):
        # print(validated_data)
        # # title=validated_data['title']
        # uploaded_file=validated_data['movie_path']
        # print("File Name:", uploaded_file.name)
        # print("Content Type:", uploaded_file.content_type)
        # print("File Size:", uploaded_file.size)
        # # print("MIME Type:", mime_type)
        # # print(upload_to_gcs(title))
        # # upload_to_gcs(uploaded_file.name,uploaded_file,uploaded_file.content_type)
        # mime_type, _ = mimetypes.guess_type('file.png', strict=False)  # Provide a filename for better detection
        # validated_data['url']=uploaded_file.name
        # del validated_data['movie_path']
        # print(download_blob(uploaded_file.name+uploaded_file.content_type.split('/')[-1])        )
        # validated_data['name'] = 'SomeName'
        # validated_data['width']= 120
        # validated_data['height']= 120
        return super().create(validated_data)
 
 
          
    # def to_representation(self, instance):
    #     # Call the parent to_representation method
    #     data = super().to_representation(instance)
        
    #     # Generate the file content using the custom method
    #     # file_content = self.generate_file_content(instance)
    #     # If you want to include the custom file content in list serialization,
    #     # you can check if 'self.context' contains 'many=True'
    #     if self.context.get('many', False):
    #         # Generate the file content using the custom method
    #         data['path']=download_blob(self.title)

    #         # Add the file content to the serializer output
    #         data['file_content'] = file_content
    #     # Add the file content to the serializer output
    #     # data['file_content'] = file_content

    #     return data
    class Meta:
        model=Movie
        exclude=()#("movie_path",)
        # include=("download_path")
        # include=('download_path')
        # fields=[ "download_path"]
class MovieSubscribedSerializer(serializers.ModelSerializer):
     class Meta:
        model=Movie
        exclude=()
        # include=("donwload_path")
        # read_only=["download_path"]
    # def perform_create(self, serializer):
    #         print(serializer.data)
    #         print(self.movie_path)
    #         print(serializer)
            # serializer.save(user=self.request.user)

class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Episode
        fields=("id","label","tv_show","desc","movie_path")
    def perform_create(self, serializer):
            
            print(json.dumps(serializer))
            serializer.save(user=self.request.user)
        
class TVSeriesSerializer(serializers.ModelSerializer):
    episode=EpisodeSerializer(many=True,read_only=True)


    class Meta:
        model=TVSeries
        exclude=()
        
        include=["episode"]
 


class UserSerializer(serializers.ModelSerializer):
    movies=MovieSerializer(many=True)
    tvshows=TVSeriesSerializer(many=True)
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    class Meta:
        model=CustomUser
        # fields='__all__'
        fields=('username','email','movies','tvshows')

    

class HomeSerializer(serializers.Serializer):
    movies=MovieSerializer(many=True)
    tvshows=TVSeriesSerializer(many=True)