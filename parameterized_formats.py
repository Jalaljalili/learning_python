names = [
    ('Ali', 'Mirsadeghi'),
    ['Mina', 'Khojeiri'],
    ['Reza', 'Bagheri'],
    ['Sara', 'Akbari'],
    ['Ahmad', 'Salimi']
    ]

box = '{corner}{0:{border}>{width}}{corner}\n{side}{title:^{width}}{side}\n{corner}{0:{border}>{width}}{corner}'

for first, last in names:
    print(box.format('', border='=', side='\u2016', corner='*', title=first, width=len(first) +2))
    print(box.format('', border='-', side='|', corner='+', title=last, width=len(last) +10))