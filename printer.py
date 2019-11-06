from latex import build_pdf


# def nameSystemProducer(names):
#     system = []
#     for n in names:
#         subNames = ' '.split(n)


# texFile = open('./texOut.txt', 'w+')
# texFile.write('\documentclass[11pt]{amsart}\n')
# texFile.write(r'\begin{document}')
# texFile.write('\n')
# texFile.write('hello LaTeX\n')
# texFile.write(r'\end{document}')
lines = '\documentclass[11pt]{amsart}\n' + r'\begin{document}' + '\n' + 'hello LaTeX\n' + r'\end{document}'
pdf = build_pdf(lines)
pdf.save_to('output.pdf')

# texFile = r'\documentclass[12pt]{amsart}' r'\begin{document}'
# pdf = build_pdf(lines)
# pdf.save_to('output.pdf')

# file = open('./article.txt')
# article = file.read()
#
# data = nltk.pos_tag(nltk.word_tokenize(article))


# data = "Martha went to the zoo and saw Tomas"
# data = nltk.pos_tag(nltk.word_tokenize(data))
# print(data)
# # print(nltk.word_tokenize(data))
# for d in data:
#     if d[1] == 'NNP':
#         print(d[0])
#         print(' ')


# names = []
# for entity in nltk.ne_chunk(data):
#     if hasattr(entity, 'label'):
#         if entity.label() == 'PERSON':
#             name = ' '.join(c[0] for c in entity)
#             # print(name)
#             if name not in names:
#                 names.append(name)
#
# for n in names:
#     print(n)
# print(names)

#     print(entity.label())
    # if isinstance(entity, nltk.tree.Tree):
    #     print('h')
    #     etext = " ".join([word for word, tag in entity.leaves()])
    #     label = entity.label()
    #     print(etext)
    #     print(label)
    #     print(' ')


