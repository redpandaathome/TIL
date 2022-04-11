def domain_name(url):
    url=url.replace("https://", "")
    url=url.replace("http://", "")
    url=url.replace("www.", "")
    return url.split('.')[0]


#
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


#
def domain_name(url):
    from re import findall, VERBOSE
    
    try:
        url = findall("""\A
                        (?: http
                        s?
                        ://)?         # matches http:// or https:// or nothing
                        
                        (?: www.)?    # matches www. or nothing
                        
                        ([- a-z]+)    # matches a sequence of letters and dashes
                        
                        (?: .com|.ru)     # matches either .com or .ru
                        (?: [/ a-z]+)?    # matches a sequence or letters and slashes
                        \Z""", url, VERBOSE)
        return url[0]
    except:
        return "Invalid URL."