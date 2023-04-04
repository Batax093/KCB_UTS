from decision_tree_forward import knowledge_base
from decision_tree_traversal import knowledge_base_
from decision_tree_forward import v_ordo, v_pisces, v_amfibia, v_aves, v_reptilia, v_mammalia
from decision_tree_forward import i_ordo, i_annelida, i_anthropoda, i_cnidaria, i_echinodermata, i_mollusca, i_nemathelminthes, i_platyhelmithes, i_porifera, i_protozoa
from collections import deque

condition = True


def traverse_decision_tree_(node):
    if isinstance(node, dict):
        for question, child_node in node.items():
            answer = input(question + "\n(Ya/Tidak): ")
            if answer == "Ya":
                return traverse_decision_tree_(child_node["Ya"])
            elif answer == "Tidak":
                return traverse_decision_tree_(child_node["Tidak"])
            else:
                print("Jawaban tidak valid, silakan masukkan 'Ya' atau 'Tidak'")
                return traverse_decision_tree_(node)
    else:
        return node
    return None


def traverse_decision_tree_bfs(node):
    queue = deque([node])
    while queue:
        current_node = queue.popleft()
        if isinstance(current_node, dict):
            for question, child_node in current_node.items():
                answer = input(question + "\n(Ya/Tidak): ")
                while answer not in ["Ya", "Tidak"]:
                    print("Jawaban tidak valid, silakan masukkan 'Ya' atau 'Tidak'")
                    answer = input(question + "\n(Ya/Tidak): ")
                queue.append(child_node[answer])
        else:
            return current_node
    return None


def forward_reasoning(knowledge_base, ciri_ciri):
    queue = deque([knowledge_base])
    while queue:
        current_node = queue.popleft()
        for key in current_node:
            if key in ciri_ciri:
                if isinstance(current_node[key], dict):
                    queue.append(current_node[key])
                else:
                    return current_node[key]
    raise ValueError('Hewan tidak terdaftar.')


def forward_reasoning_input():
    array = []
    jawaban = ''
    start = 'Apakah hewan bertulang belakang?'
    print(start)
    jawaban = input('(Ya/Tidak): ')
    array.append(start)
    array.append(jawaban)
    if jawaban == 'Ya':
        index = len(v_ordo)
        for i in range(index):
            print(v_ordo[i])
            jawaban = input('(Ya/Tidak): ')
            if jawaban == 'Ya':
                array.append(v_ordo[i])
                array.append(jawaban)
                if i == 0:
                    index_ = len(v_pisces)
                    for x in range(index_):
                        print(v_pisces[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(v_pisces[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result
                elif i == 1:
                    index_ = len(v_amfibia)
                    for x in range(index_):
                        print(v_amfibia[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(v_amfibia[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result

                elif i == 2:
                    index_ = len(v_reptilia)
                    for x in range(index_):
                        print(v_reptilia[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(v_reptilia[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result

                elif i == 3:
                    index_ = len(v_aves)
                    for x in range(index_):
                        print(v_aves[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(v_aves[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result

                elif i == 4:
                    index_ = len(v_mammalia)
                    for x in range(index_):
                        print(v_mammalia[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(v_mammalia[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result
            elif jawaban == 'Tidak':
                continue
            else:
                print('Masukkan "Ya" atau "Tidak"')
                return forward_reasoning_input()
    elif jawaban == 'Tidak':
        index = len(i_ordo)
        for i in range(index):
            print(i_ordo[i])
            jawaban = input('(Ya/Tidak): ')
            if jawaban == 'Ya':
                array.append(i_ordo[i])
                array.append(jawaban)
                if i == 0:
                    index_ = len(i_annelida)
                    for x in range(index_):
                        print(i_annelida[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(i_annelida[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result
                elif i == 1:
                    index_ = len(i_mollusca)
                    for x in range(index):
                        print(i_mollusca[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(i_mollusca[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result

                elif i == 2:
                    index_ = len(i_anthropoda)
                    for x in range(index):
                        print(i_anthropoda[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(i_anthropoda[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result

                elif i == 3:
                    index_ = len(i_protozoa)
                    for x in range(index):
                        print(i_protozoa[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(i_protozoa[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result

                elif i == 4:
                    index_ = len(i_porifera)
                    for x in range(index):
                        print(i_porifera[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(i_porifera[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result

                elif i == 5:
                    index_ = len(i_platyhelmithes)
                    for x in range(index):
                        print(i_platyhelmithes[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(i_platyhelmithes[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result

                elif i == 6:
                    index_ = len(i_nemathelminthes)
                    for x in range(index):
                        print(i_nemathelminthes[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(i_nemathelminthes[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result

                elif i == 7:
                    index_ = len(i_cnidaria)
                    for x in range(index):
                        print(i_cnidaria[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(i_cnidaria[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result

                elif i == 8:
                    index_ = len(i_echinodermata)
                    for x in range(index):
                        print(i_echinodermata[x])
                        jawaban = input('(Ya/Tidak): ')
                        if jawaban == 'Ya':
                            array.append(i_echinodermata[x])
                            array.append(jawaban)
                            print(array)
                            result = forward_reasoning(knowledge_base, array)
                            return result
            elif jawaban == 'Tidak':
                continue
            else:
                print('Masukkan "Ya" atau "Tidak"')
                return forward_reasoning_input()
    else:
        print('Masukkan pilihan "Ya" atau "Tidak"')
        return forward_reasoning_input()


def tampilan(option):
    if option == 1:
        forward = forward_reasoning_input()
        forward_ = " ".join(str(elem) for elem in forward)
        result = 'Hewan dengan ciri-ciri yang dimaksud adalah ' + \
            forward_
        return result
    elif option == 2:
        bfs = traverse_decision_tree_bfs(knowledge_base_)
        bfs_ = " ".join(str(elem) for elem in bfs)
        result = 'Hewan dengan ciri-ciri yang dimaksud adalah ' + bfs_
        return result
    elif option == 3:
        traversal = traverse_decision_tree_(knowledge_base_)
        traversal_ = " ".join(str(elem) for elem in traversal)
        result = 'Hewan dengan ciri-ciri yang dimaksud adalah ' + traversal_
        return result
    else:
        print('Tampilan menu salah!')
        return None


def pengulangan(condition):
    while condition == True:
        print('Program Sistem Klasifikasi hewan menggunakan metode otomasi\n1. Pencarian menggunakan metode forward\n2. Pencarian menggunakan metode pencarian BFS\n3. Pencarian menggunakan metode traversal otomasi\n')
        option = int(input('Masukkan pilihan menu: '))

        start = tampilan(option)
        print(start, '\n')
        print('Apakah anda ingin mencari yang lain?')
        condition = input('(Ya/Tidak): ')
        if condition == 'Ya':
            condition = True
            return pengulangan(condition)
        elif condition == 'Tidak':
            condition = False
            return 'Terima kasih telah memakai program kami'
        else:
            print('Pilihan salah!')
            return pengulangan(condition)


a = pengulangan(condition)
print(a)
