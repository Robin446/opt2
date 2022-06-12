with open('/Users/baaghi/Desktop/neer world/whatsapp problem/numbers.txt','r') as o, open('/Users/baaghi/Desktop/neer world/whatsapp problem/output3.html','w') as s, open('/Users/baaghi/Desktop/neer world/whatsapp problem/text.txt','r') as t:
    lines = o.readlines()
    msg = t.readline()
    for lines in lines:
        s.write(f'<a target="blank"href={"https://api.whatsapp.com/send/?phone=91"+lines+"&text="+msg} >'+lines+'</a>')
