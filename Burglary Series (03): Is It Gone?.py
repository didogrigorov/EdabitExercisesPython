def find_it(items, name):
    if name.lower() in items.keys():
        return "{} is gone...".format(name.capitalize())
    else:
        return "{} is here".format(name.capitalize())


print(find_it({
  "tv": 30,
  "stereo": 50,
  "julius": 100,
}, "julius"))