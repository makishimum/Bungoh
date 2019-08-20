import re
base_path = "C:/Users/maki.umekita/aozorabunko/"

akutagawa_indexpath = r"C:\Users\maki.umekita\aozorabunko\index_pages\【akutagawa】_person879.html"
kikuchi_indexpath = r"C:\Users\maki.umekita\aozorabunko\index_pages\【kikuchi】person83.html"
tanizaki_indexpath = r"C:\Users\maki.umekita\aozorabunko\index_pages\【tanizaki】person1383.html"
dazai_indexpath = r"C:\Users\maki.umekita\aozorabunko\index_pages\【dazai】person35.html"


#作家一覧のページを開き、全文をakutagawa_listリストにいれる
with open(akutagawa_indexpath,'r',encoding="utf-8_sig") as f:
  akutagawa_list = f.readlines()

  #akutagawa_listの中で、「新字新仮名」という一文が入っているものだけを抽出しakutagawa_newJapリストに格納する
akutagawa_newJap = [s for s in akutagawa_list if '新字新仮名' in s]

 #akutagawa_newJapの中で、パスを表した部分を抜き出して入れる。その部分がないものについては適当にスローする。
akutagawa_textpaths=[]
for fullname in akutagawa_newJap:
  try:
    akutagawa_textpaths =base_path + re.search(r"cards/[0-9]{6}/card.*\.html", fullname).group()
    print(akutagawa_textpaths)
  except AttributeError:
    i = 1

#akutagawa_newJapの中で、パスを表した部分を抜き出して入れる。その部分がないものについては適当にスローする。

