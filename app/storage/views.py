from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Section
from .serializers import SectionSerializer


@api_view(['GET', 'POST'])
def section_list(request):
    if request.method == "GET":
        queryset = Section.objects.all()
        return Response(
            SectionSerializer(queryset, many=True).data
        )
    elif request.method == 'POST':
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
