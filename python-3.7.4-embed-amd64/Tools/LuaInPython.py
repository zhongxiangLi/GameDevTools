#!/usr/bin/python
# -*- coding: UTF-8 -*-

# lupa python与lua交互 https://pypi.org/project/lupa/#lua-tables

import lupa
from lupa import LuaRuntime


def run():
    lua = LuaRuntime(unpack_returned_tuples=True)
    
    print(lua.eval("{ [1] = -1 }"))
    

if __name__=="__main__":
    run()