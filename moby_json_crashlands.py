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
        
        entries_sorted = sorted(data[group_id]['element']['entries'],key=lambda x:data[group_id]['element']['entries'][x]['order'])
        
        for key in entries_sorted:
        
            entry = data[group_id]['element']['entries'][key]
            
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
            
                if 'role' in ele:
                    text += '\n' + ele['role']['text'] + '\n'
            
                #print(' - - A SINGLE NAME')
                text += ele['name']['name'] + '\n'
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(ele.keys())
    
text = text.strip()

with open(sys.argv[1] + '_moby.txt', 'w', newline='', encoding='utf-8') as f:
    f.write(text)
