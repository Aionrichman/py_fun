# from bingoCall import BingoCage
#
# bingo = BingoCage(range(3))
# a = bingo()
# b = bingo.pick()
# c = callable(bingo)
# print('{}|{}|{}'.format(a, b, c))

# from htmlTag import tag
#
# print('1-------------------------------------')
# print(tag('br'))
# print('2-------------------------------------')
# print(tag('p', 'hello'))
# print('3-------------------------------------')
# print(tag('p', 'hello', 'world'))
# print('4-------------------------------------')
# print(tag('p', 'hello', id=33))
# print('5-------------------------------------')
# print(tag('p', 'hello', 'world', cls='sidebar'))
# print('6-------------------------------------')
# print(tag(content='testing', name='img'))
# print('7-------------------------------------')
# my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
# print(tag(**my_tag))

# from clipCut import clip
# from htmlTag import tag
# from inspect import signature
#
# print(clip.__defaults__)
# print(clip.__code__)
# print(clip.__code__.co_varnames)
# print(clip.__code__.co_argcount)
# print(clip.__annotations__)
# print('-------------------------------------')
# sig = signature(clip)
# print(str(sig))
# for name, param in sig.parameters.items():
#     print(param.kind, ':', name, '=', param.default)
# for param in sig.parameters.values():
#     note = repr(param.annotation).ljust(13)
#     print(note, ':', param.name, '=', param.default)
# print('-------------------------------------')
# sig = signature(tag)
# my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
# bound_args = sig.bind(**my_tag)
# for key, value in bound_args.arguments.items():
#     print(key, '=', value)
# del my_tag['name']
# try:
#     bound_args = sig.bind(**my_tag)
# except TypeError:
#     print(TypeError)

# from htmlTag import tag
# from functools import partial
#
# picture = partial(tag, 'img', cls='pic-frame')
# print(picture(src='wum.jpg'))
# print(picture)
# print(tag)
# print(picture.func)
# print(picture.args)
# print(picture.keywords)

# from registration import *
#
# print(registry)
# print(register()(f3))
# print(registry)
# print(register(active=False)(f2))
# print(registry)

from vectorTest.vector2d_v0 import Vector2d
from vectorTest.vector_v1 import Vector

print(Vector([1, 2]) == Vector2d(1, 2))
print(Vector([1, 2]) != Vector2d(1, 2))

