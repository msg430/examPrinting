from latex import build_pdf
import os


# ranges = [16, 15, 15, 15]
ranges = [2, 1, 1, 1]

version = []
reader = open('/users/matt/Box Sync/Math 1030 - Fall 19/Exams/Exam 2 Stuff/Exam2_V1.tex')
version.append(reader.readlines())
reader = open('/users/matt/Box Sync/Math 1030 - Fall 19/Exams/Exam 2 Stuff/Exam2_V2.tex')
version.append(reader.readlines())
print(version[0][5])

number = 0
for r in ranges:
    number += 1
    letter = ord('A')-1
    for c in range(r):
        letter += 1
        identifier = str(number) + chr(letter)
        version[r % 2][5] = r'\newcommand{\edition}{\fbox{\Huge{\textbf{' + identifier + '}}}}'
        lines = ' '.join(version[r % 2])
        pdf = build_pdf(lines)
        outName = 'Exam' + identifier + '.pdf'
        pdf.save_to(outName)

#       print the pdf

        os.remove(outName)





# # texFile = open('./texOut.txt', 'w+')
# # texFile.write('\documentclass[11pt]{amsart}\n')
# # texFile.write(r'\begin{document}')
# # texFile.write('\n')
# # texFile.write('hello LaTeX\n')
# # texFile.write(r'\end{document}')
# lines = '\documentclass[11pt]{amsart}\n' + r'\begin{document}' + '\n' + 'hello LaTeX\n' + r'\end{document}'
# pdf = build_pdf(lines)
# pdf.save_to('output.pdf')
#
# # texFile = r'\documentclass[12pt]{amsart}' r'\begin{document}'
# # pdf = build_pdf(lines)
# # pdf.save_to('output.pdf')
#
# # file = open('./article.txt')
# # article = file.read()
# #
# # data = nltk.pos_tag(nltk.word_tokenize(article))
#
#
# # data = "Martha went to the zoo and saw Tomas"
# # data = nltk.pos_tag(nltk.word_tokenize(data))
# # print(data)
# # # print(nltk.word_tokenize(data))
# # for d in data:
# #     if d[1] == 'NNP':
# #         print(d[0])
# #         print(' ')
#
#
# # names = []
# # for entity in nltk.ne_chunk(data):
# #     if hasattr(entity, 'label'):
# #         if entity.label() == 'PERSON':
# #             name = ' '.join(c[0] for c in entity)
# #             # print(name)
# #             if name not in names:
# #                 names.append(name)
# #
# # for n in names:
# #     print(n)
# # print(names)
#
# #     print(entity.label())
#     # if isinstance(entity, nltk.tree.Tree):
#     #     print('h')
#     #     etext = " ".join([word for word, tag in entity.leaves()])
#     #     label = entity.label()
#     #     print(etext)
#     #     print(label)
#     #     print(' ')
#
#
