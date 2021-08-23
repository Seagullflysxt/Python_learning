#pra.8-5
def describe_city(name,country = 'iceland'):
    #describe a cict
    print(f"{name.title()} is in {country.title()}")

describe_city('reykjavik')
describe_city('cambridge','england')
describe_city(country = 'china',name = 'shanghai')
