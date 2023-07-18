def f(count, moves, previous, poss_p, poss_v): # создаём функцию
    if count <= 10: return moves % 2 == 0 # условие победы
    if moves == 0: return 0 # если за отведённое количество ходов игра не закончилась, возвращаем 0
    # создаём список ходов
    h = [f(count - 1, moves - 1, previous + [1], poss_p, poss_v),
         f(count - 2, moves - 1, previous + [2], poss_p, poss_v),
         f(count - 3, moves - 1, previous + [3], poss_p, poss_v),
         ]
    if previous[-2] == 1 and len(previous) % 2 == 1 and poss_v == 0: # если есть возможность сделать ход "-8", добавляем его в список
        h.append(f(count - 8, moves - 1, previous + [8], poss_p, 1))
    elif previous[-2] == 1 and len(previous) % 2 == 0 and poss_p == 0:
        h.append(f(count - 8, moves - 1, previous + [8], 1, poss_v))
    return any(h) if moves % 2 != 0 else all(h) # прописываем условие, которое проверяет подходят ли нам ходы (h), чтобы выиграть
print('19', [s for s in range(56, 10, -1) if f(s, 2, [0, 0], 0, 0)]) # берём значения s от 56 до 10, если с их помощью игра завершиться на 2 ходе (выиграет Ваня)
# далее ищём подходящие значения s, которые позволят выиграть Пете своим вторым ходом и находим их количество
print('20', len( [s for s in range(56, 10, -1) if f(s, 3, [0, 0], 0, 0) and not f(s, 1, [0, 0], 0, 0)] ))
# ищем значения s, при которых игра завершиться на 4 ходе, то есть выиграет Ваня своим вторым ходом
print('21', [s for s in range(56, 10, -1) if f(s, 4, [0, 0], 0, 0) and not f(s, 2, [0, 0], 0, 0)])



