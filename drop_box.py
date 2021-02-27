import dropbox
from datetime import date


def dropbox_upload(text,questions):
    dbx = dropbox.Dropbox('sl.AsHtNtgZ_L2vZrKn0IIBTk0XPAbfbOSQGviTxTEgIImNaUYXoHRmtIbbYtli43fxtOckJVaJdDjNoZwvRaXkLkduz1_UxtUTPFjAq2RaMDRSfMe3Z2ylKqKAE9TJTk-IsaXpOUTMCKA')
    summarized_text=bytes(text,'utf-8')
    summarized_questions=bytes(questions,'utf-8')
    total_content= "Summary:"+text+"Possible Questions:"+questions
    total_content=bytes(total_content,'utf-8')
    today = date.today().strftime("%m:%d:%Y")
    dbx.files_upload(total_content, "/smlr/"+today+".txt")

