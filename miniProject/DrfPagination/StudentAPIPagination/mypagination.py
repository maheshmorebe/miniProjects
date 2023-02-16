
# from rest_framework.pagination import PageNumberPagination

# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 5
#     page_query_param = 'p'
#     page_size_query_param = 'records'
#     max_page_size = 7
#     last_page_strings = 'end'

from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 6
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 8