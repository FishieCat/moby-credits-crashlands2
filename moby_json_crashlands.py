import json, sys

text = ''

with open(sys.argv[1], encoding='utf-8') as f:
    data = json.load(f)
    data_sorted = {}
    
    groups_sorted = sorted(data,key=lambda x:data[x]['order'])
    
    for group_id in groups_sorted:
        #print()
        #print('# ' + data[group_id]['element']['name']['text'])
        text += '\n' + data[group_id]['element']['name']['text'] + '\n'
        
        for key, entry in data[group_id]['element']['entries'].items():
            #print(" - " + entry['element']['type'])
            ele = entry['element']
            if 'names' in ele:
            
                #print( ele['role']['text'] )
                text += '\n' + ele['role']['text'] + '\n'
            
                names_sorted = sorted(ele['names'],key=lambda x:ele['names'][x]['order'])
                for name_id in names_sorted:
                    #print(" - - A NAME " + str(ele['names'][name_id]['order']))
                    text += ele['names'][name_id]['element']['name'] + '\n'
            elif 'name' in ele:
                #print(' - - A SINGLE NAME')
                text += ele['name']['name'] + '\n'
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(ele.keys())
    
text = text.strip()

with open(sys.argv[1] + '_moby.txt', 'w', newline='', encoding='utf-8') as f:
    f.write(text)
