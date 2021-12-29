import re

def solution(new_id):
    #step1
    if not new_id.islower():
        new_id = new_id.lower()

    #step2
    new_id = re.sub("[^a-z0-9-_.]","", new_id)

    #step3
    new_id = re.sub('[.]{2,}', ".", new_id)

    #step4
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]

    #step5
    if new_id == '':
        new_id += 'a'

    #step6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]

    #step7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    answer = new_id
    return answer
  
  
  
  
  # other
  
  def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
