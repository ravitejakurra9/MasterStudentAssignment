def find(num,fun):
    if fun == None:
        return num
    else:
        return fun(num)
def Zero(fun = None):
    return find(0,fun)
def One(fun = None):
    return find(1,fun)
def Two(fun = None):
    return find(2,fun)
def Three(fun = None):
    return find(3,fun)
def Four(fun = None):
    return find(4,fun)
def Five(fun = None):
    return find(5,fun)
def Six(fun = None):
    return find(6,fun)
def Seven(fun = None):
    return find(7,fun)
def Eight(fun = None):
    return find(8,fun)
def Nine(fun = None):
    return find(9,fun)

def Times(right):
  res = lambda left :  left * right
  return  res

def Plus(right):
  res = lambda left :  left + right
  return  res

def Minus(right):
  res = lambda left :  left - right
  return  res

def Divided_by(right):
  res = lambda left :  left // right
  return  res