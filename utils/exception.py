from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.views import Response
from rest_framework import status


def exception_handler(exc, context):
    # drf的exception做基础处理
    response = drf_exception_handler(exc, context)

    # 为空，做二次处理
    if response is None:
        # print(exc)
        # print(context)
        print('%s - %s - %s' % (context['view'], context['request'].method, exc))
        return Response(data={
            'detail': '服务器错误',
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True, headers={})
    return response
