import re


def regexForKey(link):
    url = link
    getKey = re.compile(r'(d\/)+(\d|\D|\w|\W|\s|S){20,45}(\/)+')
    mo = getKey.search(url)
    regexKey = mo.group()
    finalKey = regexKey.replace("d/", "")
    finalKey = finalKey.replace("/", "")
    return finalKey
