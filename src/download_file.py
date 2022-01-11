import gdown


def downloadFile(keyUrl, fileName):
    url1 = 'https://drive.google.com/uc?id='
    url2 = keyUrl
    finurl = url1+url2
    output = fileName
    gdown.download(finurl, output, quiet=False)
