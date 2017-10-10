
def combinedata(typedict,mothertype,result):
    for key, value in typedict.items():
        if value == 1:
            result += key + ','
        else:
            result += str(value) + '(' + key  + '),'
    result=result[:-1]
    if len(typedict)>1:
        result ='('+result+')'
    return mothertype + ' of ' + result

def simtypehandler(item,typedict,mothertype):
    return mothertype

def dicthandler(item,typedict,mothertype):
    result=''
    for key,value in item.items():
        keytypestr=structmake(key)
        valuetypestr=structmake(value)
        typedict[keytypestr + ' -> ' + valuetypestr ] =\
            typedict.get(keytypestr + ' -> ' + valuetypestr , 0) + 1
    return combinedata(typedict,mothertype,result)

def tulisthandler(item,typedict,mothertype):
    result=''
    for litem in item:
        valuetypestr = structmake(litem)
        typedict[valuetypestr] = typedict.get(valuetypestr, 0) + 1
    return combinedata(typedict, mothertype, result)

structtype={
    type('s'):('string',simtypehandler),
    type(1):('int',simtypehandler),
    type(dict()):('dict',dicthandler),
    type(tuple()):('tuple',tulisthandler),
    type(list()):('list',tulisthandler)
}

def structmake(item):
    typedict = {}
    itemtype=structtype[type(item)]
    return itemtype[1](item,typedict,itemtype[0])



data={'a':1,'b':2,('a','b'):{'c':3},('a','b','c',1,2,3,):4}
print(structmake(data))