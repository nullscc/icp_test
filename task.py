#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-08-07 11:24:11

import functools

    def decorator(decorator_arg):
        print("start decorator")
        def mydecorator(func):
            @functools.wraps(func)
            def wrapper(*arg, **kwargs):
                print("excute func, decorator_arg is:{0}".format(decorator_arg))
                return func(*arg, **kwargs)
            return wrapper
        return mydecorator

    def decorator2():
        def mydecorator(func):
            @functools.wraps(func)
            def wrapper(*arg, **kwargs):
                print("in decorator2")
                return func(*arg, **kwargs)
            return wrapper
        return mydecorator

    @decorator2()
    @decorator("decorator arg test")
    def hello(*arg, **kwargs):
        print("hello decorator arg:{0} kwargs:{1}".format(arg, kwargs))

    print("before hello")
    hello("hi", one=1, two=2)
