def conv(sent):
  if type(sent) is str:
    return sent
  return conv(sent[0]) + '把' + conv(sent[2]) + conv(sent[1])

print(conv(('', '还记得', ('你', '答应过我', ('', '不会让我', ('', '找不见', '你'))))))
