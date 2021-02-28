import dropbox
from datetime import datetime


def dropbox_upload(text,questions):
    import dropbox
    dbx = dropbox.Dropbox('sl.AsGcy_ov10aSnTys7mWaabSPjKVUazjPdp0TtBhkg2ArY9A2xmJzOvFclu7G_MmitBxgNDfReR1dY1s7osFwl3xszYzLS9HwvdLdV6YE5_sitpoO2csuHa9Y9emoUIilGXQJlAEfCZU')
    result="Summary"+"\n"+text+"\n"+"\n"+"Questions"+"\n"
    for question in questions:
        result+=question['question']+"\t"+question['answer']+"\n"
    summarized_result=bytes(result,'utf-8')
    from datetime import datetime
    today = datetime.now().strftime("%H:%M,%d-%m-%Y")
    dbx.files_upload(summarized_result, "/smlr/"+" Time: "+today.split(',')[0]+","+" Date: "+today.split(',')[1]+".txt")
