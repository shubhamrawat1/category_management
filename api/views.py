from rest_framework.response import Response
from rest_framework.views import APIView
from category.models import *
from rest_framework import status
from api import serializers


class CategoryCreateAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        cat_name = request.data.get('cat_name')
        if not cat_name:
            return Response({"statusType": "failed", "message": 'Please Provide Category Name', "status": 400},
                            status=status.HTTP_400_BAD_REQUEST)

        cat_image = request.data.get('cat_image')
        is_active = request.data.get('is_active')
        if is_active == 'true' or is_active == 'True':
            is_active = True
        elif is_active == 'false' or is_active == 'False':
            is_active = False
        elif is_active is None:
            is_active = True
        else:
            return Response({"statusType": "failed",
                             "message": 'Invalid value for is_active. Please provide true or false or leave blank.',
                             "status": 400},
                            status=status.HTTP_400_BAD_REQUEST)

        cat_obj = Category.objects.create(cat_name=cat_name, is_active=is_active, cat_image=cat_image)
        serializer = serializers.CategorySerializer(cat_obj)

        return Response({"statusType": "success", "data": serializer.data, "status": 200}, status=status.HTTP_200_OK)


class CategoryUpdateView(APIView):
    authentication_classes = []
    permission_classes = []

    def patch(self, request, *args, **kwargs):

        cat_id = kwargs.get('pk')

        try:
            cat_id = int(cat_id)
        except Exception as e:
            return Response({"statusType": "failed", "message": 'Invalid Id', "status": 400},
                            status=status.HTTP_400_BAD_REQUEST)

        category = Category.objects.filter(id=int(cat_id)).first()
        _data = request.data.copy()
        if not category:
            return Response({"statusType": "success",
                             "message": 'Category not Found',
                             "status": 200},
                            status=status.HTTP_200_OK)
        else:
            serializer = serializers.CategorySerializer(instance=category,
                                                              data=_data,)
            if serializer.is_valid():
                serializer.save()

            return Response({"statusType": "success", "data": serializer.data, "status": 200},
                            status=status.HTTP_200_OK)


class CategoryViewAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        cat_id = kwargs.get('pk')

        try:
            cat_id = int(cat_id)
        except Exception as e:
            return Response({"statusType": "failed", "message": 'Invalid Id', "status": 400},
                            status=status.HTTP_400_BAD_REQUEST)

        category = Category.objects.filter(id=int(cat_id)).first()

        if not category:
            return Response({"statusType": "success",
                             "message": 'Category not Found',
                             "status": 200},
                            status=status.HTTP_200_OK)
        else:
            serializer = serializers.CategorySerializer(instance=category)

            return Response({"statusType": "success", "data": serializer.data, "status": 200},
                            status=status.HTTP_200_OK)


class CategoryDeleteAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def delete(self, request, *args, **kwargs):
        cat_id = kwargs.get('pk')

        try:
            cat_id = int(cat_id)
        except Exception as e:
            return Response({"statusType": "failed", "message": 'Invalid Id', "status": 400},
                            status=status.HTTP_400_BAD_REQUEST)

        category = Category.objects.filter(id=int(cat_id)).first()
        if not category:
            return Response({"statusType": "success",
                             "message": 'Category not Found',
                             "status": 200},
                            status=status.HTTP_200_OK)
        else:
            category.delete()

            return Response({"statusType": "success", "message": 'Successfully Deleted', "status": 200},
                            status=status.HTTP_200_OK)


class CategoryListAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)

        return Response({"statusType": "success", "data": serializer.data, "status": 200},
                        status=status.HTTP_200_OK)

