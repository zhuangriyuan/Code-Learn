import ddddocr
ocr = ddddocr.DdddOcr()
with open("RandCode.gif", "rb") as f:
    img_code = f.read()
code = ocr.classification(img_code)
print(code)
