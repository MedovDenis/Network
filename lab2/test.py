# import time

# def test_time(func):
#     def wapper(*args, **kwargs):
#         st = time.time()
#         res = func(*args, **kwargs)
#         et = time.time()
#         dt = et - st
#         print('Время работы: {}'.format(dt))
#         return res
#     return wapper
