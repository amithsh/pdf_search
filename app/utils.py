import fitz

def process_pdf(filepath,keyword):
    try:
        doc = fitz.open(filepath)
    except Exception as e :
        return {"error":str(e)}
    

    pagesfound = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_instance = page.search_for(keyword)

        if text_instance:
            pagesfound.append(page_num + 1)    

    doc.close()

    return pagesfound